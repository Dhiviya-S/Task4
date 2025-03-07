a=[5,6,7,8,9,22,5,77,8,6]
s=set()
duplicate=[]
for number in a:
    if number in s:
        duplicate.append(number)
    else:
        s.add(number)

print("Duplicates in the list are:",duplicate)
print("Set:",list(s))

non=[]
for num in s:
    if num not in duplicate:
        non.append(num)
    else:
        s.add(number)
print("First Non Repeating Element:",non[0])