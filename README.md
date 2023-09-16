# Batalha Naval Python
Este projeto busca ser a construção do clássico jogo de tabuleiro Batalha Naval usando a linguagem Python.

## O que é?
O jogo consiste em uma competição onde dois jogadores posicionam seus navios em suas próprias tabelas, em seguida, cada um tenta adivinhar em qual posição o adversário posicionou.

## Objetivo deste projeto
- Compreensão da linguagem Python;
- Aprimoramento da ideia de POO (Programação Orientada a Objetos);
- Modelagem de projetos;
- Construção de interface em linguagem Python;
- Construir um projeto apresentável. 
## Requisitos 

### Class
- The Player
- The Table
- The Game

### Player

O jogador possui os seguintes atributos:

| Atributo       | Tipo        | Descrição                                                   |
| -------------- | ----------- | ----------------------------------------------------------- |
| `name`           | `String`      | O nome do Jogador                                           |
| `displayedTable` | `Table`     | Tabela que deve ser mostrada ao jogador contrário, ele irá se basear nela para tomar as suas escolhas. |
| `trueTable`      | `Table `      | Tabela em que se encontram os navios do jogador             |

### Table

| Atributo       | Tipo        | Descrição                                                     |
| -------------- | ----------- | ------------------------------------------------------------- |
| `__cols`       | `int`     | Número de colunas na tabela.                                   |
| `__rows`       | `int`     | Número de linhas na tabela.                                    |
| `__table`      | `List[List [String] ]` | Uma Matriz que representa a tabela propriamente dita. Ela estára povoada por símbolos|

- O jogo deve ser jogador por apenas dois jogadores;
- A tabela pode possicionar os navios de forma aleatória ou possicionar de acordo com as posições desejadas por cada jogador    
- A tabela deve ser povoada por símbolos que possam representar: água, fogo e navio.
- Cada jogador escolhe uma linha e uma coluna da tabela do adversário;
- Caso o jogador acerte a posição de um navio, ele ganhará uma outra oportunidade de jogar;
