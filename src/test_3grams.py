# ======================================================
# Vérifie si toutes les lignes ont uniquement des 0
# Aucun fichier de sortie — affiche seulement un message
# ======================================================

import csv


input_file = "/content/output/features_3grams.csv"

total_lines = 0
all_zero_lines = 0

with open(input_file, "r", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        total_lines += 1

        # Vérifie si toutes les valeurs (sauf 'id') sont nulles
        all_zero = all(
            (v.strip() == "0" or v.strip() == "")
            for k, v in row.items()
            if k != "id"
        )

        if all_zero:
            all_zero_lines += 1

# ---------------------------------------
# Résultat final
# ---------------------------------------
if all_zero_lines == total_lines:
    print(" Toutes les lignes contiennent uniquement des valeurs nulles (0).")
elif all_zero_lines == 0:
    print(" Aucune ligne entièrement nulle, toutes contiennent au moins un 3-gram non nul.")
else:
    print(f"ℹ {all_zero_lines} lignes sur {total_lines} contiennent uniquement des zéros.")

  #ce code retourne: 
    # Aucune ligne entièrement nulle, toutes contiennent au moins un 3-gram non nul.