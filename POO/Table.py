class TableException(Exception):
    def __init__(self, code: int, message: str):
        '''
        1: coluna inválida
        2: linha inválida
        '''
        super().__init__(f'{code}: {message}')

class Table:
    # Símbolos da tabela
    __aguaSimbolo = '~'
    
    def __init__(self, cols: int, rows: int):
        self.__cols = cols
        self.__rows = rows
        self.__table = [[self.__aguaSimbolo for i in range(cols)] for i in range(rows)]
        
    def __str__(self) -> str:
        return self.mostrar()
    
    
    def mostrar(self) -> str:
        '''Retorna o status atual da tabela'''
        table_str = ''
        for row in self.__table:
            row_str = ' '.join(f'{cell};' for cell in row)
            table_str += f'{row_str}\n'
        return table_str

    def __validarPosicao(self, coluna: int, linha: int):
        '''Verifica se uma coluna ou linha é válida'''
        if not (1 <= coluna <= self.__cols):
            raise TableException(1, 'Coluna inválida: fora dos limites')

        if not (1 <= linha <= self.__rows):
            raise TableException(2, 'Linha inválida: fora dos limites')

    def inserirSimbolo(self, coluna: int, linha: int, simbolo: str):
        ''' 
        Insere um símbolo na tabela.
        Só é possível inserir o símbolo na tabela
        '''
        self.__validarPosicao(coluna, linha)
        
        self.__table[linha - 1][coluna - 1] = simbolo

    def obterSimbolo(self, coluna: int, linha: int)->str:
        ''' Obtém o símbolo de uma célula na tabela.'''
        self.__validarPosicao(coluna, linha)
        return self.__table[linha - 1][coluna - 1]
