from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while(True):
    order=input(f"What would you like? {menu.get_items()}:")
    if(order=="off"):
        break
    if(order=='report'):
        coffee_maker.report()
    else:
        pesanan=(menu.find_drink(order))
        if(pesanan!=None):
            if(coffee_maker.is_resource_sufficient(pesanan)):
                if(money_machine.make_payment(pesanan.cost)):
                    coffee_maker.make_coffee(pesanan)

