Poistiko agentti toisteisuuden mielestäsi järkevästi? Onko testikoodi nyt helpommin luettavaa?

Kyllä. Yksittäisiä metodeja on helpompi lukea kun kaikkien metodie alustus tehdään aluksi SetUpissa.

Muuttiko agentti testien toiminnallisuutta, esim. poistiko tai heikensikö se tarkistuksia (assert_called_with vs. assert_called)?

Käytin itse aluksi assert_called_with, agentti muutti sen assert_called_once_with. Muuten toiminnallisuus on pysynyt laajalti samana.

Jouduitko korjaamaan agentin tekemiä muutoksia itse tai pyytämään siltä muutoksia? Mitä ja miksi?

En.
