age = 20
if age >= 18: status = 'adult'
else:
    status = 'minor'

age = 20
status = 'adult' if age >= 18 else 'minor'


x = 7
y = 5

print(x,y)
if x > y:
    temp = x
    x = y
    y = temp
print(x,y)

x,y = y,x
print(x,y)

#comprehension 1) iterable, filter (optional)

#flat

for i in range(10):
    print(i)

[print(i) for i in range(10)]    # flat comprehension no filter

for i in range(10):
    if i % 2 == 0: print(i)

[print(i) for i in range(10) if i % 2 == 0] # flat comprehension with filter


#flat comprehension multiple loops
for i in range(3):
    for j in range(4):
        print(str(i)+str(j))

[print(f'{i}{j}') for i in range(3) for j in range(4)]

[print(f'{i}{j}') for i in range(3) if i % 2 == 0 for j in range(4) if j % 2 == 1]

print()

# nested comprehension (a list of lists)
[[print(f'{i}{j}') for i in range(3) if i % 2 == 0] for j in range(4) if j % 2 == 1]    


rows = [[f"{i}{j} " for j in range(4)] for i in range(3)]
print(rows)

ml = ['a', 1, 'c']

s = ''.join(str(item) for item in ml)
print(s)
