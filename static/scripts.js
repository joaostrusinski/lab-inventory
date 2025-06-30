// scripts.js (versão final, unificada e corrigida)

// Inicia um único "ouvinte" que espera a página inteira carregar.
document.addEventListener('DOMContentLoaded', function() {

    // --- LÓGICA DO FILTRO ---
    // Colocamos a lógica do filtro aqui dentro.
    const filterInput = document.getElementById('filtro');
    function filtrarTabela() {
        const tableRows = document.querySelectorAll('table tbody tr');
        const termoBusca = filterInput.value.toLowerCase();
        tableRows.forEach(function(linha) {
            const textoLinha = linha.textContent.toLowerCase();
            linha.style.display = textoLinha.includes(termoBusca) ? '' : 'none';
        });
    }
    filterInput.addEventListener('keyup', filtrarTabela);

    // --- LÓGICA DA VALIDAÇÃO NUMÉRICA ---
    // Colocamos a lógica da validação numérica aqui dentro.
    const numericInputs = document.querySelectorAll('.numeric-only');
    numericInputs.forEach(function(input) {
        input.addEventListener('input', function(evento) {
            evento.target.value = evento.target.value.replace(/\D/g, '');
        });
    });

    // --- LÓGICA DE CONFIRMAÇÃO AO APAGAR ---
    // Colocamos a lógica de confirmação aqui dentro.
    const deleteForms = document.querySelectorAll('.form-apagar');
    deleteForms.forEach(function(form) {
        form.addEventListener('submit', function(evento) {
            const confirmacao = confirm('Tem certeza que deseja apagar este equipamento? Esta ação não pode ser desfeita.');
            if (!confirmacao) {
                evento.preventDefault();
            }
        });
    });

}); // Fim do único "ouvinte" principal
