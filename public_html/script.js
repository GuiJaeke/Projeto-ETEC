// Seleciona o elemento com o id 'toggleMenu' e adiciona um evento de clique
document.getElementById('toggleMenu').addEventListener('click', function() {
    // Obtém a referência ao elemento do menu pelo id 'menu'
    var menu = document.getElementById('menu');

    // Verifica se o estilo display atual do menu é 'none'
    if (menu.style.display == 'none') {
        // Se o menu estiver oculto ('none'), muda o estilo display para 'block' (visível)
        menu.style.display = 'block';
    } else {
        // Caso contrário, se o menu estiver visível (qualquer coisa diferente de 'none'),
        // muda o estilo display para 'none' para ocultá-lo
        menu.style.display = 'none';
    }
});