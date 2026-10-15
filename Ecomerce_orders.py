cart_total=0
user_status='VIP'
has_promo_code=True
loyalty_points=600
delivery_city='Tbilisi'
is_account_active=True
current_status='Blocked'

#ვალიდაცია
if is_account_active== False:
    print(f'Account is {current_status}')
elif cart_total<= 0:
    print('cart is empty')
else:
    user_status=input('choose your status\n').title().strip()
    if user_status=='VIP':
        discount = 20
        if loyalty_points>=500:
            discount= 25
        elif user_status=='Regular':
            if has_promo_code==True or cart_total>=150:
                discount = 10
            else:
                discount= 0
    elif user_status=='Admin':
        discount= 50
    else:
        discount=0

    discounted=cart_total*(1-discount/100)
    mylist_city=['Tbilisi','Batumi','kutaisi']


    if delivery_city in mylist_city:
        if cart_total>=100:
            delivery_cost=0
        else:
            delivery_cost=5
    else:
        delivery_cost=15

    print                             ('საბოლოო ფასი')
    print(f'საწყისი თანხა იყო {cart_total} ლარი')
    print(f'ფასდაკლება არის {discount} %')
    print(f'საკურიორო მომსახურეობა არის {delivery_cost} ლარი')
    print(f'გადასახდელი გაქვთ {discounted} ლარი')

    







    


    


    











        


    
        
        
        
        
        
        
        
        