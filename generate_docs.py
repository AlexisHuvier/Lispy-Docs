import glob
import os
import shutil

from lispy_function import LispyFunction
from html_generators import module, index

eval_functions = [
    '@lispy_function("if", ["bool", "code", "code"], "Execute code if bool is true else other code")',
    '@lispy_function("while", ["bool", "code"], "Execute code while bool is true")',
    '@lispy_function("for", ["var", "list", "code"], "Execute code with a variable which get all value from a list.")',
    '@lispy_function("def", ["var", ""], "Define a variable with a value")',
    '@lispy_function("del", ["var"], "Delete a variable")',
    '@lispy_function("func", ["args", "code"], "Create function with arguments and body")',
    '@lispy_function("import", ["module"], "Import python module, lispy module or lipsy file")',
    '@lispy_function("ret", [""], "Return value")'
]

find_functions = {
    "lpygame": "libraries_src/lpygame_src/lispy_functions/**/*"
}

constantes = {
    "core": {
        'none': 'None value', "true": "True value", "false": "False value"
    },
    "math": {
        "math:pi": "PI value", "math:e": "E value", "math:tau": "tau value", "math:inf": "Infinite value", "math:nan": "Not a Number value" 
    },
    "str": {
        "str:asci_letters": "All ascii letters in string", "str:ascii_lowercase": "All ascii lowercase letters in string", "str:ascii_uppercase": "All ascii uppercase letters in string",
        "str:digits": "All digits in string", "str:hexdigits": "All hexadecimal digits in string", "str:octdigits": "All octodecimal digits in string", "str:punctuation": "All punctuations in string",
        "str:printable": "All printables in string", "str:whitespace": "All whitespaces in string"
    }
}

def generate_docs(f, to, core, retour):
    if f.endswith(".py") and "__init__" not in f:
        print("GENERATE DOCS FOR :", f)
        with open(f, "r") as fpy:
            lispyfunctions = [LispyFunction.parse(i.replace("\n", "")) for i in fpy.readlines() if i.startswith("@lispy_function")]
            if "standard" in f:
                for i in eval_functions:
                    lispyfunctions.append(LispyFunction.parse(i))
                for i in lispyfunctions:
                    i.module = "core"
            if len(lispyfunctions) > 0:
                with open("docs/"+to+"/"+lispyfunctions[0].module.replace(":", "_")+".html", "w") as fhtml:
                    fhtml.write(module.parse(lispyfunctions, core, retour, False if "standard" in f else True, (constantes[lispyfunctions[0].module] if lispyfunctions[0].module in constantes.keys() else {})))
                print("DOC GENERATED : "+"docs/"+to+"/"+lispyfunctions[0].module.replace(":", "_")+".html")
                return to+"/"+lispyfunctions[0].module.replace(":", "_")+".html"
            else:
                print("NO LISPY FUNCTIONS")
                return "NLF"
    return ""

def generate_internal_docs(f, to, retour):
    if f.endswith(".py") and "__init__" not in f:
        print("GENERATE INTERNAL DOCS FOR :", f)
        with open(f, "r") as fpy:
            lispyfunctions = [LispyFunction.parse(i.replace("\n", "")) for i in fpy.readlines() if i.startswith("@lispy_function")]
            if len(lispyfunctions) > 0:
                with open("docs/"+to+"/"+lispyfunctions[0].module.replace(":", "_")+".html", "w") as fhtml:
                    fhtml.write(module.parse(lispyfunctions, False, retour, False, constantes[lispyfunctions[0].module] if lispyfunctions[0].module in constantes.keys() else {}))
                print("DOC GENERATED : "+"docs/"+to+"/"+lispyfunctions[0].module.replace(":", "_")+".html")
                return lispyfunctions[0].module.replace(":", "_")+".html"
            else:
                print("NO LISPY FUNCTIONS")
                return "NLF"
    return ""

if os.path.exists("docs"):
    shutil.rmtree("docs")
os.makedirs("docs/lispy_modules")
modules = []
for f in glob.glob("../Lispy/lispy/objects/modules_def/*", recursive=True):
    temp = generate_docs(f, "lispy_modules", True, "../index.html")
    if temp != "":
        modules.append(temp)
    
os.makedirs("docs/python_modules")
for f in glob.glob("../Lispy/libraries/*", recursive=True):
    temp = generate_docs(f, "python_modules", False, "../index.html")
    if temp == "NLF":
        module_ = f.replace("\\", "/").split("/")[-1].replace(".py", "")
        os.makedirs("docs/python_modules/"+module_)
        internal_modules = []
        for nf in glob.glob("../Lispy/"+find_functions[module_], recursive=True):
            temp = generate_internal_docs(nf, "python_modules/"+module_, "index.html")
            if temp != "":
                internal_modules.append(temp)
        if len(internal_modules) > 0:
            with open("docs/python_modules/"+module_+"/index.html", "w") as findex:
                findex.write(index.parse(module_, internal_modules, "../../index.html", "(import python:"+module_+")"))
                print(module_+" INDEX GENERATED")
            modules.append("python_modules/"+module_+"/index.html")
    elif temp != "":
        modules.append(temp)
with open("docs/index.html", "w") as f:
    f.write(index.parse("lispy", modules))
    print("GLOBAL INDEX GENERATED")