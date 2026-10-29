def factorial_recursive(n): #ვქმნით ფუნქციას ფაქტორიალის რექურსიას
    if n < 0: # თუ ნ ნაკლებია ნულზე
        return "Factorial is not defined for negative numbers." #რეთურნ გვაქვს რომ ფაქტორიალი არ მუშაოვს უარყოფით რიცხვებზე

    if n == 0 or n == 1: # თუ ნ ის მნიშვნელობა დაფიქსირდება 0 ან 1  ფუნქციამ დააბრუნოს 1 და დაასრულოს რეკურსია. base case  ნაპოვნია
        return 1

    return n * factorial_recursive(n - 1)#  მას შემდეგ რაც  n დააბრუნებს 1 ს, დასრულდეს ფუნქცია.

# Test the function
print(factorial_recursive(5))  # Output: 120 
print(factorial_recursive(0))  # Output: 1


def calculate_cart_total(discount_rate, *prices):
    total=0
    for price in prices:
        discount_price=price-(price*discount_rate/100)
        total+=discount_price
    return float(total)

print(calculate_cart_total(21.5,100,200,500))



def filter_and_sor_products(**products):
    filtered=filter(lambda item:item[1]>100,products.items())
    return sorted(filtered,key=lambda item:item[1])

print(filter_and_sor_products(laptpo=500,mouse=2,gela=2030,gia=2020))
from functools import reduce

names = ["Ana", "Nino", "Luka", "Giorgi", "Mariam"]
scores = [45, 82, 91, 38, 74]

def pair_students(names_list, scores_list):
    return list(zip(names_list, scores_list))

print(pair_students(names,scores))

def get_passed_students(paired_data, passing_score=60):
    return list(filter(lambda student: student [1] >= passing_score,paired_data))

passed=pair_students(names,scores)
print(get_passed_students(passed))

def calculate_average_of_passed(passed_students):
    return list(map(lambda student:student[1],passed_students))

print(calculate_average_of_passed(passed))

scores_total=calculate_average_of_passed(passed)
total=reduce(lambda a,b:a+b,scores_total)
total_avarage=total/len(scores_total)
print(total_avarage)
from functools import reduce
products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Cable"]
quantities = [5, 0, 12, 3, 0]

def sia_produqtebis(products_list, quantities_list):
    return list(zip(products_list, quantities_list))

list_products=(sia_produqtebis(products,quantities))
print(list_products)

def check_in_stock(arsebulistock, min_quantity=1):
    return list(filter(lambda products:products[1]>= min_quantity,list_products))
    
check=check_in_stock(list_products,min_quantity=1)
print(check)

def  calculate_total_items(in_stock_data):
    qty=list(map(lambda count:count[1],list_products))
    return  reduce(lambda a,b:a+b,qty)

total=calculate_total_items(list_products)
print(total)
