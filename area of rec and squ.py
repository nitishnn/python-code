#wscube Area of rectangle and square by using method overloading
class Area:
    def Find_area(self, a=None, b=None):
        if a is not None and b is not None:
            print("Area of rectangle:",a*b)
        elif a is not None:
            print("Area of square:",a*a)
        
a1 = Area()
a1.Find_area(3,5)
a1.Find_area(3)
            
