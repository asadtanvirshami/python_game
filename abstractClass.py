from abc import ABC, abstractmethod;

class Transformer(ABC):
   @abstractmethod
   def Speed():
       pass
 


class Car (Transformer):
        Type = 'Car'
        Distance = int(input("Enter Distance "))
        Time = int(input("Enter Time "))
        
        def Speed(self):
                return print("Type is:",self.Type, "And Speed is:", self.Distance / self.Time )
          
cr = Car()
print(cr.Speed())


class Boat (Transformer):
        Type = 'Boat'
        Distance = int(input("Enter Distance "))
        Time = int(input("Enter Time "))
        
        def Speed(self):
                return print("Type is:",self.Type, "And Speed is:", self.Distance / self.Time )
          
bt = Boat()
print(bt.Speed())

class Plane (Transformer):
        Type = 'Plane'
        Distance = int(input("Enter Distance "))
        Time = int(input("Enter Time "))
        
        def Speed(self):
                return print("Type is:",self.Type, "And Speed is:", self.Distance / self.Time )
          
pl = Plane()
print(pl.Speed())

class Truck (Transformer):
        Type = 'Truck'
        Distance = int(input("Enter Distance "))
        Time = int(input("Enter Time "))
        
        def Speed(self):
                return print("Type is:",self.Type, "And Speed is:", self.Distance / self.Time )
          
tr = Truck()
print(tr.Speed())

class Bike (Transformer):
        Type = 'Bike'
        Distance = int(input("Enter Distance "))
        Time = int(input("Enter Time "))
        
        def Speed(self):
                return print("Type is:",self.Type, "And Speed is:", self.Distance / self.Time )
          
bk = Bike()
print(bk.Speed())

class Bus (Transformer):
        Type = 'Bus'
        Distance = int(input("Enter Distance "))
        Time = int(input("Enter Time "))
        
        def Speed(self):
                return print("Type is:",self.Type, "And Speed is:", self.Distance / self.Time )
          
bs = Bus()
print(bs.Speed())
