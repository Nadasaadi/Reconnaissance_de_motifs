import pandas as pd

# Lis uniquement les 200 premières lignes
df = pd.read_csv("/content/output/features_3grams.csv", nrows=200)

# Affiche-les joliment dans Colab
pd.set_option('display.max_columns', 20)  # Ajuste le nb de colonnes visibles
display(df.head(200))