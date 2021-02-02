from sklearn import tree

#sklearn doesn't read strings

features = [[140,1],[130,1], [150,0],[170,0]]
#140 = peso en g
#1 = textura 1 = suave / 0 = aspero
#int = how much they weight, and string the texture

labels = [10, 10, -10, -10]
#it identifies what fruit is in each list

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
#classifier = box of rules

peso = int(input("Ingrese el peso de su fruta: "))

textura = input("Ingrese la textura de su fruta: ")
if textura == "aspera":
    textura = 0 #aspera
else:
    textura = 1 #suave

prediccion = clf.predict([[peso, textura]])

if prediccion == 10:
    print("Es una manzana")
else:
    print("es una Naranja")



#learning rule = procedure that learns the pattern
