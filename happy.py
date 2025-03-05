a = [100, 501, 22, 37, 10, 999, 87, 351]
sum = 0
happy = []
count = 0
for number in a:
    num = number
    while (num > 0):
        n = num % 10
        sum = sum + (n * n)
        num = num // 10
    num = sum
    if (num == 1):
        happy.append(number)
    else:
        print()
count = count + 1
print("Happy numbers count:", count)
print("Happy numbers are:", happy)
