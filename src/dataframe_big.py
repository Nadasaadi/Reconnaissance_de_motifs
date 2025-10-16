# =====================================================================
# Parser FASTA UniProt Canonical - Compatible avec tr| et sp|
# Sauvegarde finale : CSV
# =====================================================================

import os
import csv  # <-- pour écrire proprement au format CSV

# ==============================
# Fichier d'entrée (FASTA)
# ==============================
fasta_file = "C:/Users/DELL/Desktop/pattern_recognition/data/uniprotkb_cytokines_2025_10_16.fasta"

# ==============================
# Création automatique du dossier output
# ==============================
output_dir = "C:/Users/DELL/Desktop/pattern_recognition/output"
os.makedirs(output_dir, exist_ok=True)

# Nom du fichier de sortie CSV
output_file = os.path.join(output_dir, "cytokines1_dataframe.csv")

# ==============================
# Lecture du fichier FASTA
# ==============================
with open(fasta_file, "r") as file:
    lines = file.readlines()

data = []
current_id = ""
current_name = ""
current_specie = ""
current_sequence = ""

for line in lines:
    line = line.strip()

    if len(line) > 0 and line[0] == ">":
        if current_id != "":
            data.append([current_id, current_name, current_specie, current_sequence])
            current_sequence = ""

        parts = line.split(" ")
        header_main = parts[0]
        bars = header_main.split("|")

        if len(bars) >= 3:
            current_id = bars[1]
            current_name = bars[2]
        else:
            current_id = ""
            current_name = ""

        specie = ""
        for i in range(len(parts)):
            if parts[i].startswith("OS="):
                specie = parts[i][3:]
                j = i + 1
                while j < len(parts) and not parts[j].startswith("OX="):
                    specie += " " + parts[j]
                    j += 1
                break
        current_specie = specie.strip()

    elif len(line) > 0:
        current_sequence += line

if current_id != "":
    data.append([current_id, current_name, current_specie, current_sequence])

# ==============================
# Affichage formaté (aperçu console)
# ==============================
print("{:<12} {:<20} {:<40} {}".format("ID", "Name", "Specie", "Sequence"))
print("-" * 100)
for entry in data[:10]:  # affiche seulement les 10 premières lignes
    print("{:<12} {:<20} {:<40} {}".format(
        entry[0], entry[1], entry[2], entry[3][:50] + "..."
    ))

# ==============================
# Sauvegarde au format CSV
# ==============================
with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "Name", "Specie", "Sequence"])  # entêtes
    writer.writerows(data)

print(f"\n✅ Extraction terminée : données sauvegardées dans '{output_file}' (format CSV)")
