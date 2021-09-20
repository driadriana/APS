import unittest
from AC01_APS_calculadora import Calculadora


class MeusTestes(unittest.TestCase):
    def teste_divisao(self):
        calcula1 = Calculadora()
        testedivisao = calcula1.calcular(8, 4, '/')
        self.assertEqual(testedivisao, 2)
        print("8 / 4 = ", testedivisao)

    def teste_soma(self):
        testecalcula2 = Calculadora()
        testesoma = testecalcula2.calcular(2, 9, '+')
        self.assertEqual(testesoma, 11)
        print("2 + 9 = ", testesoma)

    def teste_subtracao(self):
        testecalcula3 = Calculadora()
        testesubtracao = testecalcula3.calcular(7, 2, '-')
        self.assertEqual(testesubtracao, 5)
        print("7 - 2 = ", testesubtracao)


if __name__ == '__main__':
    unittest.main()
