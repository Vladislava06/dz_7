text = str(input()).split()
res = []
for i in range(len(text)):
    res.append(tuple(map(str, text[i].split('='))))
res = tuple(res)
print(res)

list = input().split()
result = tuple(map(lambda x: tuple(x.split('=')),list))
print(result)