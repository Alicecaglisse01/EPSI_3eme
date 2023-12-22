import datetime
import os

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

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_file = os.path.join(base_dir, 'fichiers', 'promotion_B3_B.csv')

# Utilisez csv_file pour ouvrir le fichier
with open(csv_file, "r") as file:
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
