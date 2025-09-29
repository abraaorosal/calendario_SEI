import { Course } from '../types';

type RawCourse = Omit<Course, 'startDate' | 'endDate'>;

const rawCourses: RawCourse[] = [
  // CEPM/RAIO (Curso Especial de Policiamento com Motocicletas) - 6 semanas
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 1', start: '2026-02-23', end: '2026-04-05', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 2', start: '2026-03-10', end: '2026-04-20', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 3', start: '2026-03-25', end: '2026-05-05', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 4', start: '2026-04-09', end: '2026-05-20', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 5', start: '2026-04-24', end: '2026-06-04', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 6', start: '2026-05-09', end: '2026-06-19', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 7', start: '2026-05-24', end: '2026-07-04', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 8', start: '2026-06-08', end: '2026-07-19', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 9', start: '2026-06-23', end: '2026-08-03', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 10', start: '2026-07-08', end: '2026-08-18', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 11', start: '2026-07-23', end: '2026-09-02', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 12', start: '2026-08-07', end: '2026-09-17', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 13', start: '2026-08-22', end: '2026-10-02', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 14', start: '2026-09-06', end: '2026-10-17', color: 'var(--color-cepm)' },
  { program: 'CEPM/RAIO', name: 'CEPM/RAIO Curso 15', start: '2026-09-21', end: '2026-11-01', color: 'var(--color-cepm)' },

  // CMB (Curso de Motociclista Batedor) - Módulos de 1 mês
  { program: 'CMB', name: 'CMB Módulo 1', start: '2026-03-15', end: '2026-04-15', color: 'var(--color-cmb)' },
  { program: 'CMB', name: 'CMB Módulo 2', start: '2026-05-10', end: '2026-06-10', color: 'var(--color-cmb)' },
  { program: 'CMB', name: 'CMB Módulo 3', start: '2026-07-06', end: '2026-08-07', color: 'var(--color-cmb)' },
  { program: 'CMB', name: 'CMB Módulo 4', start: '2026-10-05', end: '2026-11-05', color: 'var(--color-cmb)' },

  // CPM (Curso de Policiamento com Motocicletas)
  { program: 'CPM', name: 'CPM (Curso Policiamento Motocicletas)', start: '2026-08-10', end: '2026-09-11', color: 'var(--color-cpm)' },

  // NOVOS CURSOS (5 SEMANAS CADA)
  // CTM/RAIO (Curso Tático Motorizado) - 5 semanas, 1º Semestre
  { program: 'CTM/RAIO', name: 'CTM/RAIO', start: '2026-04-27', end: '2026-05-31', color: 'var(--color-ctm)' },
  // CIR/RAIO (Curso de Intervenção Rápida) - 5 semanas, 2º Semestre
  { program: 'CIR/RAIO', name: 'CIR/RAIO', start: '2026-09-28', end: '2026-11-01', color: 'var(--color-cir)', textColor: '#0a122d' },
];

export const courses: Course[] = rawCourses.map((course) => ({
  ...course,
  startDate: new Date(`${course.start}T00:00:00`),
  endDate: new Date(`${course.end}T23:59:59`),
}));
