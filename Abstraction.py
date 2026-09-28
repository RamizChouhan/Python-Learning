from abc import ABC,abstractmethod


class Pin(ABC):

    @abstractmethod
    def enter():
        pass
       
    @abstractmethod
    def show():
        pass



class UPI(Pin):

    def enter(self):
        self.a = int(input("Enter Your Pin :"))
    
    def show(self,a):
        print("This is Your UPI Pin Code:",self.a)

class PhonePay(Pin):
    
    def enter(self):
        self.a = int(input("Enter Your Pin :"))
    
    def show(self):
        print("This is Your PhonePay Pin Code:",self.a)
        
    def amount(self):
         self.a = int(input("Enter Your Amount :"))
         print("amount :",self.a)



UpiObj =UPI()
UpiObj.enter()
UpiObj.show(12)

phoneObj = PhonePay()
phoneObj.enter()
phoneObj.show()
phoneObj.amount()
