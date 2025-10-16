#ce code représente l'une des solutions du probleme lié a la quantitié massive de données 
#ce code filtre les données du dataset selon des critère spécifique démontré dans le rapport
# === CRITERES DE FILTRAGE ===
MIN_LENGTH = 70
PE_ALLOWED = ["PE=1", "PE=2"]

# === FICHIERS ===
input_fasta = "uniprotkb_cytokines_2025_10_13.fasta"
output_fasta = "cytokines_filtered.fasta"

total_count = 0
filtered_count = 0

with open(input_fasta, "r") as infile, open(output_fasta, "w") as outfile:
    header = ""
    sequence = ""

    for line in infile:
        line = line.strip()

        # Si on trouve un nouvel en-tête FASTA
        if line.startswith(">"):
            # Vérifier l'ancienne séquence avant de passer à la suivante
            if header != "":
                total_count += 1

                # Vérifier critères de filtrage
                if "tr|" in header or "A0A" in header:
                    pass  # Exclure TrEMBL ou ID A0A
                elif not any(pe in header for pe in PE_ALLOWED):
                    pass  # Exclure PE >= 3
                elif len(sequence) < MIN_LENGTH:
                    pass  # Exclure fragments
                else:
                    outfile.write(header + "\n")
                    outfile.write(sequence + "\n")
                    filtered_count += 1

            # Nouveau header
            header = line
            sequence = ""
        else:
            # Ajouter la ligne à la séquence
            sequence += line

    # Vérifier la dernière séquence du fichier
    if header != "":
        total_count += 1
        if "tr|" in header or "A0A" in header:
            pass
        elif not any(pe in header for pe in PE_ALLOWED):
            pass
        elif len(sequence) < MIN_LENGTH:
            pass
        else:
            outfile.write(header + "\n")
            outfile.write(sequence + "\n")
            filtered_count += 1

print(f"✅ Filtrage terminé : {filtered_count} séquences conservées sur {total_count}")
print(f"📁 Fichier final : {output_fasta}")

