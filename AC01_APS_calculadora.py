from abc import ABC, abstractmethod


def main():
    pass


class Calculadora():
    def calcular(self, valor1, valor2, operador):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        resultado = operacao.executar(valor1, valor2)
        return resultado


class OperacaoFabrica():
    def criar(self, operador):
        if operador == "/":
            return Divisao()

        elif operador == "+":
            return Soma()

        elif operador == "-":
            return Subtracao()

        else:
            print("Operador inválido.")


class Operacao(ABC):
    @abstractmethod
    def executar(self, valor1, valor2):
        pass


class Divisao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 / valor2
        return resultado


class Soma(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 + valor2
        return resultado


class Subtracao(Operacao):
    def executar(self, valor1, valor2):
        resultado = valor1 - valor2
        return resultado


if __name__ == '__main__':
    a = main()
