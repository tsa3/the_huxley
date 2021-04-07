class Carousel:

    def __init__(self, veh: [int]):
        self.vehicles = veh

    def extract_biggest_sequence(self, quant: int):
        biggest = 0
        sequence = []
        for i in range(0, quant):
            values = [self.vehicles[i]]
            for j in range(i+1, i+quant):
                if self.vehicles[j] > values[-1]:
                    values.append(self.vehicles[j])
            sequence.append(len(values))
        return max(sequence)


def get_values(ls: [int], s: str, l: int):
    for i in range(0, l):
        if "0" <= numbers[i] <= "9":
            if i < len(numbers) - 1:
                if numbers[i + 1] != " ":
                    s += numbers[i]
                else:
                    s += numbers[i]
                    lst.append(int(s))
                    s = ""
            else:
                s += numbers[i]
                lst.append(int(s))
                s = ""


# Variables and input
lst = []
q = int(input())
numbers = input()
st = ""
# Extract values to the list
get_values(lst, st, len(numbers))
# Circular array
circular = [None]*q*2
i = 0
while i < q:
    circular[i] = circular[i+q] = lst[i]
    i += 1
# Crete the object
carousel = Carousel(circular)
print(carousel.extract_biggest_sequence(q))
