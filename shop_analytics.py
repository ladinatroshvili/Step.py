inventory={
    'Laptop': {"price": 1500, "quantity": 10,'color': "black"},
    'mouse': {"price": 20, "quantity": 0,'color': "white"},
    'keyboard': {"price": 50, "quantity": 300,'color': "yellow"},
}

print('============================')
print("ონლაინ მაღაზიის ინვენტარი")
print('=============================')



while True:
    Answer=input("პროდუქტის დამატება, ADD,რაოდენიბის stock ან დააჭირეთ stop-s რათა ნახოთ მიმდინარე სია").lower()

    if Answer=="stop":
        print(inventory)
        break
    elif Answer=="add":
        product=input("შეიყვანეთ პროდუქტის სახელი: ")
        try:
            price=int(input("შეიყვანეთ პროდუქტის ფასი: "))
            quantity=int(input("შეიყვანეთ პროდუქტის რაოდენობა: "))
        except ValueError:
            print("შეიყვანეთ სწორი მონაცემები")
            continue
        color=input("შეიყვანეთ პროდუქტის ფერი: ")
        if color.isdigit():
            print("შეიყვანეთ სწორი მონაცემები, ფერის სახელი არ უნდა შეიცავდეს ციფრებს")
            continue
        new_inventori=inventory[product]={"price": price, "quantity": quantity, "color": color}
        print(f'პროდუქტი {product} დამატებულია ინვენტარში')
        continue
        
    elif Answer=="stock":
        product=input("შეიყვანეთ პროდუქტის სახელი: ")
        for product in inventory:
            print(product)
        try:
            if product in inventory:
                quantity=int(input("შეიყვანეთ პროდუქტის რაოდენობა: "))
        except ValueError:
            print("შეიყვანეთ სწორი მონაცემები")
            continue
        inventory[product]["quantity"] = quantity
        print(f"{product}-ის ახალი რაოდენობაა: {inventory[product]['quantity']}")
        print(f"იხილეთ განახლებული ინვენტარი: {inventory}")
            
    else:
        print(f'პროდუქტი {product} არ არის ჩამოთვლილ სიაში')
        print('შეიყვანეთ პროდუქტის სახელი რომელიც არის ჩამოთვლილ სიაში: ', product)
        
inventory_expensive=0
max_price=0

for product, details in inventory.items():
    if details['quantity'] > 0:
        print(f'პროდუქტების ჩამონათვალი რომელიც ნაშთშია: {product}, ფასი: {details["price"]}, რაოდენობა: {details["quantity"]}, ფერი: {details["color"]}')
        
        if details['price']> max_price:
            max_price=details['price']
            max_product=product


print(f'ყველაზე  ძვირადღირებულების პროდუქტი: {max_product.capitalize()}, ფასი: {max_price}')





active_user={"ladi", "gio","dato", "mari","nino", "tako"}
vip_user={"Tako", 'gia',"nino",'lizi'}


inter=active_user.intersection(vip_user)

print(f'მომხმარებლები რომლებიც არიან ჩვეულებრივი  იუზერებიც და VIP ებიც:\n{inter}')

union=active_user.union(vip_user)
print(f'მომხმარებლები რომლებიც არიან რეგისტრირებული ბაზაში:\n {union}')

difference=active_user.difference(vip_user)
print(f'მომხმარებლები რომლებიც არიან იუზერები და არ არიან VIP ები: \n{difference}')

              
