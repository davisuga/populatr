users=[]
populatr = open('populatr.sql', 'w+')

#nomes = map(lambda s: s.strip(), nomes)
def populateUsers():
    nomes = open('nomes.txt', 'r')
    nomes = nomes.readlines()
    print(nomes)    
    #print(nomes)
    for nome in nomes:
        line="insert into usuario values(NULL,'{}','{}','{}','{}');\n".format(nome.strip(),nome.strip()[::-1],nome.strip()+'@gmail.com',nome.strip()+".png")
        populatr.write(line)

def populateIngredients():
    ingredients = open('ingredients.txt', 'r')
    ingredients = ingredients.readlines()
    print(ingredients)
    for ingredient in ingredients:
        line="insert into usuario values(NULL,'{}');\n".format(ingredient.strip())
        populatr.write(line)

populatr.close()
