import js
import string
import re
from pyscript import display, when


def has_sequential_chars(pwd, length=4):        #De functie checkt elk deel van het wachtwoord of er karakters oplopend zijn volgens de ASCII-tabel.
    for i in range(len(pwd) - length + 1):
        chunk = pwd[i:i+length]
        if all(ord(chunk[j]) == ord(chunk[0]) + j for j in range(len(chunk))):
            return True
    return False

@when("click", "#check-btn")                    #Dit geeft aan dat de onderstaande fucnties gelijk uitgevoerd moeten worden zodra de knop 'Check' wordt ingedrukt.
def check_password(event):              #Nieuwe functie die kijkt of een gegeven wachtwoord ook een goed wachtwoord is
    password = str(js.document.getElementById("dutch").value)    
    output_div = js.document.getElementById("output")

    if " " in password:                                               #Het programma checkt of er spaties aanwezig zijn
        output_div.innerText = "Een wachtwoord mag geen spaties bevatten."
    elif len(password) < 10:
        output_div.innerText = "Een goed wachtwoord heeft minstens 10 tekens, probeer het nog eens!"
    elif not any(c.isupper() for c in password):                        #Het programma kijkt of er een hoofdletter (isupper) aanwezig is
        output_div.innerText = "Voeg minstens één hoofdletter toe."
    elif not any(c.islower() for c in password):                        #Het programma kijkt of er een kleine letter (islower) aanwezig is
        output_div.innerText = "Voeg minstens één kleine letter toe."
    elif not any(c.isdigit() for c in password):                        #Het programma kijkt of er een cijfer (isdigit) aanwezig is
        output_div.innerText = "Voeg minstens één cijfer toe."
    elif not any(c in string.punctuation for c in password):            #Het programma kijkt of er een speciaal teken (string.punctuation) aanwezig is
        output_div.innerText = "Voeg minstens één speciaal teken toe."
    elif re.search(r"(.)\1{2,}", password):                             #Het programma zoekt naar één teken dat minstens 2 keer wordt herhaald
        output_div.innerText = "Gebruik niet te veel herhaalde tekens achter elkaar (zoals 'aaa' of '111'). Dat maakt een wachtwoord voorspelbaar."
    elif has_sequential_chars(password):                                #Het programma checkt of er opeenvolgende tekens aanwezig zijn
        output_div.innerText = "Vermijd opeenvolgende tekens zoals 'abcd' of '1234'. Dat maakt een wachtwoord voorspelbaar."
    else:
        output_div.innerHTML = (
        "Goed wachtwoord! 🎉<br>"
        "Jouw wachtwoord voldoet aan alle eisen van een goed wachtwoord:<br>"
        "1. Geen spaties<br>"
        "2. Minimaal 10 tekens lang<br>"
        "3. Minimaal één hoofdletter<br>"
        "4. Minimaal één kleine letter<br>"
        "5. Minimaal één cijfer<br>"
        "6. Minimaal één speciaal teken<br>"
        "7. Niet te voorspelbaar"
        )





