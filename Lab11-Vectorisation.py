import numpy as np
#initialisation des tableaux
A = np.array([5, 10, 15, 20])
B = np.array([1, 2, 3, 4])
print("A :", A)
print("B :", B)

#Étape 2 – Opérations élémentaires vectorisées
addition = A + B
multiplication = A * B         # produit élément par élément
puissances = A ** 2             # carré de chaque valeur
print("Addition (A + B) :", addition)
print("Multiplication (A * B) :", multiplication)
print("Puissances (A ** 2) :", puissances)

#Étape 3 – Fonctions universelles
angles = np.linspace(0, np.pi, 5)  # 0 → π en 5 points
sinus = np.sin(angles)
logarithmes = np.log(angles[1:])   # log(0) étant indéfini, on ignore le premier élément
print("Angles :", angles)
print("sin(angles) :", sinus)
print("log(angles[1:]) :", logarithmes)
print("exp(A) :", np.exp(A))
print("sqrt(B) :", np.sqrt(B))

#Étape 4 – Masques booléens et filtrage
masque = A > 10
print("Masque A > 10 :", masque)
valeurs_filtrées = A[masque]
print("Valeurs de A > 10 :", valeurs_filtrées)

#Étape 5 – Broadcasting : principes et cas pratiques
#ajouter un scalaire
addition_scalaire = A + 5
print("A + 5 =", addition_scalaire)
#additionner un vecteur ligne à une matrice
M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
vecteur_ligne = np.array([10, 20, 30])
resultat = M + vecteur_ligne
print("M + vecteur_ligne :\n", resultat)
#broadcasting  colonne
vecteur_colonne = np.array([[10],
                            [20],
                            [30]])
resultat_colonne = M + vecteur_colonne
print("M + vecteur_colonne :\n", resultat_colonne)

#Étape 6 – Applications et vérifications
#Calcul vectoriel global
C = (A * 2) + np.sin(A) - np.mean(A)
print("Opération composite sur A :", C)
log_A = np.log(A)
masque_log = log_A > 2
print("log(A) > 2 :", log_A[masque_log])
print("shape de C :", C.shape)
print("shape de log_A :", log_A.shape)
print("shape de masque_log :", masque_log.shape)