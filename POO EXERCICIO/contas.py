from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do saldo precisa ser númerico')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depósito precisa ser númerico')
        
        self._saldo += valor
        self.detalhes()

    def detalhes(self, msg=''):
        print(f'Agência: {self._agencia}', end=' ')
        print(f'Conta: {self._conta}', end=' ')
        print(f'Saldo: {self._saldo:.2f} {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}'
        return f'{class_name}{attrs}'

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'SAQUE NEGADO {valor}')
        return self.saldo

class ContaCorrente(Conta):
    def __init__(
            self, agencia: int, conta: int, 
            saldo: float = 0, limite: float = 0
        ):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor}')
            return self.saldo
        
        print('Não foi possivel sacar o valor desejado')
        print(f'Seu limite é: {-self.limite:.2f}')
        self.detalhes(f'SAQUE NEGADO {valor}')
        return self.saldo


    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, '\
                f'{self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'

    # @property
    # def limite(self):
    #     return self.limite
    

if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
