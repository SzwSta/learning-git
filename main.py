numbers=[]
for i in range(1,101):
    if i%5==0:
        numbers.append(i)
cubes=[number**3 for number in numbers]
print(f"Zadanie 2 - poczatek\npoczatkowa lista: {numbers}\nlista szescianow: {cubes}\nZadanie 2 - koniec\n")
print("test2")
