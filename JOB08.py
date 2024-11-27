a = float(input('Entrez une longueur a : '))
b = float(input('Entrez une longueur b : '))
c = float(input('Entrez une longueur c : '))

if (a < b + c and b < a + c and c < a + b) and (a**2 != b**2 + c**2 and b**2 != a**2 + c**2 and c**2 != a**2 + b**2) and (a != b and a != c and b != c):
    print("ceci est un triangle quelconque")
elif (a < b + c and b < a + c and c < a + b) and ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)) and (a**2 != b**2 + c**2 and b**2 != a**2 + c**2 and c**2 != a**2 + b**2):
    print("ceci est un triangle isocèle")
elif (a < b + c and b < a + c and c < a + b) and (a == b and b == c) and (a**2 != b**2 + c**2 and b**2 != a**2 + c**2 and c**2 != a**2 + b**2):
    print("ceci est un triangle équilatéral")
elif (a < b + c and b < a + c and c < a + b) and (a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2)  and (a != b and a != c and b != c):
    print("ceci est un triangle rectangle")
elif (a < b + c and b < a + c and c < a + b) and (a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2) and (a == b or a == c or b == c):
    print("ceci est un triangle rectangle isocèle")
else:
    print("Avec ces 3 longueurs, nous ne pouvons pas construire un triangle")