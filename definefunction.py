def greet():
    print("Hello !")
    pass

greet()

def check_whether():
    temprature = 16
    if temprature > 25:
        print("It's hot")
    else:
        print("It's nice weather !")    
        
check_whether()

def greet(first_name , last_name):
    print(f"Hello , {first_name} {last_name}")
    
greet("Aman","Shankar")


def calculate_total(price , tax_rate , discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total : ${final_price}")
calculate_total(100 , 0.08 ,10 )

