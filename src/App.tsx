import { useEffect, useMemo, useRef, useState, type CSSProperties } from 'react';
import logoImage from './assets/logo-raio.png';
import { courses } from './data/courses';
import { Course } from './types';

const timelineStart = new Date('2026-02-01T00:00:00');
const timelineEnd = new Date('2026-12-01T00:00:00');
const oneDayMs = 1000 * 60 * 60 * 24;
const totalDurationMs = timelineEnd.getTime() - timelineStart.getTime();

const monthLabels = ['Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov'];

const programDefinitions = [
  { program: 'CEPM/RAIO', label: 'CEPM/RAIO (Curso Esp. de Policiamento com Motocicletas)', color: 'var(--color-cepm)' },
  { program: 'CMB', label: 'CMB (Curso de Motociclista Batedor)', color: 'var(--color-cmb)' },
  { program: 'CPM', label: 'CPM (Curso de Policiamento com Motocicletas)', color: 'var(--color-cpm)' },
  { program: 'CIR/RAIO', label: 'CIR/RAIO (Curso de Intervenção Rápida)', color: 'var(--color-cir)' },
  { program: 'CTM/RAIO', label: 'CTM/RAIO (Curso Tático Motorizado)', color: 'var(--color-ctm)' },
];

const diffInDays = (start: Date, end: Date) => {
  const diff = Math.abs(end.getTime() - start.getTime());
  return Math.ceil(diff / oneDayMs);
};

const formatDate = (date: Date) => {
  const day = String(date.getDate()).padStart(2, '0');
  const month = String(date.getMonth() + 1).padStart(2, '0');
  return `${day}/${month}`;
};

function App() {
  const [activeCourse, setActiveCourse] = useState<Course | null>(null);
  const [visiblePrograms, setVisiblePrograms] = useState<Set<string>>(
    () => new Set(programDefinitions.map((item) => item.program)),
  );
  const hideTimer = useRef<number | null>(null);

  const months = useMemo(() => {
    const items: Array<{ width: number; label: string }> = [];
    let current = new Date(timelineStart);

    for (let index = 0; index < monthLabels.length; index += 1) {
      const next = new Date(current.getFullYear(), current.getMonth() + 1, 1);
      const span = next.getTime() - current.getTime();
      const width = (span / totalDurationMs) * 100;
      items.push({ width, label: `${monthLabels[index]}/26` });
      current = next;
    }

    return items;
  }, []);

  const filteredCourses = useMemo(
    () => courses.filter((course) => visiblePrograms.has(course.program)),
    [visiblePrograms],
  );

  const programStats = useMemo(() => {
    const totals = new Map<string, number>();
    filteredCourses.forEach((course) => {
      totals.set(course.program, (totals.get(course.program) ?? 0) + 1);
    });
    return totals;
  }, [filteredCourses]);

  const totalDurationDays = useMemo(
    () =>
      filteredCourses.reduce((acc, course) => acc + diffInDays(course.startDate, course.endDate), 0),
    [filteredCourses],
  );

  const firstCourse = useMemo(() => {
    if (filteredCourses.length === 0) {
      return null;
    }

    return filteredCourses.reduce((earliest: Course, candidate) =>
      candidate.startDate < earliest.startDate ? candidate : earliest,
    );
  }, [filteredCourses]);

  const handleShowCourse = (course: Course) => {
    if (hideTimer.current) {
      window.clearTimeout(hideTimer.current);
      hideTimer.current = null;
    }

    setActiveCourse(course);
  };

  const handleHideCourse = (delay = 0) => {
    if (hideTimer.current) {
      window.clearTimeout(hideTimer.current);
    }

    hideTimer.current = window.setTimeout(() => {
      setActiveCourse(null);
      hideTimer.current = null;
    }, delay);
  };

  useEffect(() => {
    if (activeCourse && !visiblePrograms.has(activeCourse.program)) {
      setActiveCourse(null);
    }
  }, [activeCourse, visiblePrograms]);

  const toggleProgram = (program: string) => {
    setVisiblePrograms((prev) => {
      const next = new Set(prev);
      if (next.has(program)) {
        next.delete(program);
      } else {
        next.add(program);
      }
      return next;
    });
  };

  const resetFilters = () => {
    setVisiblePrograms(new Set(programDefinitions.map((item) => item.program)));
  };

  return (
    <div className="app-shell">
      <header className="hero-card">
        <img src={logoImage} alt="Logomarca do RAIO" className="hero-logo" />
        <div className="hero-content">
          <h1 className="page-title">Calendário Unificado de Cursos - 2026</h1>
          <p className="page-subtitle">
            Visão geral do cronograma de atividades dos programas CEPM/RAIO, CMB, CPM, CIR/RAIO e CTM/RAIO, destacando durações e sobreposições.
          </p>
        </div>
      </header>

      <section className="legend-card" aria-label="Legenda de programas">
        <h2 className="legend-title">Legenda</h2>
        {programDefinitions.map((item) => (
          <div key={item.program} className="legend-item">
            <span className="legend-dot" style={{ backgroundColor: item.color }} aria-hidden />
            <span>{item.label}</span>
          </div>
        ))}
      </section>

      <section className="toolbar" aria-label="Filtros e resumo">
        <div className="filters-toolbar">
          {programDefinitions.map((item) => {
            const isActive = visiblePrograms.has(item.program);
            const count = programStats.get(item.program) ?? 0;

            return (
              <button
                type="button"
                key={item.program}
                className={`filter-chip ${isActive ? 'is-active' : ''}`}
                onClick={() => toggleProgram(item.program)}
                style={{ '--chip-color': item.color } as CSSProperties}
                aria-pressed={isActive}
              >
                <span className="filter-dot" aria-hidden />
                {item.program}
                <span className="filter-count">{count}</span>
              </button>
            );
          })}
          <button type="button" className="filter-reset" onClick={resetFilters}>
            Mostrar todos
          </button>
        </div>

        <div className="stats-card">
          <div className="stats-grid">
            <div className="stats-item">
              <p className="stats-value">{filteredCourses.length}</p>
              <p className="stats-label">Cursos exibidos</p>
            </div>
            <div className="stats-item">
              <p className="stats-value">{totalDurationDays}</p>
              <p className="stats-label">Dias de formação somados</p>
            </div>
            <div className="stats-item">
              <p className="stats-value">
                {firstCourse ? formatDate(firstCourse.startDate) : '--'}
              </p>
              <p className="stats-label">Próximo início</p>
            </div>
          </div>
        </div>
      </section>

      <section className="calendar-card" aria-label="Calendário de cursos">
        <div className="month-headers">
          {months.map((month) => (
            <div key={month.label} className="month-header" style={{ width: `${month.width}%` }}>
              {month.label}
            </div>
          ))}
        </div>

        <div className="timeline-wrapper">
          <div className="timeline-grid" aria-hidden="true">
            {months.map((month) => (
              <div
                key={`grid-${month.label}`}
                className="timeline-grid-segment"
                style={{ width: `${month.width}%` }}
              >
                <span className="timeline-grid-label">{month.label}</span>
              </div>
            ))}
          </div>

          <div className="gantt-chart">
            {filteredCourses.length === 0 ? (
              <div className="empty-state">
                Nenhum curso corresponde aos filtros aplicados.
              </div>
            ) : (
              filteredCourses.map((course) => {
                const startOffset = course.startDate.getTime() - timelineStart.getTime();
                const duration = course.endDate.getTime() - course.startDate.getTime();
                const leftPercent = (startOffset / totalDurationMs) * 100;
                const widthPercent = (duration / totalDurationMs) * 100;
                const isActive = activeCourse?.name === course.name;

                return (
                  <div key={`${course.program}-${course.start}`} className={`course-row ${isActive ? 'is-active' : ''}`}>
                    <div className="course-name">{course.name}</div>
                    <div className="chart-area">
                      <button
                        type="button"
                        className={`gantt-bar ${isActive ? 'is-active' : ''}`}
                        style={{
                          backgroundColor: course.color,
                          left: `${leftPercent}%`,
                          width: `${widthPercent}%`,
                          color: course.textColor ?? '#f8fafc',
                        }}
                        onMouseEnter={() => handleShowCourse(course)}
                        onMouseLeave={() => handleHideCourse(120)}
                        onFocus={() => handleShowCourse(course)}
                        onBlur={() => handleHideCourse(0)}
                        onTouchStart={(event) => {
                          event.preventDefault();
                          handleShowCourse(course);
                          handleHideCourse(2500);
                        }}
                      >
                        {course.name}
                      </button>
                    </div>
                  </div>
                );
              })
            )}
          </div>
        </div>
      </section>

      <aside className={`info-bar ${activeCourse ? 'visible' : ''}`} aria-live="polite">
        {activeCourse ? (
          <>
            <p className="info-title">{activeCourse.name}</p>
            <p className="info-dates">
              Início: {formatDate(activeCourse.startDate)} — Término: {formatDate(activeCourse.endDate)}
            </p>
            <p className="info-program">
              Programa: {activeCourse.program} | Duração aproximada: {diffInDays(activeCourse.startDate, activeCourse.endDate)} dias
            </p>
          </>
        ) : (
          <>
            <p className="info-title">Passe o cursor sobre um curso</p>
            <p className="info-dates">Toque ou focalize um item para ver detalhes.</p>
            <p className="info-program">As datas exibem início, término e duração estimada.</p>
          </>
        )}
      </aside>
    </div>
  );
}

export default App;
