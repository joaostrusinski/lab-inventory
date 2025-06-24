// scripts.js (versão 3 - com validação numérica)

document.addEventListener('DOMContentLoaded', function() {

    // --- SEÇÃO DE FILTRO ---
    const filterInput = document.getElementById('filtro');
    const filterButton = document.getElementById('btn-filtrar');

    function filtrarTabela() {
        const tableRows = document.querySelectorAll('table tbody tr');
        const termoBusca = filterInput.value.toLowerCase();

        tableRows.forEach(function(linha) {
            const textoLinha = linha.textContent.toLowerCase();
            if (textoLinha.includes(termoBusca)) {
                linha.style.display = '';
            } else {
                linha.style.display = 'none';
            }
        });
    }

    filterButton.addEventListener('click', filtrarTabela);
    filterInput.addEventListener('keyup', filtrarTabela);


    // --- SEÇÃO DE CADASTRO ---
    const form = document.querySelector('.form-cadastro');
    const tableBody = document.querySelector('table tbody');

    form.addEventListener('submit', function(evento) {
        evento.preventDefault();
        const inputs = form.querySelectorAll('input');
        const novaLinha = document.createElement('tr');

        inputs.forEach(function(input) {
            const novaCelula = document.createElement('td');
            novaCelula.textContent = input.value;
            novaLinha.appendChild(novaCelula);
        });

        tableBody.appendChild(novaLinha);
        form.reset();
    });


    // --- NOVA SEÇÃO DE VALIDAÇÃO NUMÉRICA ---
    // Seleciona todos os inputs que marcamos com a classe 'numeric-only'
    const numericInputs = document.querySelectorAll('.numeric-only');

    // Para cada um desses inputs, adiciona um "ouvinte"
    numericInputs.forEach(function(input) {
        // O evento 'input' é disparado toda vez que o valor do campo muda (digitação, colar, etc.)
        input.addEventListener('input', function(evento) {
            // Pega o valor atual do campo e usa uma expressão regular para remover
            // qualquer coisa que NÃO seja um número (\D).
            // O 'g' no final garante que ele remova todas as ocorrências, não apenas a primeira.
            evento.target.value = evento.target.value.replace(/\D/g, '');
        });
    });

});