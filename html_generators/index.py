def get_name(i):
    if i.split("/")[-1] != "index.html":
        name = i.split("/")[-1].replace(".html", "").replace("_", " ").title()
    else:
        name = i.split("/")[-2].replace("_", " ").title()
    if len(name.split(" ")) > 1:
        return " ".join(name.split(" ")[1:])
    else:
        return name

def parse(name, modules, retour="", module_method = ""):
    with open("templates/index.html", "r") as f:
        temp = f.read()
    replaces = {
        "{{RETURN}}": '<a href="'+retour+'" class="w3-button w3-border w3-cyan w3-margin">Back</a>' if retour != "" else "", 
        "{{MODULE}}": name.title(),
        "{{IMPORT_METHOD}}": module_method,
        "{{LIST_MODULES}}": "\n            ".join(['<div class="w3-card-2 w3-third w3-margin"><a href="'+i+'" class="w3-button w3-center" style="width:100%">'+get_name(i)+"</a></div>" for i in modules])
    }
    for k,v in replaces.items():
        temp = temp.replace(k, v)
    return temp
