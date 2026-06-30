# JogoDaVelha-Python v1.0
# Created by: NkzDev-Cyber


# InvestCalc-Python V2
# Created by: NkzDev-Cyber

print("=" * 40)
print("📈 INVESTCALC-PYTHON V2 📈")
print("=" * 40)

print("1 - Português 🇧🇷")
print("2 - English 🇺🇸")

idioma = input("\nEscolha / Choose: ")


if idioma == "2":
    textos = {
        "nome": "What is your name? ",
        "inicial": "How much will you invest initially? R$ ",
        "aporte": "How much will you add per month? R$ ",
        "meses": "For how many months will you invest? ",
        "taxa": "What is the monthly return rate? (%) ",
        "resultado": "SIMULATION RESULT",
        "usuario": "User",
        "total": "Total invested",
        "final": "Final value",
        "rendimento": "Profit",
        "obrigado": "Thank you for using InvestCalc 🚀"
    }

else:
    textos = {
        "nome": "Qual o seu nome? ",
        "inicial": "Quanto você vai investir inicialmente? R$ ",
        "aporte": "Quanto você vai adicionar por mês? R$ ",
        "meses": "Por quantos meses vai investir? ",
        "taxa": "Qual a taxa mensal de rendimento? (%) ",
        "resultado": "RESULTADO DA SIMULAÇÃO",
        "usuario": "Usuário",
        "total": "Total investido",
        "final": "Valor final",
        "rendimento": "Rendimento",
        "obrigado": "Obrigado por usar a InvestCalc 🚀"
    }


nome = input(textos["nome"])

valor_inicial = float(input(textos["inicial"]))

aporte = float(input(textos["aporte"]))

meses = int(input(textos["meses"]))

taxa = float(input(textos["taxa"]))

taxa = taxa / 100


valor = valor_inicial


for i in range(meses):
    valor = valor * (1 + taxa)
    valor += aporte


total_investido = valor_inicial + (aporte * meses)

rendimento = valor - total_investido


print("\n" + "=" * 40)

print(textos["resultado"])

print("=" * 40)

print(f"{textos['usuario']}: {nome}")
print(f"{textos['total']}: R$ {total_investido:.2f}")
print(f"{textos['final']}: R$ {valor:.2f}")
print(f"{textos['rendimento']}: R$ {rendimento:.2f}")

print("=" * 40)

print(textos["obrigado"])
