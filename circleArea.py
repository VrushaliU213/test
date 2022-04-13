class circle:
    PI=3.14
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return circle.PI*self.rad*self.rad
C=circle(7)
print("Area=",C.area())


