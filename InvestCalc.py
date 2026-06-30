# InvestCalc-Python v1.0
# Created by: NkzDev-Cyber

print ("=" * 40)
print ("📈 INVESTCALC-PYTHON 📈")
print ("Financial Investment Simulator")
print ("=" * 40)

nome = input ("qual o seu nome? ")
valor_inicial = float (input ("quanto você vai investir inicialmente? "))
aporte = float (input ("quanto você vai adicionar por mês? "))
meses = int (input ("por quantos meses vai investir? "))
taxa = float (input ("qual a taxa mensal de rendimentos? (%) "))
taxa = taxa / 100

valor = valor_inicial


for i in range (meses):
    valor = valor * (1 + taxa)
    valor += aporte
    
total_investido = valor_inicial + (aporte * meses)
rendimento = valor - total_investido


print("\n" + "=" * 40)
print ("RESULTADO DA SIMULAÇÃO")
print ("=" * 40)

print (f"usuário: {nome}")
print (f"Total investido: R$ {total_investido:.2f}")
print (f"Valor final: R$ {valor:.2f}")
print (f"Rendimento: R$ {rendimento:.2f}")

print ("=" * 40)
print ("Thanks for use the InvestCalc-Python🚀 ")
