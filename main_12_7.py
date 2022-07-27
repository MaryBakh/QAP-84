money=float(input("Планируемая сумма вклада:"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[]

for key, value in per_cent.items():
    x=money*value/100
    deposit.append(x)
	
print("Сумма, которую можно заработать за год:",deposit)
print("Максимальная сумма, которую можно заработать за год:",max(deposit))
