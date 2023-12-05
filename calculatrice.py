def addition(nombre1, nombre2):
    return nombre1 + nombre2

def soustraction(nombre1, nombre2):
    return nombre1 - nombre2

def multiplication(nombre1, nombre2):
    return nombre1 * nombre2

def division(nombre1, nombre2):
    if nombre2 != 0:
        return nombre1 / nombre2
    else:
        raise ValueError("Erreur: Division par zéro")

# Demander à l'utilisateur d'entrer deux nombres et l'opération
try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    operation = input("Entrez l'opération (+, -, *, /) : ")

    # Effectuer l'opération demandée
    if operation == "+":
        resultat = addition(nombre1, nombre2)
    elif operation == "-":
        resultat = soustraction(nombre1, nombre2)
    elif operation == "*":
        resultat = multiplication(nombre1, nombre2)
    elif operation == "/":
        resultat = division(nombre1, nombre2)
    else:
        raise ValueError("Erreur: Opération non valide")

    # Afficher le résultat
    print(f"Le résultat de {nombre1} {operation} {nombre2} est : {resultat}")

except ValueError as e:
    print(f"Erreur: {e}. Veuillez entrer des nombres valides et une opération correcte.")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")
