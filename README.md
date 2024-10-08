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

### Classes
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
| `cols`       | `int`     | Número de colunas na tabela.                                   |
| `rows`       | `int`     | Número de linhas na tabela.                                    |
| `table`      | `List[List [String] ]` | Uma Matriz que representa a tabela propriamente dita. Ela estára povoada por símbolos|

## Requisitos 

- [X] O jogo deve ser jogador por apenas dois jogadores;

- [X] O jogador pode possicionar os navios na tabela de duas formas: ele próprio escolhendo, ou de forma aleatória;

- [X] A tabela deve ser povoada por símbolos que devem representar: água, fogo e navio;

- [ ] Cada jogador escolhe uma linha e uma coluna da tabela do adversário;

- [ ] Caso o jogador acerte a posição de um navio, ele ganhará uma outra oportunidade de jogar;

- [X] O jogador1 sempre iniciará a primeira partida.  
