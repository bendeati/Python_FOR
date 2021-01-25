# FOR-ciklus használata

lista = [1,3,5,7,9,12]
print(f"A lista elemszáma: {len(lista)}")
print(lista)
for elem in lista:
    print(elem)

#az i értéke 0-4-ig
print("Az i kiírása 0-4-ig:")
for i in range(5):
    print(i)

print("Az i kiírása 1-4-ig:")
for i in range(1,5):
    print(i)

print("Számok kiírása 1 től (nem)20-ig kettesével")
for i in range(1,20,2):
    print(i)

print("A lista elemei:")
print(lista)
for i in range(0,len(lista),3):
    print(lista[i])
