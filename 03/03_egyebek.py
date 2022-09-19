# tuple: elem n-es (immutable)
demo_tuple = ("alma", "körte", "barack")
print(type(demo_tuple))
print(demo_tuple)

print(demo_tuple[-1])
print(len(demo_tuple))
# demo_tuple[0] = "eper"    # ezt nem szabad!
# indexelés, függvények mint a listáknál, kivéve az értékadás, hozzáfűzés

print("--------------")
# set
demo_set = {"alma", "körte", "barack", "alma"}      # nem lehet ismétlődés
print(type(demo_set))
print(demo_set)

demo_set.add("eper")
print(demo_set)

demo_set.remove("barack")
print(demo_set)

# print(demo_set[0])      # nincs sorrendiség -> indexek se
