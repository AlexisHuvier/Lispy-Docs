from html_generators import function, constantes

def module_name(name):
    if len(name.split(":")) > 1:
        return " ".join(name.split(":")[1:])
    else:
        return name

def parse(lispy_functions, core, retour, show_method=True, constants={}):
    with open("templates/module.html", "r") as f:
        temp = f.read()

    menus_items = ['<a href="#'+i.fullname()+'" class="w3-bar-item w3-button w3-margin">'+i.fullname()+"</a>" for i in lispy_functions]
    if len(constants.keys()) > 0:
        menus_items.append('<a href="#constantes" class="w3-bar-item w3-button w3-margin">Constantes</a>')

    replaces = {
        "{{MODULE}}": module_name(lispy_functions[0].module.title()),
        "{{IMPORT_METHOD}}": "(import "+ ("python:" if not core else "") + lispy_functions[0].module + ")" if show_method else "",
        "{{FUNCTIONS}}": "\n            ".join([function.parse(i) for i in lispy_functions]),
        "{{MENU}}": "\n            ".join(menus_items),
        "{{CONSTANTES}}": constantes.parse(constants),
        "{{RETURN}}": retour
    }
    for k,v in replaces.items():
        temp = temp.replace(k, v)
    return temp