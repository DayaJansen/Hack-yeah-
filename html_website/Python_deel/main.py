from pyscript import Element

def check_password(*args):
    input_value = Element("dutch").element.value
    output = Element("output")

    if input_value == "123":
        output.write("Goed wachtwoord! 🎉")
    else:
        output.write("Slecht wachtwoord 😢")
__exports__ = ["check_password"]