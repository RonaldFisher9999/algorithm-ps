x = set(['aa', 'bb', 'cc'])
f = open("test.txt", "w")
for xi in x :
    f.write(f"{xi} ")
f.close()