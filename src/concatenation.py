import os

# ==============================
# Liste des fichiers à fusionner
# ==============================
fichiers = [
    "C:/Users/DELL/Desktop/pattern_recognition/data/uniprotkb_cytokines_AND_model_organism_2025_10_16.fasta",
    "C:/Users/DELL/Desktop/pattern_recognition/data/uniprotkb_cytokines_AND_model_organism_2025_10_16.fasta (1)",
    "C:/Users/DELL/Desktop/pattern_recognition/data/uniprotkb_cytokines_AND_model_organism_2025_10_16.fasta (2)",
    "C:/Users/DELL/Desktop/pattern_recognition/data/uniprotkb_cytokines_AND_model_organism_2025_10_16.fasta (3)",
    "C:/Users/DELL/Desktop/pattern_recognition/data/uniprotkb_cytokines_AND_model_organism_2025_10_16.fasta (4)"
]

# ==============================
# Création du dossier output
# ==============================
output_dir = "C:/Users/DELL/Desktop/pattern_recognition/output"
os.makedirs(output_dir, exist_ok=True)

# ==============================
# Nom et chemin du fichier final
# ==============================
fichier_sortie = os.path.join(output_dir, "concatenation.txt")

# ==============================
# Fusion des fichiers
# ==============================
with open(fichier_sortie, "w", encoding="utf-8") as outfile:
    for nom_fichier in fichiers:
        if os.path.exists(nom_fichier):
            with open(nom_fichier, "r", encoding="utf-8") as infile:
                contenu = infile.read().strip()
                outfile.write(contenu + "\n")
            print(f"✅ Fusionné : {nom_fichier}")
        else:
            print(f"⚠️ Fichier introuvable : {nom_fichier}")

print(f"\n✅ Fusion terminée. Fichier final : {fichier_sortie}")
