MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resource={
    "water":200,
    "coffee":500,
    "milk":500,
    "money":0
}

def checkBarang(pesanan):
    for a in pesanan["ingredients"]:
        if(resource[a]<pesanan["ingredients"][a]):
            print("the ingredient to make this coffee not enoght Sorry")
            return False
    return True
def makeOrder(pesanan):
    for a in pesanan['ingredients']:
        resource[a]-=pesanan["ingredients"][a]
    print("Enjoy your coffee")

def payment(pesanan):
    quarter=int(input("How Many quarters ?:"))
    dimes=int(input("How Many dimes ?:"))
    nicklets=int(input("How Many nicklets ?:"))
    penny=int(input("How Many pennies ?:"))
    total=quarter*0.25+dimes*0.10+nicklets*0.05+penny*0.01
    if(total<pesanan['cost']):
        print("Your monney not enough")
        return False
    else:
        resource['money']+=float(pesanan['cost'])
        print(f"Heres your charge {total-pesanan['cost']}")
        return True
    
while(True):
    order=input("What would you like? (espresso/latte/cappuccino):")
    if(order=="off"):
        break
    if(order=='report'):
        print(f"water :{resource['water']}")
        print(f"coffee :{resource['coffee']}")
        print(f"milk :{resource['milk']}")
        print(f"money :{resource['money']}")
    else:
        pesanan=MENU[order]
        if(checkBarang(pesanan)):
            if(payment(pesanan)):
                makeOrder(pesanan)

        else:
            order=input("What would you like? (espresso/latte/cappuccino):")
            
