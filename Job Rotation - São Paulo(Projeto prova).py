# 2)
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib


def pertence_fibonacci(x):
    fib = fibonacci(x+1)
    if x in fib:
        return f"{x} pertence à sequência de Fibonacci."
    else:
        return f"{x} não pertence à sequência de Fibonacci."


numero = 21
mensagem = pertence_fibonacci(numero)
print(mensagem)

# 3)
import json

with open('faturamento.json', 'r') as f:
    dados = json.load(f)

menor_faturamento = float('inf')
maior_faturamento = float('-inf')

total_faturamento = 0
contagem_faturamento = 0


for valor in dados['faturamento_diario']:

    if valor != 0:

        if valor < menor_faturamento:
            menor_faturamento = valor
        if valor > maior_faturamento:
            maior_faturamento = valor


        total_faturamento += valor
        contagem_faturamento += 1


media_faturamento = total_faturamento / contagem_faturamento


dias_acima_media = 0
for valor in dados['faturamento_diario']:
    if valor > media_faturamento:
        dias_acima_media += 1

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")

# 4)
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento_mensal.values())

for estado, faturamento in faturamento_mensal.items():
    percentual = (faturamento / total) * 100
    print(f'{estado}: {percentual:.2f}%')


# 5)
string_original = "Exemplo de string original"  # Define a string original

string_invertida = ""  # Define a string invertida vazia

# Percorre a string original de trás para frente e adiciona cada caractere na string invertida
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

print("String original:", string_original)
print("String invertida:", string_invertida)
