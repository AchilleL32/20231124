#import des packages 
import pandas as pd
import numpy as np 
from math import sin

# Ceci est un commentaire 

x = 5
a = 1 
b = 2
# Boucle if 

if x >= 10:
    pass  # Ne fait rien et passe à la suite
else:
    print("x est inférieur ou égal à 10")
    
# Boucle While 

while x < 10:
    x += 1
    if x % 2 == 0:
        continue  # Saute les nombres pairs
    print(x)
    
# Boucle for 

for letter in 'Python':
    if letter == 'h':
        continue  # Saute 'h' et continue la boucle
    if letter == 'o':
        pass  # Ne fait rien pour 'o' mais continue l'exécution
        
    print('Lettre actuelle :', letter)

for num in range(1, 11):  # Itère de 1 à 10
    if num == 5:
        pass  # Ne fait rien pour le nombre 5
    elif num % 2 == 0:
        continue  # Saute les nombres pairs
    print(num)


# Boucle try 
try:
    resultat = a / b
except ZeroDivisionError:
    resultat = "Erreur : Division par zéro."

def function_name(argument1 , argument2 = 48): 
    
    argument_total = argument1 * argument2 
    
    return argument_total

x = function_name(1,2)
y = function_name(1)

## Utilisation de pandas 

# Lecture d'un fichier CSV
#df = pd.read_csv('chemin/vers/votre/fichier.csv')
df = pd.read_csv('dataframe_ex.csv')
# Affichage des premières et dernières lignes du DataFrame
print(df.head())
print(df.tail(n=5))

# Sélection de colonnes spécifiques
#colonne_specifique = df['NomColonne']
age = df["Age"]

# Filtrage basé sur une condition
donnees_filtrees = df[df['Age'] > 30]

# Prendre les 2 premières colonnes de données 
donnees_select = df.iloc[:,:2]


# Création d'une nouvelle colonne
#df['NouvelleColonne'] = df['Colonne1'] + df['Colonne2']
df['NouvelleColonne'] = df['Age'] *2
# Remplacer les valeurs manquantes par une valeur spécifique
df.fillna(value=0, inplace=True)

# Combiner 2 Dataframe ensemble
#df = pd.merge(df1,df2)
df = pd.merge(df,df)

# Supprimer les lignes avec des valeurs manquantes
df.dropna(inplace=True)


## Utilisation de numpy 

# Création d'un array NumPy
array = np.array([1, 2, 3, 4, 5])

# Création d'un array 2D
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Opérations mathématiques
somme = np.sum(array)
moyenne = np.mean(array)

# Multiplication de matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
produit = np.dot(A, B)