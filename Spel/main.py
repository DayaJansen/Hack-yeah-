from pyscript import when
from js import document

emails = [
    {"text": "Uw bankrekening wordt geblokkeerd. Klik hier om te voorkomen: http://bankveiligheid-login.com", "isPhishing": True},
    {"text": "Uw pakket is onderweg! Track & Trace: PostNL App", "isPhishing": False},
    {"text": "Gefeliciteerd! U heeft een iPhone gewonnen. Klik hier om te claimen.", "isPhishing": True},
    {"text": "Je Apple ID werd gebruikt om in te loggen op een nieuw apparaat.", "isPhishing": False}
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
    check_answer(user_thinks_real=True)

@when("click", "#phishing-btn")
def handle_phishing_click(event):
    check_answer(user_thinks_real=False)

@when("click", "#next-btn")
def next_email(event):
    global current_index

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
