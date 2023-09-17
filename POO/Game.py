from Player import Player
from Table import Table

class Game:
    __round = 0 # contagem dos turnos da partida
    
    __gameOver = False # Caso um dos jogadores vença, muda para True
    
    
    def __init__(self, player1: Player, player2: Player):
        self.__player1 = player1
        self.__player2 = player2
        self.__jogador_atual = player1
        
    
    def checarVencedor(self, player: Player)->bool:
        """Checa se o jogador teve todos os navios atingidos pelo jogador Rival. Se for, o jogador Rival é o vencedor. """
        if player.shipQuanty==0:
            return True        

    def realizarJogada(self):
        if not self.__gameOver:
            pass

    
    
    def mostrarTabelaJogador(self, player: Player,TrueTableShow:bool=False):
        s=f"Tabela de {player.nome}\n"
        
        if TrueTableShow: 
            table = player.trueTable.table
        else:
            table = player.displayedTable.table
        
        for i in range(len(table)):
            for j in range(len(table[i])):
                s+= f' {table[i][j]:^5}' +"|"
    