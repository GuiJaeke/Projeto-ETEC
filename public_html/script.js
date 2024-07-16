// Seleciona o elemento com o id 'toggleMenu' e adiciona um evento de clique
document.getElementById('toggleMenu').addEventListener('click', function() {
    var menu = document.getElementById('menu'); // Obtém a referência ao elemento do menu pelo id 'menu'

    // Verifica se o estilo display atual do menu é 'none'
    if (menu.style.display == 'none') {        

        menu.style.display = 'grid'; // Se o menu estiver oculto ('none'), muda o estilo display para 'block' (visível)
    }
    else { // Caso contrário, se o menu estiver visível (qualquer coisa diferente de 'none'),

        menu.style.display = 'none'; // muda o estilo display para 'none' para ocultá-lo
    }
});