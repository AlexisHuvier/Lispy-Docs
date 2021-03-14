def parse(lispy_function):
    with open("templates/function.html", "r") as f:
        temp = f.read()
    if len(lispy_function.params) > 1:
        param = "Parameters :<br/>"
    elif lispy_function.params[0] == "No parameters":
        param = ""
    else:
        param = "Parameter : "
    replaces = {
        "{{NAME}}": lispy_function.fullname(),
        "{{EXPLAINATION}}": lispy_function.explaination,
        "{{PARAMS}}": param+"<br/>\n".join(lispy_function.params),
    }
    for k,v in replaces.items():
        temp = temp.replace(k, v)
    return temp