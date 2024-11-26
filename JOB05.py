# Création d'un fonction qui renvoie un boolean

def is_prime(nb):
    # Un nombre premier ne peut être égale à 0 ou 1
    if nb == 0 or nb == 1:
        return False
    # Les nombres premiers sont divisable par leurs racine² (ou avoir une puissance de 0.5)
    else:
        diviseur_a_tester = 2
        racine = nb**0.5
        while diviseur_a_tester <= racine:
            if nb % diviseur_a_tester == 0:
                return False
            diviseur_a_tester += 1
        return True
    
    
nombre = 0
nombre2 = 0

for nombre in range(1000):
    nombre2 += 1
    if is_prime(nombre) == True:
        nombre += 1
        print(nombre2)
        