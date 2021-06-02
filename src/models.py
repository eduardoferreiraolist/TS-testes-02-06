class Category:
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name + ", " + self.description


class Product:
    def __init__(self, name="", value=0, description=""):
        self.name = name
        self.value = value
        self.description = description

    def __str__(self):
        return self.name + ", " + str(self.value) + ", " + self.description
