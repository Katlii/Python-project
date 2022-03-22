class Rect:
    """ Trida k evidenci obdelniku """
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2=x2
        self.y2=y2

    def __repr__(self):
        """vytvoří řetězcovou reprezentaci ve tvaru Rect(x1,y1,x2,y2)."""
        return f'Rect({self.x1},{self.y1},{self.x2},{self.y2})'

    def perimeter(self):
        """vrací obvod obdélníka"""
        perimetr=2*((self.x2-self.x1)+(self.y2-self.y1))
        return perimetr

    def area(self):
        """ vrací obsah obdélníka"""
        obsah=((self.x2-self.x1)*(self.y2-self.y1))
        return obsah

    def __eq__(self, other):
        """zjistí, zda jsou dva obdélníky totožné (mají stejné vrcholy).
         Vrací False nebo True.
         Implementuje operátor == (Python automaticky doplní != jako negaci ==).
         """
        return self.x1 == other.x1 and self.x2==other.x2 and self.y1==other.y1 and self.y2==other.y2

    def __contains__(self, other):
        """zjistí, zda jeden obdélník other obsažen neostře uvnitř obdélníka self. Vrací False nebo True.
           Implementuje operátor other in self
           (Python automaticky doplní not in jako negaci in)."""
        return other.area()<=self.area() and self.x1<=other.x1 and self.x2>=other.x2 and self.y1<=other.y1 and self.y2>=other.y2

    def __and__(self, other):
        """spočítá průnik dvou obdélníků, vrací opět obdélník. Implementuje operátor &. Pokud je průnik prázdný, """
                
        if other in self: return other
        elif self in other: return self
        if other.y1<=self.y1: other.y1=self.y1
        if other.y2>=self.y2: other.y2=self.y2
        if other.x1<=self.x1: other.x1=self.x1
        if other.x2>=self.x2: other.x2=self.x2
        if other.x1<other.x2 and other.y1<other.y2 :
            return other
        else:
            return Rect(0,0,0,0)

obdelnik=Rect(1, 2, 3, 5)
obdelnik2=Rect(1, 0, 3, 2)
print(obdelnik, obdelnik2)
print(obdelnik.perimeter())
print(obdelnik.area())
print(obdelnik==obdelnik2)
print(obdelnik2 in obdelnik)
print(obdelnik & obdelnik2)









