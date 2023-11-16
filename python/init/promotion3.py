import argparse
import datetime


def calculer_age(date_naissance):
    today = datetime.date.today()
    naissance = datetime.datetime.strptime(date_naissance, "%d/%m/%Y").date()
    age = (
        today.year
        - naissance.year
        - ((today.month, today.day) < (naissance.month, naissance.day))
    )
    mois = today.month - naissance.month - (today.day < naissance.day)
    if mois < 0:
        mois += 12
    return age, mois


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--path", type=str)

args = parser.parse_args()
file = args.path

if file == None:
    file = "promotion_B3_B.csv"

# Boucle de lecture ligne à ligne
with open(file, "r") as file:
    nbrf = nbrh = nbro = 0
    # On saute la première ligne
    next(file)
    for line in file:
        fields = line.split(";")
        gender = fields[2]
        date_naissance = fields[4].strip()
        age, mois = calculer_age(date_naissance)
        print(
            f"{fields[1]} {fields[0]} - Âge: {age} ans et {mois} mois - Genre: {gender}"
        )

        if gender.lower() == "h":
            nbrh += 1
        elif gender.lower() == "f":
            nbrf += 1
        else:
            nbro += 1

nbr_tot = nbrf + nbrh + nbro
sep = "=" * 80
print(sep)
print(f"Nombre total d'élèves : {nbr_tot}")
print(f"Nombre total de filles : {nbrf} - {round((nbrf/nbr_tot)*100,2)} %")
print(f"Nombre total de garçons : {nbrh} - {round((nbrh/nbr_tot)*100,2)} %")
print(f"Autres : {nbro} - {round((nbro/nbr_tot)*100,2)} %")
print(sep)
print("fin du programme...")
