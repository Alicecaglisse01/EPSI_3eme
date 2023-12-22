import datetime
import unittest
from init.promotion3 import calculer_age


class TestCalculAge(unittest.TestCase):
    def test_majorite(self):
        # Calculer la date qui donnerait 18 ans aujourd'hui
        date_18_ans = datetime.date(datetime.date.today().year - 18, datetime.date.today().month, datetime.date.today().day)


        # Calculer les dates pour hier, aujourd'hui et demain
        date_hier = date_18_ans - datetime.timedelta(days=1)
        print("Date de naissance pour 'hier':", date_hier.strftime('%d/%m/%Y'))
        date_demain = date_18_ans + datetime.timedelta(days=1)

        age_hier, _ = calculer_age(date_hier.strftime('%d/%m/%Y'))
        age_aujourdhui, _ = calculer_age(date_18_ans.strftime('%d/%m/%Y'))
        age_demain, _ = calculer_age(date_demain.strftime('%d/%m/%Y'))

        self.assertGreaterEqual(age_hier, 18, "Hier, la personne devrait être majeure.")
        self.assertGreaterEqual(age_aujourdhui, 18, "Aujourd'hui, la personne devrait être majeure.")
        self.assertLess(age_demain, 18, "Demain, la personne devrait être mineure.")

if __name__ == '__main__':
    unittest.main()
