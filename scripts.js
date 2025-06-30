// scripts.js (versão 4 - com funcionalidade de apagar)

document.addEventListener('DOMContentLoaded', function() {

    // --- SEÇÕES DE ELEMENTOS GLOBAIS ---
    const filterInput = document.getElementById('filtro');
    const form = document.querySelector('.form-cadastro');
    const tableBody = document.querySelector('table tbody');

    // --- SEÇÃO DE FILTRO ---
    function filtrarTabela() {
        const tableRows = document.querySelectorAll('table tbody tr');
        const termoBusca = filterInput.value.toLowerCase();
        tableRows.forEach(linha => {
            const textoLinha = linha.textContent.toLowerCase();
            linha.style.display = textoLinha.includes(termoBusca) ? '' : 'none';
        });
    }
    filterInput.addEventListener('keyup', filtrarTabela);

    // --- SEÇÃO DE CADASTRO ---
    form.addEventListener('submit', function(evento) {
        evento.preventDefault();
        const inputs = form.querySelectorAll('input');
        const novaLinha = document.createElement('tr');
        
        inputs.forEach(input => {
            const novaCelula = document.createElement('td');
            novaCelula.textContent = input.value;
            novaLinha.appendChild(novaCelula);
        });

        // Adiciona a célula com o botão de apagar na nova linha
        const celulaAcoes = document.createElement('td');
        celulaAcoes.innerHTML = '<button class="btn-apagar">Apagar</button>';
        novaLinha.appendChild(celulaAcoes);
        
        tableBody.appendChild(novaLinha);
        form.reset();
    });

    // --- SEÇÃO PARA APAGAR LINHA (Delegação de Eventos) ---
    // Adicionamos um único "ouvinte" ao corpo da tabela.
    // Ele vai monitorar todos os cliques que acontecerem dentro dele.
    tableBody.addEventListener('click', function(evento) {
        // Verificamos se o alvo do clique (evento.target) foi um botão com a classe 'btn-apagar'
        if (evento.target.classList.contains('btn-apagar')) {
            // Se foi, encontramos a linha (tr) mais próxima do botão que foi clicado
            const linhaParaApagar = evento.target.closest('tr');
            // E removemos essa linha da tabela
            linhaParaApagar.remove();
        }
    });

    // --- SEÇÃO DE VALIDAÇÃO NUMÉRICA ---
    const numericInputs = document.querySelectorAll('.numeric-only');
    numericInputs.forEach(input => {
        input.addEventListener('input', function(evento) {
            evento.target.value = evento.target.value.replace(/\D/g, '');
        });
    });
});