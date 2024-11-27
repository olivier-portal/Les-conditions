# Créez un programme qui demande à l’utilisateur trois longueurs, a, b, c.
# À l’aide de ces trois longueurs, déterminez s’il est possible de construire un triangle.
# Déterminez ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque.

# Attention : un triangle rectangle peut être isocèle.

# Solution  :)

# Entrer les numeros
a = float(input("Entrez votre premier numero : "))
b = float(input("Entrez votre deuxieme numero : "))
c = float(input("Entrez votre troisieme numero : "))

# Trouver la variable superieur
if a > b and a > c:
    superieur = a
    print(f"Le numero superieur est {superieur}")
    
    summatoire = b + c
    
    if summatoire > superieur:
        print(f"La summatoire entre {b} + {c} est major que {superieur}")
        print("Est possible de construire un triangle")
        
        if a == b == c:
            type_equilateral = True
        else:
            type_equilateral = False
        if a == b != c or a != b == c or a == c != b:
            type_isocele = True
        else:
            type_isocele = False
        if b*b + c*c == a*a:
            type_rectangle = True
        else:
            type_rectangle = False
            
            
        if type_equilateral == True:
            print("Le triangle est équilateral")
        elif type_isocele == True:
            print("Le triangle est isocèle")
        elif type_isocele == True and type_rectangle == True:
            print("Le triangle est isocèle et rectangle")
        elif type_rectangle == True:
            print("Le triangle est rectangle")
        else:
            print("Ninguno")
    else:
        print(f"Ne pas possible de construire un triangle")
elif b > a and b > c:
    superieur = b
    print(f"Le numero superieur est {superieur}")
    
    summatoire = a + c
    
    if summatoire > superieur:
        print(f"La summatoire entre {a} + {c} est major que {superieur}")
        print("Est possible de construire un triangle")
        
        if a == b == c:
            type_equilateral = True
        else:
            type_equilateral = False
        if a == b != c or a != b == c or a == c != b:
            type_isocele = True
        else:
            type_isocele = False
        if a*a + c*c == b*b:
            type_rectangle = True
        else:
            type_rectangle = False
            
            
        if type_equilateral == True:
            print("Le triangle est équilateral")
        elif type_isocele == True:
            print("Le triangle est isocèle")
        elif type_isocele == True and type_rectangle == True:
            print("Le triangle est isocèle et rectangle")
        elif type_rectangle == True:
            print("Le triangle est rectangle")
        else:
            print("Ninguno")
    else:
        print(f"Ne pas possible de construire un triangle")
elif c > a and c > b:
    superieur = c
    print(f"Le numero superieur est {superieur}")
    
    summatoire = a + b
    
    if summatoire > superieur:
        print(f"La summatoire entre {a} + {b} est major que {superieur}")
        print("Est possible de construire un triangle")
        
        if a == b == c:
            type_equilateral = True
        else:
            type_equilateral = False
        if a == b != c or a != b == c or a == c != b:
            type_isocele = True
        else:
            type_isocele = False
        if a*a + b*b == c*c:
            type_rectangle = True
        else:
            type_rectangle = False
            
            
        if type_equilateral == True:
            print("Le triangle est équilateral")
        elif type_isocele == True:
            print("Le triangle est isocèle")
        elif type_isocele == True and type_rectangle == True:
            print("Le triangle est isocèle et rectangle")
        elif type_rectangle == True:
            print("Le triangle est rectangle")
        else:
            print("Ninguno")
    else:
        print(f"Ne pas possible de construire un triangle")
        
