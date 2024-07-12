f = open("test.txt", "r")
print(f.read())

f = open("test.txt", "a")
f.write("adicionando algo"+'\n')
f.close()