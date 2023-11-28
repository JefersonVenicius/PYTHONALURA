# Estruturas de repetição
# WHILE
gastos=0
valor_gasto=0
while gastos < 1000:
    valor_gasto = int(input("Digite o valor gasto"))
    gastos = gastos + valor_gasto
print(gastos)

# Digite o valor do novo gasto 20
# Digite o valor do novo gasto 500
# Digite o valor do novo gasto 480
# Resultado: 1000

# FOR - Utilizamos o for quando queremos iterar sobre um bloco de código por um determinado número de vezes
for i in range(1,10):
    print(i)