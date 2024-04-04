# 1 - bibliotecas, framework e referências externas
import pytest # framework de teste de unidade

# funções que serão testadas
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

from utils.utils import ler_csv # função de leitura de arquivos csv

# 2 - Testes

def test_somar_dois_numeros():

    # Padrão / Standard AAA (se diz Tiple A / 3A) = Arrange, Act, Assert
    
    # Prepara (fornecer dados) / Configura
    # Dados entrada e saída
    num1 = 5
    num2 = 7
    resultado_esperado = 12

    # Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():

    # Padrão / Standard AAA (se diz Tiple A / 3A) = Arrange, Act, Assert
    
    # Prepara (fornecer dados) / Configura
    # Dados entrada e saída
    num1 = 7
    num2 = 5
    resultado_esperado = 2

    # Act / Executa
    resultado_obtido = subtrair_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_multiplicar_dois_numeros():

    # Padrão / Standard AAA (se diz Tiple A / 3A) = Arrange, Act, Assert
    
    # Prepara (fornecer dados) / Configura
    # Dados entrada e saída
    num1 = 7
    num2 = 5
    resultado_esperado = 35

    # Act / Executa
    resultado_obtido = multiplicar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros():

    # Padrão / Standard AAA (se diz Tiple A / 3A) = Arrange, Act, Assert
    
    # Prepara (fornecer dados) / Configura
    # Dados entrada e saída
    num1 = 10
    num2 = 5
    resultado_esperado = 2

    # Act / Executa
    resultado_obtido = dividir_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

def test_dividir_por_zero():

    # Padrão / Standard AAA (se diz Tiple A / 3A) = Arrange, Act, Assert
    
    # Prepara (fornecer dados) / Configura
    # Dados entrada e saída
    num1 = 64
    num2 = 0
    resultado_esperado = 'Não é possível dividir por zero'

    # Act / Executa
    resultado_obtido = dividir_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

# Test Baseados em Dados = Data Driven Tests (DTT) --> Massa de Teste
    # Dados em uma lista
    # Dados em um arquivo, vários formatos, mais comun: csv (texto separado por vírgulas), json, xlm, dat

@pytest.mark.parametrize('num1, num2, resultado_esperado',
                         [ # array / matriz
                             (5, 7, 12), # tupla / registro
                             (0, 8, 8),
                             (10, -15, -5),
                             (6, 0.75, 6.75)                             
                         ]
                         )


def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):

    # Padrão / Standard AAA (se diz Tiple A / 3A) = Arrange, Act, Assert
    
    # Prepara (fornecer dados) / Configura
    # Dados entrada e saída fornecidos pela massa de teste em formato de lista

    # Act / Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Assert / Valida
    assert resultado_esperado == resultado_obtido

@pytest.mark.parametrize('num1, num2, resultado_esperado',
                           ler_csv('./fixtures/massa_somar.csv')
                         )

def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):

    # Padrão / Standard AAA (se diz Tiple A / 3A) = Arrange, Act, Assert
    
    # Prepara (fornecer dados) / Configura
    # Dados entrada e saída fornecidos pela massa de teste em formato de lista

    # Act / Executa
    resultado_obtido = somar_dois_numeros(float(num1), float(num2))

    # Assert / Valida
    assert float(resultado_esperado) == resultado_obtido