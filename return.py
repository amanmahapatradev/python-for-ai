def add_print(a,b):
    print(a+b)
    
print_result = add_print(5,6)
print(print_result)

def add_return(a ,b):
    return a + b

result = add_return( 5 , 6)
print(result)

def calc_area( w , h):
    area = w * h
    return area

room_area = calc_area(10,12)
print(f"Room size : {room_area} sq ft")

def double(num):
    return num * 2

result = double(5)

total = double(5) + double(3)

print(double(10))

if double(7) > 10 :
    print("Bigger number")
    


def simple_function():
    numbers = [1,2,3,4,5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number , last_number

f , l = simple_function()

print(f)
print(l)

