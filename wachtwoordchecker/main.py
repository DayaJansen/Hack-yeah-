import js
from pyscript import display, when

@when("click", "#check-btn")
def check_password(event):
    input_value = js.document.getElementById("dutch").value
    output_div = js.document.getElementById("output")

    if input_value == "123":
        output_div.innerText = "Goed wachtwoord! 🎉"
    else:
        output_div.innerText = "Slecht wachtwoord 😢"