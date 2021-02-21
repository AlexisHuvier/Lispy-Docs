def get_name(i):
    if i.split("/")[-1] != "index.html":
        return i.split("/")[-1].replace(".html", "").title()
    else:
        return i.split("/")[-2].title()

def parse(name, modules, module_method = ""):
    with open("templates/index.html", "r") as f:
        temp = f.read()
    replaces = {
        "{{MODULE}}": name.title(),
        "{{IMPORT_METHOD}}": module_method,
        "{{LIST_MODULES}}": "\n            ".join(['<div class="w3-card-2 w3-third w3-margin"><a href="'+i+'" class="w3-button w3-center" style="width:100%">'+get_name(i)+"</a></div>" for i in modules])
    }
    for k,v in replaces.items():
        temp = temp.replace(k, v)
    return temp
