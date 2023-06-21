# Django_seminar

### Izraditi sustav za upis studenata. Sustav ce se sastojati od tri uloge: student, profesor i administrator.

Uloga administrator:
- autentikacija
- pregled i promjena liste predmeta
- dodavanje novog predmeta
- dodjeljivanje predmeta profesoru
- pregled liste studenata
- dodavanje i editiranje studenata
- izrada/promjena upisnog lista za bilo kojeg studenta
- pregled liste profesora
- dodavanje i editiranje profesora
- pregled popisa studenata za svaki pojedinacni predmet (na svaki predmet dodati link „vidi popis studenata”)
- za administrator ulogu nije dozvoljeno koristiti Djangov admin sustav

Uloga profesor:
- autentikacija
- pregled liste predmeta prijavljenog profesora
- pregled popisa studenata na pojedinom kolegiju (kojem je prijavljeni profesor nositelj)
- mijenjanje statusa predmeta (po defaultu je samo upisan, a moze se promijeniti u „polozen” ili „izgubio potpis”. Predmet se moze ispisati sve dok mu status nije promijenjen u polozen/izgubio potpis)
- pregled studenata na svakom pojedinom predmetu prema sljedecim kriterijima:
1. studenti koji su izgubili potpis
2. studenti koji su dobili potpis, ali jos nisu polozili predmet
3. studenti koji su polozili predmet

Uloga student:
- autentikacija
- upis/ispis predmeta
