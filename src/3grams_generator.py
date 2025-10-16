# ===========================================================
#  Générateur de 3-grams (traitement par lots)
#  Optimisé RAM + vitesse pour Google Colab
# ===========================================================

import csv

# ---  Chemins ---
# les chemins sont celles utilisés dans collab
input_file = "/cytokines1_dataframe.csv"
threegrams_file = "/content/output/3grams_list.txt"
output_file = "/content/output/features_3grams.csv"

# ---Charger la liste des 3-grams ---
with open(threegrams_file, "r", encoding="utf-8") as f:
    all_3grams = [line.strip() for line in f if line.strip()]

print(f" {len(all_3grams)} trigrammes chargés.")

# ---  Paramètres de lot ---
BATCH_SIZE = 200   # ← traite 200 séquences à la fois 

# ---  Fonction pour traiter un lot de séquences ---
def process_batch(batch, writer):
    for row in batch:
        seq_id = row["ID"]
        sequence = row["Sequence"].strip().upper()

        # Initialiser les fréquences de tous les trigrammes à 0
        counts = {gram: 0 for gram in all_3grams}

        # Calculer les trigrammes
        for i in range(len(sequence) - 2):
            tri = sequence[i:i+3]
            if tri in counts:
                counts[tri] += 1

        # Construire la ligne résultat
        row_data = {"id": seq_id}
        row_data.update(counts)
        writer.writerow(row_data)

# ---  Lecture et écriture par lots ---
with open(output_file, "w", newline="", encoding="utf-8") as out_f:
    writer = csv.DictWriter(out_f, fieldnames=["id"] + all_3grams)
    writer.writeheader()

    with open(input_file, "r", encoding="utf-8") as in_f:
        reader = csv.DictReader(in_f)
        batch = []
        total = 0

        for row in reader:
            batch.append(row)
            if len(batch) == BATCH_SIZE:
                process_batch(batch, writer)
                total += len(batch)
                print(f" Séquences traitées : {total}")
                batch = []  # vider le lot de la mémoire

        # Traiter le dernier lot restant
        if batch:
            process_batch(batch, writer)
            total += len(batch)
            print(f" Séquences traitées : {total}")

print(f"\n Fichier généré avec succès : {output_file}")