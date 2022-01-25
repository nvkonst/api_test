class JsTestTask:
    def __init__(self, name=None, image=None, price=None):
        self.name = name
        self.image = image
        self.price = price

    def __repr__(self):
        return f"{self.name}:{self.image}:{self.price}"

    def __eq__(self, other):
        return self.name == other.name and self.image == other.image and self.price == other.price
