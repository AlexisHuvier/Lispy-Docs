def parse(lispy_function):
    with open("templates/function.html", "r") as f:
        temp = f.read()
    replaces = {
        "{{NAME}}": lispy_function.fullname(),
        "{{EXPLAINATION}}": lispy_function.explaination,
        "{{PARAMS}}": "Parameters :<br/>"+"<br/>\n".join(lispy_function.params),
    }
    for k,v in replaces.items():
        temp = temp.replace(k, v)
    return temp