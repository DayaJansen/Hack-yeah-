import js
import string
import re
from pyscript import display, when


def has_sequential_chars(pwd, length=4):        #De functie checkt elk deel van het wachtwoord of er karakters oplopend zijn volgens de ASCII-tabel (zoals abcd of 1234).
    for i in range(len(pwd) - length + 1):
        chunk = pwd[i:i+length]
        if all(ord(chunk[j]) == ord(chunk[0]) + j for j in range(len(chunk))):
            return True
    return False

@when("click", "#check-btn")                    #Dit geeft aan dat de onderstaande fucnties gelijk uitgevoerd moeten worden zodra de knop 'Check' wordt ingedrukt.
def check_password(event):              #Nieuwe functie die kijkt of een gegeven wachtwoord ook een goed wachtwoord is
    password = str(js.document.getElementById("dutch").value)    
    output_div = js.document.getElementById("output")

    common_words = ["test", "welkom", "qwerty", "password", "wachtwoord", "admin", "abc123", "letmein", "hoi"]  #Dit zijn de meest voorkomende woorden in wachtwoorden. Dit is natuurlijk heel voorspelbaar.


    score = 0                           #Dit stuk berekent je score, je kan maximaal 5 punten score, 5 punten is een goed wachtwoord. Je krijgt 1 punt voor een wachtwoord met meer dan 10 tekens, 1 punt voor een hoofd- en kleine letter, 1 punt voor een cijfer, 1 punt voor een speciaal teken en je krijgt het laatste punt voor het hebben van geen spaties en als je wachtwoord niet voorspelbaar is.
    if len(password) >= 10:
        score += 1
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if (
        " " not in password and
        not re.search(r"(.)\1{2,}", password) and
        not has_sequential_chars(password) and
        not any(word in password.lower() for word in common_words)
    ):
        score += 1


    for word in common_words:           #Hier kijkt het programma of 1 van de woorden hierboven in het wachtwoord voorkomt. Als dit zo is, geeft het programma terug welk woord het heeft gevonden.
        if word in password.lower():
            js.document.querySelector("#output pre").innerText = (
                f"Vermijd het gebruik van bekende woorden zoals '{word}' in je wachtwoord."
                f"🔢 Wachtwoordscore: {score}/5"
            )
            return
    if " " in password:                                               #Het programma checkt of er spaties aanwezig zijn
        js.document.querySelector("#output pre").innerText = (
            "Een wachtwoord mag geen spaties bevatten.\n\n"
            f"🔢 Wachtwoordscore: {score}/5"
        )
        #Dit is wat het programma vervolgens teruggeeft, zodat je het aan kan passen (je score en wat je moet aanpassen).
    elif len(password) < 10:
        js.document.querySelector("#output pre").innerText = (
            "Een goed wachtwoord heeft minstens 10 tekens, probeer het nog eens!\n\n"
            f"🔢 Wachtwoordscore: {score}/5"
        )
    elif not any(c.isupper() for c in password):                        #Het programma kijkt of er een hoofdletter (isupper) aanwezig is
        js.document.querySelector("#output pre").innerText = (
            "Voeg minstens één hoofdletter toe.\n\n"
            f"🔢 Wachtwoordscore: {score}/5"
        )
    elif not any(c.islower() for c in password):                        #Het programma kijkt of er een kleine letter (islower) aanwezig is
        js.document.querySelector("#output pre").innerText = (
            "Voeg minstens één kleine letter toe."
            f"🔢 Wachtwoordscore: {score}/5"
        )
    elif not any(c.isdigit() for c in password):                        #Het programma kijkt of er een cijfer (isdigit) aanwezig is
        js.document.querySelector("#output pre").innerText = (
            "Voeg minstens één cijfer toe."
            f"🔢 Wachtwoordscore: {score}/5"
        )
    elif not any(c in string.punctuation for c in password):            #Het programma kijkt of er een speciaal teken (string.punctuation) aanwezig is
        js.document.querySelector("#output pre").innerText = (
            "Voeg minstens één speciaal teken toe."
            f"🔢 Wachtwoordscore: {score}/5"
        )
    elif re.search(r"(.)\1{2,}", password):                             #Het programma zoekt naar één teken dat minstens 2 keer wordt herhaald
        js.document.querySelector("#output pre").innerText = (
            "Gebruik niet te veel herhaalde tekens achter elkaar (zoals 'aaa' of '111'). Dat maakt een wachtwoord voorspelbaar."
            f"🔢 Wachtwoordscore: {score}/5"
        )
    elif has_sequential_chars(password):                                #Het programma checkt of er opeenvolgende tekens aanwezig zijn
        js.document.querySelector("#output pre").innerText = (
            "Vermijd opeenvolgende tekens zoals 'abcd' of '1234'. Dat maakt een wachtwoord voorspelbaar."
            f"🔢 Wachtwoordscore: {score}/5"
        )
    else:                                                               #Als alles in orde is geeft het programma aan dat het een goed wachtwoord is.
        js.document.querySelector("#output pre").innerText = (
        "Goed wachtwoord! 🎉\n"
        "Jouw wachtwoord voldoet aan alle eisen van een goed wachtwoord:\n"
        "1. Geen spaties\n"
        "2. Minimaal 10 tekens lang\n"
        "3. Minimaal één hoofdletter\n"
        "4. Minimaal één kleine letter\n"
        "5. Minimaal één cijfer\n"
        "6. Minimaal één speciaal teken\n"
        "7. Niet te voorspelbaar\n\n"
        f"🔢 Wachtwoordscore: {score}/5"
        )




