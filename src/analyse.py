import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =====================================================================
# 1. Chargement du DataFrame
# =====================================================================
input_file = "C:/Users/DELL/Desktop/pattern_recognition/output/cytokines1_dataframe.csv"

# ✅ Lecture du fichier CSV avec le bon séparateur (virgule)
df = pd.read_csv(input_file, sep=",")

print(f"✅ {len(df)} séquences chargées avec succès.\n")
print("Aperçu du contenu :")
print(df.head(3))
print("\nColonnes disponibles :", df.columns.tolist())

# =====================================================================
# 2. Description générale du contenu
# =====================================================================
print("\n=== DESCRIPTION DU CONTENU DU FICHIER ===")

# Nombre total de séquences
nombre_sequences = len(df)

# Espèces uniques présentes
if "Specie" in df.columns:
    especes = df["Specie"].unique()
    nombre_especes = len(especes)
else:
    especes = ["Inconnue"]
    nombre_especes = 1

# ✅ Ajout d'une colonne pour la longueur des séquences
df["Length"] = df["Sequence"].apply(len)

# Longueur moyenne et maximale
longueur_moyenne = df["Length"].mean()
longueur_maximale = df["Length"].max()

# Nombre total d’acides aminés dans l’ensemble du fichier
nombre_total_acides_amines = df["Length"].sum()

# Affichage
print(f"Nombre total de séquences : {nombre_sequences}")
print(f"Nombre total d'espèces présentes : {nombre_especes}")
print("Espèces identifiées :")
for esp in especes:
    print(f" - {esp}")
print(f"Longueur moyenne des séquences : {longueur_moyenne:.2f} acides aminés")
print(f"Longueur maximale observée : {longueur_maximale} acides aminés")
print(f"Nombre total d’acides aminés dans le fichier : {nombre_total_acides_amines}")

# =====================================================================
# 3. Statistiques descriptives globales sur les longueurs
# =====================================================================
print("\n=== STATISTIQUES DESCRIPTIVES SUR LES LONGUEURS ===")
stats = df["Length"].describe()
print(stats)

# =====================================================================
# 4. Distribution des longueurs des séquences
# =====================================================================
plt.figure(figsize=(10, 5))
sns.histplot(df["Length"], bins=50, kde=True, color="skyblue")
plt.title("Distribution des longueurs des séquences protéiques (Cytokines)")
plt.xlabel("Longueur de la séquence (nombre d'acides aminés)")
plt.ylabel("Nombre de séquences")
plt.show()

# =====================================================================
# 5. Analyse de la fréquence des acides aminés
# =====================================================================
print("\n=== FRÉQUENCE DES ACIDES AMINÉS ===")

# Concaténer toutes les séquences
toutes_sequences = "".join(df["Sequence"])
frequence_acides = Counter(toutes_sequences)

# Conversion en DataFrame pour affichage
freq_df = pd.DataFrame(frequence_acides.items(), columns=["Acide_Amine", "Fréquence"])
freq_df = freq_df.sort_values(by="Fréquence", ascending=False)

print("\nLes 10 acides aminés les plus fréquents :")
print(freq_df.head(10))

# Graphique
plt.figure(figsize=(10, 5))
sns.barplot(data=freq_df, x="Acide_Amine", y="Fréquence", palette="magma")
plt.title("Fréquence des acides aminés dans les séquences de cytokines")
plt.xlabel("Acide aminé")
plt.ylabel("Fréquence")
plt.show()

# =====================================================================
# 6. Statistiques par espèce (si plusieurs présentes)
# =====================================================================
if "Specie" in df.columns:
    print("\n=== STATISTIQUES PAR ESPÈCE ===")
    stats_par_espece = df.groupby("Specie")["Length"].describe()
    print(stats_par_espece)

# =====================================================================
# 7. Sauvegarde des résultats dans un fichier texte
# =====================================================================
output_dir = "C:/Users/DELL/Desktop/pattern_recognition/output"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "statistiques_descriptives_cytokines.txt")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("=== DESCRIPTION DU CONTENU DU FICHIER ===\n")
    f.write(f"Nombre total de séquences : {nombre_sequences}\n")
    f.write(f"Nombre total d'espèces présentes : {nombre_especes}\n")
    f.write("Espèces identifiées :\n")
    for esp in especes:
        f.write(f" - {esp}\n")
    f.write(f"Longueur moyenne des séquences : {longueur_moyenne:.2f} acides aminés\n")
    f.write(f"Longueur maximale observée : {longueur_maximale} acides aminés\n")
    f.write(f"Nombre total d’acides aminés dans le fichier : {nombre_total_acides_amines}\n\n")

    f.write("=== STATISTIQUES DESCRIPTIVES SUR LES LONGUEURS ===\n")
    f.write(str(stats))
    f.write("\n\n=== FRÉQUENCE DES ACIDES AMINÉS ===\n")
    for aa, freq in frequence_acides.items():
        f.write(f"{aa}: {freq}\n")

print(f"\n💾 Les statistiques descriptives détaillées ont été enregistrées dans : {output_file}")
