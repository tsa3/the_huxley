class Loteria:
    def __init__(self, n: []):
        self.numbers = n

    def number_hits(self, n: [int]):
        quant = 0
        for i in n:
            for j in self.numbers:
                if i == j:
                    quant += 1
                    break
        return quant


dic = {}
while True:
    st = str(input())
    if st == "FIM":
        break
    else:
        name = ""
        num = False
        numbers = []
        nb = ""
        for i in range(0, len(st)):
            if num == False and st[i] != " ":
                name += st[i]
            elif st[i] == " " and num == False:
                num = True
            elif num and st[i] != " ":
                nb += st[i]
            elif st[i] == " ":
                try:
                    numbers.append(int(nb))
                    nb = ""
                except:
                    continue
        numbers.append(int(nb))
        dic[name] = numbers

valuess = []
v = str(input())
vt = ""
for i in v:
    if i == "-":
        valuess.append(int(vt))
        vt = ""
    else:
        vt += i
valuess.append(int(vt))
select = Loteria(valuess)

tp = []
for key, value in dic.items():
    tp.append([key, select.number_hits(value)])

tp.sort(key=lambda x: x[1])

init = False
txt = []
now = 0
for i in tp:
    if init == False:
        init = True
        now = i[1]
        txt.append(i[0])
    else:
        if i[1] == now:
            txt.append(i[0])
        else:
            txt.sort()
            for a in txt:
                print(f'{a} {now*"+"}')
            txt = []
            txt.append(i[0])
            now = i[1]
txt.sort()
for a in txt:
    print(f'{a} {now*"+"}')
