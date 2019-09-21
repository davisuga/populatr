users=[]
populatr = open('populatr.sql', 'w+')

#nomes = map(lambda s: s.strip(), nomes)
def populateUsers():
    nomes = open('nomes.txt', 'r')
    nomes = nomes.readlines()
    print(nomes)    
    #print(nomes)
    for nome in nomes:
        line="insert into Usuario values(NULL,'{}','{}','{}','{}');\n".format(nome.strip(),nome.strip()[::-1],nome.strip()+'@gmail.com',nome.strip()+".png")
        populatr.write(line)

def populateIngredients():
    ingredients = open('ingredients.txt', 'r')
    ingredients = ingredients.readlines()
    print(ingredients)
    for ingredient in ingredients:
        line="insert into Ingredientes values(NULL,'{}');\n".format(ingredient.strip())
        populatr.write(line)
populateChoice = input("What do you what to populate?")
if populateChoice.lower() == "ingredients" or int(populateChoice)==1:
	populateIngredients()
elif populateChoice.lower() == "users" or int(populateChoice)==2:
	populateUsers()
populatr.close()
