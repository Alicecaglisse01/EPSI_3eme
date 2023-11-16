"""
Nom : Moisan
Prénom : Alice
Date : 16/11/2023 

"""

import csv
import argparse

parser = argparse.ArgumentParser(
    description="Lire et analyser un fichier CSV de promotion."
)
parser.add_argument(
    "--file",
    "-f",
    type=str,
    default="promotion_B3_B.csv",
    help="Chemin du fichier CSV à analyser",
)

args = parser.parse_args()
chemin_csv = args.file


nombre_total = 0
nombre_filles = 0
nombre_garcons = 0
autre = 0

with open(chemin_csv, mode="r", encoding="utf-8-sig") as file:
    csv_reader = csv.reader(file, delimiter=";")
    next(csv_reader)  # ça ignore l'entête du fichier

    for row in csv_reader:
        nombre_total += 1
        genre = row[2].upper()
        if genre == "F":
            nombre_filles += 1
        elif genre == "H":
            nombre_garcons += 1
        else:
            autre += 1


pourcentage_filles = (nombre_filles / nombre_total) * 100 if nombre_total > 0 else 0
pourcentage_garcons = (nombre_garcons / nombre_total) * 100 if nombre_total > 0 else 0
pourcentage_autre = (
    (autre / nombre_total) * 100 if nombre_total > 0 else 0
)  # ici on vérifie juste que le nombre_total n'est pas = à 0 ou si il n'est pas rempli

print(f"Nombre total d'élèves : {nombre_total}")
print(f"Nombre total de filles : {nombre_filles} - {pourcentage_filles:.2f}%")
print(f"Nombre total de garçons : {nombre_garcons} - {pourcentage_garcons:.2f}%")
print(f"Autres : {autre} - {pourcentage_autre:.2f}%")
