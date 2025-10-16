# =====================================================================
# Générateur de n-grams (1 et 2-grams) depuis un fichier CSV
# Sans aucune bibliothèque externe (ni Counter, ni itertools)
# =====================================================================

import csv
import os

# --------------------------
# Fonction pour générer les n-grams
# --------------------------
def generate_ngrams(sequence, n):
    """Génère la liste des n-grams d'une séquence donnée."""
    grams = []
    for i in range(len(sequence) - n + 1):
        grams.append(sequence[i:i+n])
    return grams

# --------------------------
# Fonction principale
# --------------------------
def main():
    input_file = "C:/Users/DELL/Desktop/pattern_recognition/output/cytokines1_dataframe.csv"
    output_dir = "C:/Users/DELL/Desktop/pattern_recognition/output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "features_ngrams.csv")

    # Liste des acides aminés standards
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"

    # Générer manuellement toutes les combinaisons possibles de 1 et 2-grams
    all_1grams = [a for a in amino_acids]
    all_2grams = [a + b for a in amino_acids for b in amino_acids]
    feature_columns = all_1grams + all_2grams

    # Lecture du fichier CSV (sans pandas)
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    results = []

    for row in data:
        seq_id = row["ID"]
        sequence = row["Sequence"].strip()

        # Initialiser un dictionnaire pour les fréquences
        counts = {}
        for gram in feature_columns:
            counts[gram] = 0

        # Calculer les fréquences 1-gram et 2-gram
        # (boucle directe, sans Counter)
        for i in range(len(sequence)):
            aa = sequence[i]
            if aa in counts:
                counts[aa] += 1
            if i < len(sequence) - 1:
                dipeptide = sequence[i] + sequence[i+1]
                if dipeptide in counts:
                    counts[dipeptide] += 1

        # Construire la ligne résultat
        row_data = {"id": seq_id}
        row_data.update(counts)
        results.append(row_data)

    # Écriture du fichier CSV final
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id"] + feature_columns)
        writer.writeheader()
        writer.writerows(results)

    print(f" Fichier généré avec succès : {output_file}")

# --------------------------
# Exécution
# --------------------------
if __name__ == "__main__":
    main()
