from html_generators import function

def parse(lispy_functions, core, show_method=True):
    with open("templates/module.html", "r") as f:
        temp = f.read()
    replaces = {
        "{{MODULE}}": lispy_functions[0].module.title(),
        "{{IMPORT_METHOD}}": "(import "+ ("python:" if not core else "") + lispy_functions[0].module + ")" if show_method else "",
        "{{FUNCTIONS}}": "\n            ".join([function.parse(i) for i in lispy_functions]),
        "{{MENU}}": "\n            ".join(['<a href="#'+i.fullname()+'" class="w3-bar-item w3-button">'+i.fullname()+"</a>" for i in lispy_functions])
    }
    for k,v in replaces.items():
        temp = temp.replace(k, v)
    return temp