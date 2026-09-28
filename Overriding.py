'''class Parent:
    def Work(self):
        print("Employee is working")



class Developer(Parent):
    
    def Work(self):
        super().Work()
        print("Developer is writing code")




class Designer(Parent):
    def Work(self):
        print("Designer is creating designs")



developerObj = Developer()
DesignerObj = Designer()

developerObj.Work()
DesignerObj.Work()'''


'''class Payment:
    def pay(self):
        print("Processing payment...")



class UpiPayment(Payment):
    def pay(self):
        super().pay()
        print("Payment done through UPI")



class CardPayment(Payment):
    def pay(self):
        super().pay()
        print("Payment done through Card")


UpiObj = UpiPayment()
CardObj = CardPayment()


UpiObj.pay()
CardObj.pay()'''


class Order:
    def confirm_order(self):
        print("Order confirmed")
        

class OnlineOrder(Order):
    def confirm_order(self):
        super().confirm_order()
        print("Online payment verified")


class CashOnDelivery(Order):
    def confirm_order(self):
        super().confirm_order()
        print("Cash on Delivery selected")



OnlineOrderObj = OnlineOrder()
CashOnDeliveryObj = CashOnDelivery()


OnlineOrderObj.confirm_order()
CashOnDeliveryObj.confirm_order()
