# Testikoodin siistiminen agentin avulla

Käytin tehtävässä agenttina Claude Codea. Annoin sen siistiä tehtävän 3 `kauppa_test.py`:n itsenäisesti ja tarkistin muutoksen sen jälkeen.

## Poistiko agentti toisteisuuden järkevästi?

Kyllä. Jokainen viidestä testistä loi aiemmin omat mockinsa ja `saldo`- ja `hae_tuote`-toteutukset. Agentti siirsi ne `setUp`-metodiin: pankki- ja viitegeneraattorimockit, varastomockin ja `Kauppa`-olion. Varaston tuotteet ja saldot on nyt koottu yhteen paikkaan sanakirjoiksi (maito 5 €, leipä 3 €, juusto 7 € joka on loppu), ja `side_effect` hakee arvot niistä. Tiedosto lyheni 157 rivistä 73 riviin. Testeihin jäi vain itse toiminta (`aloita_asiointi`, `lisaa_koriin`, `tilimaksu`) ja tarkistus, joten jokaisesta testistä näkee nyt yhdellä silmäyksellä, mitä se testaa.

## Muuttiko agentti testien toiminnallisuutta?

Tarkistukset eivät muuttuneet. Vertasin `git diff`:n avulla jokaisen testin `assert`-rivit ennen ja jälkeen: kaikki `assert_called_with`-tarkistukset ovat ennallaan, eikä yhtäkään niistä heikennetty muotoon `assert_called`. Ainoa `assert_called` on tehtäväpohjan alkuperäisessä testissä.

Yksi testidatan muutos tuli: loppuneen tuotteen testi käytti aiemmin tuotetta 2 saldolla 0. Koska yhteisessä alustuksessa tuote 2 (leipä) on varastossa, agentti lisäsi loppuneeksi tuotteeksi tuotteen 3 (juusto) ja vaihtoi testin käyttämään sitä. Testattava asia ei muuttunut.

Varmistin vielä, että testit huomaavat bugit samoin kuin ennen, rikkomalla `Kauppa`-luokan väliaikaisesti kolmella tavalla:

- loppuneen tuotteen hyväksyminen koriin → loppuneen tuotteen testi hajosi
- asiakkaan ja kaupan tilinumeroiden vaihtaminen keskenään → 4 testiä hajosi
- viitenumeron korvaaminen vakiolla → 4 testiä hajosi

## Jouduinko korjaamaan agentin muutoksia?

En joutunut. Testit menivät läpi ensimmäisellä yrityksellä (5/5). Tiedoston alkuun jäi tehtäväpohjasta käyttämättömiä importteja (`ANY`, `Viitegeneraattori`, `Varasto`). Ne jätettiin tarkoituksella, koska tehtävä koski vain toisteisuuden poistamista.
