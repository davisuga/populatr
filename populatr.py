users=[]
nomes = open('nomes.txt', 'r')
nomes = nomes.readlines()
print(nomes)
#nomes = map(lambda s: s.strip(), nomes)

#print(nomes)
populatr = open('populatr.sql', 'w+')
for nome in nomes:
    line="insert into usuario values(NULL,'{}','{}','{}','{}');\n".format(nome.strip(),nome.strip()[::-1],nome.strip()+'@gmail.com',nome.strip()+".png")
    populatr.write(line)
populatr.close()