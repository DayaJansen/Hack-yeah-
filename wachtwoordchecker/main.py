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
        js.document.querySelector("#output pre").innerText = "Een wachtwoord mag geen spaties bevatten."
    elif len(password) < 10:
        js.document.querySelector("#output pre").innerText = "Een goed wachtwoord heeft minstens 10 tekens, probeer het nog eens!"
    elif not any(c.isupper() for c in password):                        #Het programma kijkt of er een hoofdletter (isupper) aanwezig is
        js.document.querySelector("#output pre").innerText = "Voeg minstens één hoofdletter toe."
    elif not any(c.islower() for c in password):                        #Het programma kijkt of er een kleine letter (islower) aanwezig is
        js.document.querySelector("#output pre").innerText = "Voeg minstens één kleine letter toe."
    elif not any(c.isdigit() for c in password):                        #Het programma kijkt of er een cijfer (isdigit) aanwezig is
        js.document.querySelector("#output pre").innerText = "Voeg minstens één cijfer toe."
    elif not any(c in string.punctuation for c in password):            #Het programma kijkt of er een speciaal teken (string.punctuation) aanwezig is
        js.document.querySelector("#output pre").innerText = "Voeg minstens één speciaal teken toe."
    elif re.search(r"(.)\1{2,}", password):                             #Het programma zoekt naar één teken dat minstens 2 keer wordt herhaald
        js.document.querySelector("#output pre").innerText = "Gebruik niet te veel herhaalde tekens achter elkaar (zoals 'aaa' of '111'). Dat maakt een wachtwoord voorspelbaar."
    elif has_sequential_chars(password):                                #Het programma checkt of er opeenvolgende tekens aanwezig zijn
        js.document.querySelector("#output pre").innerText = "Vermijd opeenvolgende tekens zoals 'abcd' of '1234'. Dat maakt een wachtwoord voorspelbaar."
    else:
        js.document.querySelector("#output pre").innerText = (
        "Goed wachtwoord! 🎉\n"
        "Jouw wachtwoord voldoet aan alle eisen van een goed wachtwoord:\n"
        "1. Geen spaties\n"
        "2. Minimaal 10 tekens lang\n"
        "3. Minimaal één hoofdletter\n"
        "4. Minimaal één kleine letter\n"
        "5. Minimaal één cijfer\n"
        "6. Minimaal één speciaal teken\n"
        "7. Niet te voorspelbaar"
        )




