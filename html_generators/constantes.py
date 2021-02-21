def parse(constantes):
    with open("templates/constantes.html", "r") as f:
        temp = f.read()
    replaces = {
        "{{CONSTANTES}}": "\n        ".join([k+": "+v+"<br/>" for k, v in constantes.items()]),
    }
    for k,v in replaces.items():
        temp = temp.replace(k, v)
    return temp