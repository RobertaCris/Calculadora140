# 1 - bibliotecas, framework e referências externas
import pytest # framework de teste de unidade

# funções que serão testadas
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

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

