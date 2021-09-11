#Hamowanie oboczne
def Output(inp):
    for x in range(1, len(inp) - 1):
        o = inp[x] - 0.5 * inp[x - 1] - 0.5 * inp[x + 1]
        o = round(o,2)
        print("Signal Number ", x, " Input  ", inp[x], " Output ", o, "\n")
        file.write(f"{x}\t{inp[x]}\t{o}\n")

#main
file_name = input("Podaj nazwe pliku do ktorego chcesz zapisac wyniki")
file = open(f"{file_name}.txt", "a")

inp = []
amount_of_signals = int(input("Podaj ile sygnalow chcesz wprowadzic\n"))


for i in range(0,amount_of_signals):
    i_x = float(input(f"Podaj wartość sygnału input({i}) "))

    inp.append(i_x)

Output(inp)
file.close()


