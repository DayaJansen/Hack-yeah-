from pyscript import when
from js import document

emails = [                      #Dit is de lijst waarin alle emails zijn opgeslagen, deze krijg je te zien in het spel. isPhishing = of het om phishing gaat of niet.
    {"text": "Uw bankrekening wordt geblokkeerd. Klik hier om te voorkomen: http://bankveiligheid-login.com", "isPhishing": True},
    {"text": "Gefeliciteerd! U heeft een iPhone gewonnen. Klik hier om te claimen.", "isPhishing": True},
    {"text": "Je Apple ID werd gebruikt om in te loggen op een nieuw apparaat.", "isPhishing": False},
    {"text": "Uw belastingteruggave is beschikbaar. Klik op de link om uw gegevens te bevestigen: http://belastingdienst-check.com", "isPhishing": True},
    {"text": "Uw bestelling bij Bol.com is succesvol geplaatst en wordt binnenkort geleverd.", "isPhishing": False},
    {"text": "Je hebt een uitnodiging ontvangen voor een Teams-meeting van je docent.", "isPhishing": False},
    {"text": "Uw pakket is onderweg! Track & Trace: PostNL App", "isPhishing": False},
    {"text": "U komt in aanmerking voor een vergoeding van €275. Bevestig nu uw rekeningnummer.", "isPhishing": True},
    {"text": "Uw OV-chipkaart is bijna verlopen. Vraag hier direct een nieuwe aan via onze website.", "isPhishing": False},
    {"text": "Er staat een ongebruikelijke login op uw Microsoft-account. Klik hier om uw identiteit te verifiëren.", "isPhishing": True},
    {"text": "De school heeft het rooster voor volgende week aangepast. Bekijk het hier in Magister.", "isPhishing": False},
    {"text": "Uw telefoonabonnement wordt binnenkort verlengd. Klik hier om uw bankgegevens bij te werken.", "isPhishing": True},
    {"text": "Je hebt een cadeaubon van €100 gewonnen van de HEMA! Vul je gegevens in om hem te ontvangen.", "isPhishing": True},
    {"text": "Er is een update beschikbaar voor je DigiD app. Update deze via de officiële app store.", "isPhishing": False}, 
    {"text": "Je hebt je wachtwoord voor Instagram succesvol gewijzigd. Was jij dit niet? Klik hier.", "isPhishing": False},
    ]

current_index = -1          #Geeft aan welke e-mail wordt getoond. -1 = nog niet gestart, we willen niet dat het spel gelijk start, we willen dat er eerst op een start-knop wordt gedrukt.
score = 0                   #De score geeft aan hoeveel goede antwoorden de speler heeft gegeven.
game_started = False        #Geeft aan of het spel begonnen is. We willen dat er eerst op start wordt gedrukt en dat het spel dus niet gelijk begint, daarom staat er false.

def show_email():           #Functie die de emails op het scherm laat zien.
    email_text = emails[current_index]["text"]  #Variabele die één email bevat. Als de current index verandert, krijgt deze variabele ook een andere inhoud, namelijk het volgende mailtje.
    document.getElementById("email-text").innerText = email_text    #document.getElementById("email-text").innerText = hier krijg je het mailtje op het scherm te zien.
    document.getElementById("feedback").innerText = ""      #Het veld waar de feedback (goed of fout) staat wordt hier geleegd, want er wordt een nieuwe e-mail getoond.
    document.getElementById("final-score").innerText = ""   #Het veld waar de score aan het eind van het spel staat wordt hier geleegd, want er wordt een nieuwe e-mail getoond.

def enable_answer_buttons(enabled: bool):       #Deze functie zet alle knoppen aan. (De real-knop waar je op klikt als een mailtje echt is en de phishing-knop waar je op drukt als een mailtje nep is.) 
    document.getElementById("real-btn").disabled = not enabled
    document.getElementById("phishing-btn").disabled = not enabled

@when("click", "#start-btn")
def start_game(event):                      #Deze functie wordt uitgevoerd wanneer (when, zie hierboven) er op de start-knop wordt gedrukt.
    global current_index, score, game_started       #Deze regel zegt tegen Python dat de variabelen current_index, score en game_started aangepast gaan worden.
    current_index = 0
    score = 0              # Het spel wordt teruggezet naar de beginstatus.
    game_started = True

    document.getElementById("start-btn").style.display = "none"
    document.querySelector(".buttons").style.display = "block"    #Start-knop wordt verbergt, samen met de volgende-knop. De antwoordknoppen worden getoond.
    document.getElementById("next-btn").style.display = "none"
    enable_answer_buttons(True)

    show_email()            #Het eerste mailtje wordt getoond.

@when("click", "#real-btn")
def handle_real_click(event):       #Deze functie gaat in werking als een speler op de start-knop drukt.
    if not game_started:
        return
    check_answer(user_thinks_real=True) 	#Roept de functie check_anwer aan. Het antwoord wordt dus vergeleken met het goede antwoord.

@when("click", "#phishing-btn")
def handle_phishing_click(event):       #Deze functie gaat in werking als een speler op de phishing-knop durkt.
    if not game_started:
        return
    check_answer(user_thinks_real=False)    #Roept de functie check_anwer aan. Het antwoord wordt dus vergeleken met het goede antwoord.

@when("click", "#next-btn")
def next_email(event):              #Deze functie gaat in werking als er op de volgende-knop wordt gedrukt.
    global current_index, game_started

    current_index += 1          #Het programma gaat naar de volgende mail.
    if current_index >= len(emails):        #Het spel stopt als het einde van de lijst is bereikt.
        end_game()
    else:                                   #Nog niet het einde van de lijst = de volgende mail wordt laten zien.
        show_email()
        enable_answer_buttons(True)            #antwoord-knoppen (echt, phishing) worden geactiveerd.
        document.getElementById("next-btn").style.display = "none"
        document.getElementById("feedback").innerText = ""

def check_answer(user_thinks_real: bool):       #Deze functie controleert of het gegeven antwoord goed is en zet de antwoord-knoppen uit.
    global score

    enable_answer_buttons(False)

    correct = (user_thinks_real == (not emails[current_index]["isPhishing"]))       #Hier vergelijkt het programma het antwoord van de speler met het goede antwoord en als de speler het goede antwoord heeft gegeven, wordt de score met 1 verhoogd.
    if correct:
        score += 1
        feedback = "✅ Correct!"
    else:
        feedback = "❌ Fout!"

    document.getElementById("feedback").innerText = feedback                #Laat de feedback (goed of fout) zien en laat de volgende knop zien.
    document.getElementById("next-btn").style.display = "inline-block"

def end_game():     #functie wordt aangeroepen als de speler is aangekomen bij de laatste email.
    global game_started
    game_started = False            #Het spel wordt gestopt.
    document.getElementById("email-text").innerText = "Spel afgelopen!"         #"spel afgelopen" wordt laten zien en alle knoppen worden uitgezet.
    document.getElementById("feedback").innerText = ""
    document.querySelector(".buttons").style.display = "none"
    document.getElementById("next-btn").style.display = "none"

    document.getElementById("final-score").innerText = f"Je score: {score} van de {len(emails)}."           #Toont je eindscore.

    document.getElementById("start-btn").style.display = "inline-block"
    document.getElementById("start-btn").innerText = "Opnieuw spelen"       #De start-knop wordt weer laten zien, maar nu staat er opnieuw spelen in plaats van start.
