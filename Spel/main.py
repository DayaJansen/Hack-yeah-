from pyscript import when
from js import document

emails = [
    {"text": "Uw bankrekening wordt geblokkeerd. Klik hier om te voorkomen: http://bankveiligheid-login.com", "isPhishing": True},
    {"text": "Uw pakket is onderweg! Track & Trace: PostNL App", "isPhishing": False},
    {"text": "Gefeliciteerd! U heeft een iPhone gewonnen. Klik hier om te claimen.", "isPhishing": True},
    {"text": "Je Apple ID werd gebruikt om in te loggen op een nieuw apparaat.", "isPhishing": False},
    {"text": "Uw belastingteruggave is beschikbaar. Klik op de link om uw gegevens te bevestigen: http://belastingdienst-check.com", "isPhishing": True},
    {"text": "Uw bestelling bij Bol.com is succesvol geplaatst en wordt binnenkort geleverd.", "isPhishing": False},
    {"text": "We hebben verdachte activiteiten gedetecteerd op uw PayPal-account. Log onmiddellijk in om uw account te beveiligen.", "isPhishing": True},
    {"text": "Je hebt je wachtwoord voor Instagram succesvol gewijzigd. Was jij dit niet? Klik hier.", "isPhishing": False},
    {"text": "U komt in aanmerking voor een vergoeding van €275. Bevestig nu uw rekeningnummer.", "isPhishing": True},
    {"text": "Uw OV-chipkaart is bijna verlopen. Vraag hier direct een nieuwe aan via onze website.", "isPhishing": False},
    {"text": "Er staat een ongebruikelijke login op uw Microsoft-account. Klik hier om uw identiteit te verifiëren.", "isPhishing": True},
    {"text": "De school heeft het rooster voor volgende week aangepast. Bekijk het hier in Magister.", "isPhishing": False},
    {"text": "Uw telefoonabonnement wordt binnenkort verlengd. Klik hier om uw bankgegevens bij te werken.", "isPhishing": True},
    {"text": "Je hebt een uitnodiging ontvangen voor een Teams-meeting van je docent.", "isPhishing": False},
    {"text": "Je hebt een cadeaubon van €100 gewonnen van de HEMA! Vul je gegevens in om hem te ontvangen.", "isPhishing": True},
    {"text": "Er is een update beschikbaar voor je DigiD app. Update deze via de officiële app store.", "isPhishing": False}, 
    ]

current_index = -1
score = 0
game_started = False

def show_email():
    email_text = emails[current_index]["text"]
    document.getElementById("email-text").innerText = email_text
    document.getElementById("feedback").innerText = ""
    document.getElementById("final-score").innerText = ""

def enable_answer_buttons(enabled: bool):
    document.getElementById("real-btn").disabled = not enabled
    document.getElementById("phishing-btn").disabled = not enabled

@when("click", "#start-btn")
def start_game(event):
    global current_index, score, game_started
    current_index = 0
    score = 0
    game_started = True

    document.getElementById("start-btn").style.display = "none"
    document.querySelector(".buttons").style.display = "block"
    document.getElementById("next-btn").style.display = "none"
    enable_answer_buttons(True)

    show_email()

@when("click", "#real-btn")
def handle_real_click(event):
    if not game_started:
        return
    check_answer(user_thinks_real=True)

@when("click", "#phishing-btn")
def handle_phishing_click(event):
    if not game_started:
        return
    check_answer(user_thinks_real=False)

@when("click", "#next-btn")
def next_email(event):
    global current_index, game_started

    current_index += 1
    if current_index >= len(emails):
        end_game()
    else:
        show_email()
        enable_answer_buttons(True)
        document.getElementById("next-btn").style.display = "none"
        document.getElementById("feedback").innerText = ""

def check_answer(user_thinks_real: bool):
    global score

    enable_answer_buttons(False)

    correct = (user_thinks_real == (not emails[current_index]["isPhishing"]))
    if correct:
        score += 1
        feedback = "✅ Correct!"
    else:
        feedback = "❌ Fout!"

    document.getElementById("feedback").innerText = feedback
    document.getElementById("next-btn").style.display = "inline-block"

def end_game():
    global game_started
    game_started = False
    document.getElementById("email-text").innerText = "Spel afgelopen!"
    document.getElementById("feedback").innerText = ""
    document.querySelector(".buttons").style.display = "none"
    document.getElementById("next-btn").style.display = "none"

    document.getElementById("final-score").innerText = f"Je score: {score} van de {len(emails)}."

    document.getElementById("start-btn").style.display = "inline-block"
    document.getElementById("start-btn").innerText = "Opnieuw spelen"
