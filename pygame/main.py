import pygbag
import pygame
import sys
import asyncio

pygame.init()
larguraTela, alturaTela = 1200, 700

janelaDoJogo = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('My pygame')
relogio = pygame.time.Clock()
async def main():
    preto = (0, 0, 0)
    #background do jogo
    bgApple = janelaDoJogo.fill(preto)
    
    bg = janelaDoJogo.fill(preto)
    

    #contador
    fonte = pygame.font.Font(None, 74)
    fonte = pygame.font.SysFont('algerian', 80, False, False)
    fonteInicial = pygame.font.SysFont('arial', 50, True, False)

    #Cores RGB
    preto = (0, 0, 0)
    branco = (255, 255, 255)
    ciano = (63,166,255)
    azul = (34, 85, 229)
    rosa = (255, 51, 255)

    #parâmetro da raquete 1 
    xRaquete = 10
    yRaquete = 300
    larguraRaquete = 10
    alturaRaquete = 110

    #parâmetro da raquete 2 
    xRaquete2 = 1180
    yRaquete2 = 300
    larguraRaquete2 = 10
    alturaRaquete2 = 110
    velocidadeRaquete2 = 0

    #parâmetro da bolinha
    xBolinha = 600
    yBolinha = 350
    diametroBolinha = 17
    velocidadeXBolinha = 5
    velocidadeYBolinha = 5
    velocidadeInicial = 500

    #pontuação inicial
    pontosAPPLE = 0
    pontosIBM = 0

    #mensagens do jogo
    mensagemInicio = f'Aperte ESPAÇO para'
    mensagemInicio2 = f'iniciar o jogo'

    vitoriaApple = f'Play 1 VENCEU'

    vitoriaIBM = f'play 2 VENCEU'

    #Loops das telas
    fimDeJogo = False
    rodando = True
    telaInicial = False

    #Loop da tela inicial
    while not telaInicial:
        
        fomatacaoInical = fonteInicial.render(mensagemInicio, True, (branco))
        janelaDoJogo.blit(fomatacaoInical, (350,250))

        fomatacaoInical = fonteInicial.render(mensagemInicio2, True, (branco))
        janelaDoJogo.blit(fomatacaoInical, (425,350))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    telaInicial = True
                    contador = 5
                    texto = fonte.render(str(contador), True, (ciano))
    #Loop para a contagem regressiva
                    executando = True
                    while executando:
                        janelaDoJogo.fill(preto)
                        for evento in pygame.event.get():
                            if evento.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

    #Preparação para o jogo
                        bolinha = pygame.draw.circle(janelaDoJogo, (branco), (xBolinha, yBolinha), diametroBolinha)
                        raquete1 = pygame.draw.rect(janelaDoJogo, (rosa), (xRaquete, yRaquete, larguraRaquete, alturaRaquete))
                        raquete2 = pygame.draw.rect(janelaDoJogo, (azul), (xRaquete2, yRaquete2, larguraRaquete2, alturaRaquete2))

                        janelaDoJogo.blit(texto, (575, 310))
                        pygame.time.delay(1000)
    #Atualiza o contador e o texto
                        contador -= 1
                        texto = fonte.render(str(contador), True, (ciano))
                        pygame.display.flip()
                        if contador == 0:
                            executando = False
        
    #Janela principal
    while rodando:
        janelaDoJogo.fill(preto)
        relogio.tick(velocidadeInicial)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

    #bolinha do jogo
        bolinha = pygame.draw.circle(janelaDoJogo, (branco), (xBolinha, yBolinha), diametroBolinha)
        xBolinha += velocidadeXBolinha
        if xBolinha > larguraTela - diametroBolinha or xBolinha < 0 + diametroBolinha:
            velocidadeXBolinha *= -1
        if yBolinha < 0 + 17 or yBolinha > alturaTela - 17:
            velocidadeYBolinha *= -1

        yBolinha += velocidadeYBolinha
        if yBolinha > alturaTela or yBolinha < 0:
            velocidadeYBolinha *= -1

    #criando raquete
        raquete1 = pygame.draw.rect(janelaDoJogo, (rosa), (xRaquete, yRaquete, larguraRaquete, alturaRaquete))
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_s] and yRaquete <585:
            yRaquete += 10
        if tecla[pygame.K_w] and yRaquete >5:
            yRaquete -= 10
        if raquete1.colliderect(bolinha):
            velocidadeXBolinha = +5
            velocidadeYBolinha *= 1

    #raquete oponente
        raquete2 = pygame.draw.rect(janelaDoJogo, (azul), (xRaquete2, yRaquete2, larguraRaquete2, alturaRaquete2))
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_DOWN] and yRaquete2 <585:
            yRaquete2 += 10
        if tecla[pygame.K_UP] and yRaquete2 >5:
            yRaquete2 -= 10
        if raquete2.colliderect(bolinha):
            velocidadeXBolinha = -5
            velocidadeYBolinha *= 1

    #Pontos dos jogadores
        mensagem1 = f'{pontosAPPLE}'
        mensagem2 = f'{pontosIBM}'
        textoFormatado1 = fonte.render(mensagem1, True, (255, 255, 255))
        textoFormatado2 = fonte.render(mensagem2, True, (255, 255, 255))
        if xBolinha > larguraTela - diametroBolinha:
            pontosAPPLE += 1

        if xBolinha < 0 + diametroBolinha:
            pontosIBM += 1

    #fim de jogo Apple
        if pontosAPPLE == 10:
            rodando = False
            fimDeJogo = True
            while fimDeJogo:
                janelaDoJogo.blit(bgApple, (0, 0))
                relogio.tick()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        fimDeJogo = False
                recomece = pygame.key.get_pressed()
                if recomece[pygame.K_r]:
                    fimDeJogo = False
                await asyncio.sleep(0)
                vitoriaFormatacao = fonteInicial.render(vitoriaApple, True, (branco))
                janelaDoJogo.blit(vitoriaFormatacao, (410,100))
                pygame.display.flip()
            pygame.quit()

    #Fim de jogo IBM
        elif pontosIBM == 10:
            rodando = False
            fimDeJogo = True
            while fimDeJogo:
                janelaDoJogo.blit(bgApple, (0, 0))
                relogio.tick()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        fimDeJogo = False
                recomece = pygame.key.get_pressed()
                if recomece[pygame.K_r]:
                    fimDeJogo = False
                await asyncio.sleep(0)
                vitoriaFormatacao2 = fonteInicial.render(vitoriaIBM, True, (branco))
                janelaDoJogo.blit(vitoriaFormatacao2, (410,100))

                pygame.display.flip()
            pygame.quit()
        await asyncio.sleep(0)
        janelaDoJogo.blit(textoFormatado1, (270, 0))
        janelaDoJogo.blit(textoFormatado2, (890, 0))
        pygame.display.flip()
    pygame.quit()
asyncio.run(main())