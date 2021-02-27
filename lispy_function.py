def lispy_function(name="", arguments=[], explaination="", must_async=False):
    return name, arguments, explaination

class LispyFunction:
    def __init__(self, module, name, params, explaination):
        self.module = module
        self.name = name
        if len(params):
            for i in range(len(params)):
                if params[i] == "":
                    params[i] = f"{i+1}: Any Type"
                else:
                    params[i] = f"{i+1}: " + ", ".join([i.capitalize() for i in params[i].split("|")])
        else:
            params = ["No parameters."]
        self.explaination = explaination
        self.params = params

    def fullname(self):
        if self.module == "" or self.module == "core":
            return self.name
        else:
            return self.module + ":" + self.name

    def __str__(self):
        return "LF(module = "+str(self.module)+", name = "+str(self.name)+", params = "+str(self.params)+", explaination = "+str(self.explaination)+ ")"
    
    @classmethod
    def parse(cls, text):
        func = eval(text[1:])
        if ":" in func[0]:
            module = ":".join(func[0].split(":")[:-1])
            name = func[0].split(":")[-1]
        else:
            module = ""
            name = func[0]
        return LispyFunction(module, name, func[1], func[2])