from Table import Table
from random import randint

class Player:
    __nome=''
    __trueTable= Table() #Tabela onde está os navios do Jogador.
    __displayedTable= Table() #Tabela mostrada ao jogador oposto
    
    #=== Símbolos utilizados ====#
    __navioSimbolo='N'
    __ErroSimbolo='X'
    __AcertoSimbolo='F'
    
    def __init__(self,nome:str,naviosQuantidade:int):
        self.__nome=nome
        self.__navioQuantidade=naviosQuantidade
    @nome.setter
    def nome(self,nome:str):
        self.nome=nome
        
        
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def trueTable(self) -> Table:
        return self.__trueTable
    
    @property
    def displayedTable(self) -> Table:
        return self.__displayedTable
    
    
    def __montarTableVerdadeira(self, randomize:bool = True, posicoes: list[list[int]] = None):
    
        if randomize:
            # Lógica para gerar aleatoriamente as posições dos navios
            self.__trueTable = Table(10, 10)  # Assumindo um tabuleiro de 10x10
            for navio in range(self.__navioQuantidade):
                while True:
                    col = randint(1, 10)
                    row = randint(1, 10)
                    if self.__trueTable.obterSimbolo(col, row) != 'N':
                        self.__trueTable.inserirSimbolo(col, row, 'N')
                        break
            
        else:
            self.__trueTable = Table(10, 10)  # Assumindo um tabuleiro de 10x10
            for posicao in posicoes:
                col, row = posicao
                self.__trueTable.inserirSimbolo(col, row, 'N')
                
    def montarTableMostrada(self):
        self.__displayedTable = Table(10, 10)  # Assumindo um tabuleiro de 10x10
        
        
    def marcarJogada(self, col:int, row:int)->bool:
        '''Se tiver acertado a posição de um navio, retorna True, e False caso contrário.
        Também altera a  TableMostrada
        '''
        simbolo = self.__ErroSimbolo
        Acertounavio= self.__trueTable.obterSimbolo(col, row) == 'N'        
        if Acertounavio:
            simbolo = self.__AcertoSimbolo

        self.__displayedTable.inserirSimbolo(col, row,simbolo)
        
        return Acertounavio