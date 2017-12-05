with open('D:\\workspace\\Toothless-Forth\\data\\tmp\\industries.txt', 'r',encoding="utf8") as f:
    lines = list(f.readlines())
    ids = []
    for line in lines:
        ids.append(line[:line.find('	')])

print(ids)
