import csv


with open("python/fichiers/promotion_B3_B.csv", mode="r", encoding="utf-8-sig") as file:
    csv_reader = csv.reader(file, delimiter=";")
    next(csv_reader)

    for row in csv_reader:
        nom = row[0]
        prenom = row[1]
        email = row[3]

        print(f"Nom: {nom}, Prénom: {prenom}, Email: {email}")
