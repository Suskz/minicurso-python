"""
receber do usuario uma frase e imprimir quantas vogais e quantas consoantes essa frase possui

def contar_vogais_consoantes(s):
    # Definir as vogais
    vogais = "áaeiouAEIOU"
    
    # Inicializar contadores
    num_vogais = 0
    num_consoantes = 0
    
    # Iterar sobre cada caractere na string
    for char in s:
        # Verificar se o caractere é uma letra
        if char.isalpha():
            # Contar se é vogal ou consoante
            if char in vogais:
                num_vogais += 1
            else:
                num_consoantes += 1
    
    # Imprimir os resultados
    print(f"Vogais: {num_vogais}")
    print(f"Consoantes: {num_consoantes}")
 
# Exemplo de uso
contar_vogais_consoantes("Olá, mundo!5 45435")
"""

"""
façam uma função que receba uma data no formato dia/mes/ano e retorne a data no formato americano

# Divide a string da data em dia, mês e ano
    dia, mes, ano = data.split('/')
    
    # Retorna a data no formato americano
    return f'{ano}-{mes}-{dia}'
 
# Exemplo de uso
data_brasileira = "11/07/2024"
data_americana = converter_data(data_brasileira)
print(data_americana)  # Saída: 2024-07-11
"""
