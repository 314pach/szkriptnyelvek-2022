def osztas(a, b):
    if b == 0:
        raise ZeroDivisionError("Ejnye-bejnye")
    else:
        return a/b


print(osztas(15, 3))
print(osztas(3, 0))


def fgv():
    ls = ["ajjajj", "mi", "lesz", "ebbol"]
    for i in range(10):
        print(ls[i])


try:
    fgv()
except IndexError as ie:
    print(ie)
except Exception as e:
    print("Valami egyéb kivétel:", e)
