<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calendário de Atividades - 2026</title>
    <!-- Carregamento do Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Configuração de fonte global e cores base */
        :root {
            --color-cepm: #1d4ed8; /* blue-700 - CEPM/RAIO */
            --color-cmb: #0d9488;  /* teal-600 - CMB (Motociclista Batedor) */
            --color-cpm: #4f46e5;  /* indigo-600 - CPM */
            --color-cir: #b91c1c;  /* red-700 - CIR/RAIO */
            --color-ctm: #db2777;  /* pink-600 - CTM/RAIO */
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f7f9fc;
        }
        .gantt-container {
            position: relative;
            padding: 1rem 0;
        }
        .gantt-bar {
            height: 1.75rem; /* h-7 */
            position: absolute;
            top: 0;
            cursor: pointer;
            transition: all 0.3s ease;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .gantt-bar:hover {
            opacity: 0.9;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.06);
            transform: scale(1.01);
        }
        /* Estilos específicos para a barra de informações */
        .info-bar {
            transition: opacity 0.3s ease-in-out;
        }
        /* Mobile: Ajusta o tamanho da fonte e margem */
        @media (max-width: 768px) {
            .month-header {
                font-size: 0.75rem; /* text-xs */
                padding: 0.25rem 0;
            }
            .course-name {
                font-size: 0.75rem;
                padding-left: 0.5rem;
            }
        }
    </style>
</head>
<body class="p-4 md:p-8">

    <div class="max-w-7xl mx-auto">
        <h1 class="text-3xl font-extrabold text-gray-900 mb-2 border-b border-blue-500 pb-2">Calendário Unificado de Cursos - 2026</h1>
        <p class="text-gray-600 mb-6">Visão geral do cronograma de atividades dos programas CEPM/RAIO, CMB, CPM, CIR/RAIO e CTM/RAIO, destacando durações e sobreposições.</p>

        <!-- Seção da Legenda -->
        <div class="flex flex-wrap gap-4 mb-8 p-4 bg-white shadow-lg rounded-lg">
            <h2 class="text-lg font-semibold text-gray-800 w-full mb-2">Legenda:</h2>
            <div class="flex items-center space-x-2">
                <div class="w-4 h-4 rounded-full bg-blue-700"></div>
                <span class="text-sm text-gray-700">CEPM/RAIO (Curso Esp. de Policiamento com Motocicletas)</span>
            </div>
            <div class="flex items-center space-x-2">
                <div class="w-4 h-4 rounded-full bg-teal-600"></div>
                <span class="text-sm text-gray-700">CMB (Curso de Motociclista Batedor)</span>
            </div>
            <div class="flex items-center space-x-2">
                <div class="w-4 h-4 rounded-full bg-indigo-600"></div>
                <span class="text-sm text-gray-700">CPM (Curso de Policiamento com Motocicletas)</span>
            </div>
            <div class="flex items-center space-x-2">
                <div class="w-4 h-4 rounded-full bg-red-700"></div>
                <span class="text-sm text-gray-700">CIR/RAIO (Curso de Intervenção Rápida)</span>
            </div>
            <div class="flex items-center space-x-2">
                <div class="w-4 h-4 rounded-full bg-pink-600"></div>
                <span class="text-sm text-gray-700">CTM/RAIO (Curso Tático Motorizado)</span>
            </div>
        </div>

        <!-- Container Principal do Calendário (Gráfico de Gantt) -->
        <div id="calendar-container" class="bg-white shadow-xl rounded-xl overflow-hidden">
            
            <!-- Cabeçalhos dos Meses -->
            <div id="month-headers" class="flex border-b border-gray-300 font-bold text-center text-gray-700 bg-gray-100">
                <!-- Conteúdo gerado via JS -->
            </div>

            <!-- Visualização dos Cursos e Linha do Tempo -->
            <div id="gantt-chart" class="grid grid-cols-1 divide-y divide-gray-200">
                <!-- Linhas dos Cursos (Geradas via JS) -->
            </div>

        </div>

        <!-- Barra de Informação Detalhada (Flutuante/Modal) -->
        <div id="info-bar" class="fixed bottom-0 left-0 right-0 bg-gray-800 text-white p-4 info-bar opacity-0 pointer-events-none rounded-t-xl shadow-2xl">
            <p class="font-bold text-lg" id="info-title"></p>
            <p class="text-sm" id="info-dates"></p>
            <p class="text-xs text-gray-400" id="info-program"></p>
        </div>

    </div>

    <script>
        // Dados dos cursos fornecidos pelo usuário
        const coursesData = [
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
            { program: 'CIR/RAIO', name: 'CIR/RAIO', start: '2026-09-28', end: '2026-11-01', color: 'var(--color-cir)' },
        ].map(course => ({
            ...course,
            startDate: new Date(course.start + 'T00:00:00'),
            endDate: new Date(course.end + 'T23:59:59'), // Inclui o dia de término
        }));

        const monthNames = ["Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov"];
        
        // Definição do período do calendário (Fevereiro 2026 a Novembro 2026)
        const timelineStart = new Date('2026-02-01T00:00:00');
        const timelineEnd = new Date('2026-12-01T00:00:00'); // Final de Novembro, começa Dezembro.
        const totalDurationMs = timelineEnd.getTime() - timelineStart.getTime();

        const ganttChart = document.getElementById('gantt-chart');
        const monthHeaders = document.getElementById('month-headers');
        const infoBar = document.getElementById('info-bar');
        const infoTitle = document.getElementById('info-title');
        const infoDates = document.getElementById('info-dates');
        const infoProgram = document.getElementById('info-program');

        // Função utilitária para calcular a diferença de dias
        const diffInDays = (date1, date2) => {
            const oneDay = 1000 * 60 * 60 * 24;
            const diffTime = Math.abs(date2.getTime() - date1.getTime());
            return Math.ceil(diffTime / oneDay);
        };

        // Função para formatar a data (DD/MM)
        const formatDate = (date) => {
            return `${String(date.getDate()).padStart(2, '0')}/${String(date.getMonth() + 1).padStart(2, '0')}`;
        };

        // 1. Geração dos Cabeçalhos dos Meses
        function renderMonthHeaders() {
            let currentMonth = new Date(timelineStart);
            monthHeaders.innerHTML = '';

            for (let i = 0; i < 10; i++) { // De Fev a Nov (10 meses)
                const nextMonth = new Date(currentMonth.getFullYear(), currentMonth.getMonth() + 1, 1);
                const monthDurationMs = nextMonth.getTime() - currentMonth.getTime();
                const widthPercent = (monthDurationMs / totalDurationMs) * 100;
                
                const headerDiv = document.createElement('div');
                headerDiv.className = 'month-header flex-1 p-2 text-xs md:text-sm transition-all duration-300';
                headerDiv.style.width = `${widthPercent}%`;
                headerDiv.textContent = monthNames[i] + '/26';

                monthHeaders.appendChild(headerDiv);
                currentMonth = nextMonth;
            }
        }

        // 2. Geração da Linha do Tempo (Gráfico de Gantt)
        function renderGanttChart() {
            ganttChart.innerHTML = '';
            
            coursesData.forEach(course => {
                // Cálculo de Posição e Largura
                const startOffsetMs = course.startDate.getTime() - timelineStart.getTime();
                const durationMs = course.endDate.getTime() - course.startDate.getTime();

                // Porcentagem de deslocamento a partir do início da timeline
                const leftPercent = (startOffsetMs / totalDurationMs) * 100;
                // Porcentagem de largura (duração)
                const widthPercent = (durationMs / totalDurationMs) * 100;

                // Linha do Curso
                const rowDiv = document.createElement('div');
                rowDiv.className = 'flex items-center min-h-[4rem] relative py-2 md:py-3';

                // Nome do Curso (Lado Esquerdo)
                const nameDiv = document.createElement('div');
                nameDiv.className = 'course-name w-1/4 md:w-48 text-sm md:text-base font-medium text-gray-800 shrink-0 pr-2 transition-all duration-300';
                nameDiv.textContent = course.name;

                // Área do Gráfico (Lado Direito)
                const chartArea = document.createElement('div');
                chartArea.className = 'flex-1 h-full relative';

                // Barra do Curso
                const barDiv = document.createElement('div');
                barDiv.className = 'gantt-bar rounded-md shadow-md text-white px-2 flex items-center justify-start text-xs font-semibold';
                barDiv.style.backgroundColor = course.color;
                barDiv.style.left = `${leftPercent}%`;
                barDiv.style.width = `${widthPercent}%`;
                barDiv.textContent = course.name; // Repete o nome na barra para melhor identificação visual

                // Adiciona eventos de mouse para a barra de informações
                barDiv.addEventListener('mouseenter', () => showInfo(course));
                barDiv.addEventListener('mouseleave', hideInfo);
                barDiv.addEventListener('touchstart', (e) => {
                    e.preventDefault();
                    showInfo(course);
                    setTimeout(hideInfo, 3000); // Esconde após 3 segundos no toque
                });
                
                chartArea.appendChild(barDiv);

                rowDiv.appendChild(nameDiv);
                rowDiv.appendChild(chartArea);
                ganttChart.appendChild(rowDiv);
            });
        }

        // 3. Funções da Barra de Informações Flutuante
        function showInfo(course) {
            infoTitle.textContent = course.name;
            infoDates.textContent = `Início: ${formatDate(course.startDate)} - Término: ${formatDate(course.endDate)}`;
            infoProgram.textContent = `Programa: ${course.program} | Duração Aprox.: ${diffInDays(course.startDate, course.endDate)} dias`;
            infoBar.classList.remove('opacity-0', 'pointer-events-none');
            infoBar.classList.add('opacity-100', 'pointer-events-auto');
        }

        function hideInfo() {
            infoBar.classList.remove('opacity-100', 'pointer-events-auto');
            infoBar.classList.add('opacity-0', 'pointer-events-none');
        }

        // Inicialização
        window.onload = function() {
            renderMonthHeaders();
            renderGanttChart();
        }

        // Adiciona um listener para lidar com a responsividade (re-renderização opcional em resize, mas o CSS já trata a maioria)
        window.addEventListener('resize', () => {
            // Re-renderizar o gráfico pode ser pesado, mas garante que os percentuais fiquem corretos se o layout mudar drasticamente.
            // Para simplicidade, o layout é majoritariamente tratado pelo flexbox e percentuais de largura do JS.
        });
    </script>
</body>
</html>
