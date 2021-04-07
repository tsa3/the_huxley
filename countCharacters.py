class Characters:
    def __init__(self, t: str):
        self.text = t

    def extract_informations(self):
        a = blackspaces = 0
        freq = []
        pair = []
        for i in range(0, len(self.text)):
            if self.text[i] == " ":
                blackspaces += 1
            if self.text[i] == "a":
                a += 1
            if i+1 < len(self.text):
                if "a" <= self.text[i] <= "z" and "a" <= self.text[i + 1] <= "z":
                    dec = True
                    sub = self.text[i]+self.text[i+1]
                    for j in pair:
                        if sub == j:
                            dec = False
                            freq[pair.index(sub)] += 1
                    if dec:
                        pair.append(sub)
                        freq.append(1)

        print(blackspaces)
        print(a)
        if len(pair) == 0:
            print("NENHUM PAR")
        else:
            pos = 0
            for i in range(0, len(freq)):
                if freq[i] == max(freq):
                    pos = i
                    break
            print(max(freq))
            print(pair[pos])


while True:
    st = input()
    s = st.lower()
    if st != "NAO QUERO MAIS":
        txt = Characters(s)
        txt.extract_informations()
    else:
        break
