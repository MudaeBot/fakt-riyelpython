
while True:
    guess=int(input("Bır sayı gir"))
    if guess<0:
        print("Lütfen pozitif tam sayı girin.")
        continue
    else:
        break
toplam=1
for i in range(1,guess+1):
    toplam*=i
print(f"{guess}! = :{toplam}")
