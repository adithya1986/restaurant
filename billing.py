class Billing:
    def __init__(self,item_name,quantity,price):
        self.item_name=item_name
        self.quantity=quantity
        self.price=price
        
    def calculate_bill_amount(self):
        self.total=self.quantity*self.price

item_price={'Meal':80,'Briyani':120,'FriedRice':130,'Noodles':140}
bill=Billing()