Objetivo do código:
O código é um jogo chamado "2048", seu objetivo é fazer com que qualquer um dos elementos da grade forme 2048.

Regras:
Você pode mover todos os números da grade juntos em uma qualquer direção disponível, vale lembrar que os número movidos na direção escolhida serão somados automaticamente caso eles sejam iguais.
Logo, você só pode somar os números caso eles sejam idênticos! (Exemplo:. 16 + 16 = 32)
Outra detalhe importante é que a cada jogada, houvendo uma soma ou não faz com que um número 4 ou 2 apareça em uma posição aleatória vazia da grade.

Spoiler!
O jogo é bem difícil, mas possível de chegar ao fim! ...Eu acredito... :)


Funcionamento Técnico Geral do código:
O jogo é responsivo ao usuário, isso significa que a dificuldade do jogo é totalmente dependente do usuário. Isso se deve ao fato de que o tamanho da grade é o medidor de dificuldade, 
então o usuário ao escolher o tamanho da grade ele também está escolhendo a dificuldade do jogo.

O jogo possui mecânica de salvamento, o único momento que o jogo é salvo é quando você instrui o código a salvar o momento atual do jogo.
O jogo também possui mecãnica de carregamento de jogos salvos anteriormente.

Caso você decida escolher a opção de sair, você consequentemente irá parar o funcionamento do código, então você terá que iniciar novamente para jogar.

Funcionamento Técnico Específico do código:
Grade:
O código utiliza listas para gerar as grades, a grade que o jogador vê é um mero recurso visual para facilitar a jogabilidade, como a grade é personalizável, ou seja, seu tamanho é escolhido pelo
usuário, portanto a forma que as operações númericas são realizadas envolvem uma lógica válida para uma grade n dimensional.

Salvamento e Carregamento:
O salvamento e carregamento utiliza um arquivo json chamado "Saves.json", dentro desse arquivo encontramos um dicionário chamado de "Saves" que contém cada "save". Cada save é um dicionário
por si só, cada dicionário contém o nome do save, o tamanho da grade do save e o momento atual do jogo (a lista que cria a grade). 

Outros:
Vale mencionar que existe uma função de remover um save escolhido, mas devido a problemas na lógica não implementei por completo essa funcionalidade, por hora para remover
um save você deve ir manualmento no arquivo json e apagar o save.

Outros P2:
O terminal não é apagado a cada jogada pois eu achei interessante o jogador poder visualizar suas jogadas anteriores, especialmente por conta da natureza única desse jogo que é
que os número são somados automaticamente, podendo causar momentos de confusão por conta da visibilidade reduzida do terminal do VSCode ou qualquer Compilador utilizado.

