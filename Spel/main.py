from pyscript import when, display
from js import document
import random

emails = [
    {"text": "Uw bankrekening wordt geblokkeerd. Klik hier om te voorkomen: http://bankveiligheid-login.com", "isPhishing": True},
    {"text": "Uw pakket is onderweg! Track & Trace: PostNL App", "isPhishing": False},
    {"text": "Gefeliciteerd! U heeft een iPhone gewonnen. Klik hier om te claimen.", "isPhishing": True},
    {"text": "Je Apple ID werd gebruikt om in te loggen op een nieuw apparaat.", "isPhishing": False}
]

current_index = 0

def show_email():
    email_text = emails[current_index]["text"]
    document.getElementById("email-text").innerText = email_text
    document.getElementById("feedback").innerText = ""

@when("click", "#real-btn")
def handle_real_click(event):
    check_answer(user_thinks_real=True)

@when("click", "#phishing-btn")
def handle_phishing_click(event):
    check_answer(user_thinks_real=False)

@when("click", "#next-btn")
def next_email(event):
    global current_index
    current_index = (current_index + 1) % len(emails)
    show_email()

def check_answer(user_thinks_real: bool):
    correct_answer = not emails[current_index]["isPhishing"]
    feedback = "✅ Correct!" if user_thinks_real == correct_answer else "❌ Fout!"
    document.getElementById("feedback").innerText = feedback

show_email()
