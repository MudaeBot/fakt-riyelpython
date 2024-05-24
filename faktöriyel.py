
while True:
    guess=int(input("What's your num?"))
    if guess<0:
        print("It must be an ınteger")
        continue
    else:
        break
total=1
for i in range(1,guess+1):
    total*=i
print(f"{guess}! = :{total}")
