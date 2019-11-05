users=[]
populate_nome = open('populate_nomes.sql', 'w+')
populate_ingredientes = open('populate_ingredientes.sql', 'w+')

#nomes = map(lambda s: s.strip(), nomes)
def populateUsers():
    nomes = open('nomes.txt', 'r')
    nomes = nomes.readlines()
    print(nomes)    
    #print(nomes)
    for nome in nomes:
        line="insert into usuario values(NULL,'{}','{}','{}','{}');\n".format(nome.strip(),nome.strip()[::-1],nome.strip()+'@gmail.com',nome.strip()+".png")
        populate_nome.write(line)

def populateIngredients():
    ingredients = open('ingredients.txt', 'r')
    ingredients = ingredients.readlines()
    print(ingredients)
    for ingredient in ingredients:
        line="insert into ingredientes values(NULL,'{}');\n".format(ingredient.strip())
        populate_ingredientes.write(line)

    

def populateReceitas():
    ingredients = open('ingredients.txt', 'r')
    ingredients = ingredients.readlines()
    print(ingredients)
    for ingredient in ingredients:
        line="insert into ingredientes values(NULL,'{}');\n".format(ingredient.strip())
        populate_ingredientes.write(line)

        

quest = input('Vc quer: \n Popular ingredientes (a) \n Popular nomes (b)\n')


if quest == 'a':
    populateIngredients()
elif quest == 'b':
    populateUsers()
    
    

populate_ingredientes.close()
populate_nome.close()
