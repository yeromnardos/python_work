class fruits:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sale(self):
        print(f"I like eating {self.name} and it costs Ksh {self.price} ")


rlobj = fruits("straberry", "200")
rlobj.sale()
rlobj = fruits("banana", "100")
rlobj.sale()
rlobj = fruits("mango", "105")
rlobj.sale()
rlobj = fruits("orange", "180")
rlobj.sale()
rlobj = fruits("berry", "300")
rlobj.sale()
