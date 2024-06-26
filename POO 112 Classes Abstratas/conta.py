from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @abstractmethod
    def sacar(self, valor):
        pass

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do saldo precisa ser numérico')
        self._saldo = valor

    def detalhes(self, msg=''):
        print(f'Agência: {self._agencia}', end=' ')
        print(f'Conta: {self._conta}', end=' ')
        print(f'Saldo: {self._saldo:.2f} {msg}')

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depósito precisa ser numérico')

        self._saldo += valor
        self.detalhes()
        