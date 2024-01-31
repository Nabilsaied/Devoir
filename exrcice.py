
print("Multiplication ")

nb=int(input("Donner votre nombre : "))
print("Vous avez choisir :",nb)



for i in range(11):
    print(nb * i)

choix = input("Veux-tu recommencer? (Oui ou Non) : ").lower()

if choix == "oui":
    nb = int(input("Donner un autre  nombre : "))
    for i in range(11):
        print(nb * i)
elif choix == "non":
    print("C'est fini ")
else:
    print("Choix non valide. On recommence.")
