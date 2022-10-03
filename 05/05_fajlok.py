try:
    file = open("be.txt", "r")
    sorok = file.readlines()
    for sor in sorok:
        print(sor.strip())
    file.close()
except FileNotFoundError as notfound:
    print(notfound)
except Exception as e:
    print(e)


count = 0
with open("be.txt", "r") as file:
    sorok = file.readlines()
    for sor in sorok:
        szavak = sor.split()
        count += len(szavak)

with open("ki.txt", "w") as file:
    file.write("Szavak szama: " + str(count))
