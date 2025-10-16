# ======================================================
# Script unique à exécuter une seule fois pour générer la liste des combinaisons possibles des 3 acides aminés
# ======================================================

amino_acids = "ACDEFGHIKLMNPQRSTVWY"

with open("C:/Users/DELL/Desktop/pattern_recognition/output/3grams_list.txt", "w") as f:
    for a in amino_acids:
        for b in amino_acids:
            for c in amino_acids:
                f.write(a + b + c + "\n")

print("✅ Fichier 3grams_list.txt généré avec succès !")

#----------------------------------------
# ======================================================
# Génère toutes les combinaisons possibles de 3-grams
# et les enregistre dans /content/3grams_list.txt
# ======================================================

import os

# Dossier de sortie (créé automatiquement)
output_dir = "/content/output"
os.makedirs(output_dir, exist_ok=True)

# Liste des acides aminés standards
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

# Fichier de sortie
output_file = os.path.join(output_dir, "3grams_list.txt")

# Génération du fichier
with open(output_file, "w") as f:
    for a in amino_acids:
        for b in amino_acids:
            for c in amino_acids:
                f.write(a + b + c + "\n")

print("✅ Fichier généré :", output_file)