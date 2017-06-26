restaurant={
    'pizza hut':{
        'owner':"vishwarupa",
        'rating':"A",
        'foods':{
            'pizza':150,
            'garlic bread':70,
            'colddrink':50
        }
    },
    'kfc':{
        'owner':'basak',
        'rating':'B',
        'foods':{
            'chicken popcorn':100,
            'rice chicken':50,
            'krushers':90
        }
    },

    'bikaner':{
        'owner':'mr rest',
        'rating':'C',
        'foods':{
            'noodles':100,
            'lemonade':50,
            'pastry':200
        }
    }
}
def calculate_bill(price):
    final_price=(0.06*price)+(0.1*price)+(0.15*price)+price
    return final_price


print "Welcome to vishwa's food-booking!"

user_type=int(raw_input("Please tell if you are 1-Restaurant owner or \n 2.Customer? "))
if user_type == 1:
    print "selected type is owner"
    to_update=int(raw_input("what do you wish to do?\n1.Add item? \n2.Update food price"))
    if to_update ==1:
        rest_name_update_food=raw_input("Enter the name of the restaurant for you wish to update")
        for rest_names in restaurant.keys():
            if rest_name_update_food == rest_names:
                item_to_Add=raw_input("what item do you wish to add?")
                item_price=int(raw_input("what is the new item's price?"))
                restaurant[rest_names]['foods'][item_to_Add]=item_price
                print restaurant[rest_names]
    elif to_update ==2:
        rest_name_update_food = raw_input("Enter the name of the restaurant for you wish to update")
        for rest_names in restaurant.keys():
            if rest_name_update_food == rest_names:
                update_food = raw_input("Enter the food for you wish to update")
                updated_price=int(raw_input("what is the item's new price?"))
                restaurant[rest_names]['foods'][update_food] = updated_price
                print "new price for %s has been changed to %i"%(update_food,updated_price)
                print restaurant[rest_names]
elif user_type ==2:
    print "selected type is customer"
    print "available restaurants %s"%(restaurant.keys())
    print "food at pizza hut-",restaurant['pizza hut']['foods']
    print "food at kfc-", restaurant['kfc']['foods']
    print "food at bikaner-", restaurant['bikaner']['foods']
    choice=True
    while choice==True:
        customer_choice=int(raw_input("Enter 1.order food \n2.rate a restaurant \n3.QUIT"))
        if customer_choice==1:
            rest_name_food_order = raw_input("Enter the name of the restaurant for you wish to order")
            if rest_name_food_order in restaurant.keys():
                #if rest_name_food_order == rest_names:
                    order_food = raw_input("Enter the food for you wish to order")
                    if order_food in restaurant[rest_name_food_order]['foods'].keys():
                        order_price=restaurant[rest_name_food_order]['foods'][order_food]
                        print "price", order_price
                        print "order successful"
                        choice_get_food = int(raw_input("How do you wish to receive your order? 1.Walk-in \n2.Take Away"))
                        if choice_get_food == 1:
                            print "Walk-In chosen"
                            bill=calculate_bill(order_price)
                            print "your required payment is",bill
                        elif choice_get_food == 2:
                            print "Take-away chosen"
                            bill = calculate_bill(order_price)
                            print "your required payment is", bill
                        else:
                            print "Invalid option."
                    else:
                        print "order unsuccessful,order again please!"
            else:
                print "Invalide restaurant name"

        elif customer_choice==2:
            rest_name_update_rate = raw_input("Enter the name of the restaurant for you wish to change status for.Status can be from A-D ie from excellent to poor.")
            if rest_name_update_rate in restaurant.keys():
                #if rest_name_update_rate == rest_names:
                    rest_rate=raw_input("Enter the status for the Restaurant")
                    restaurant[rest_name_update_rate]['rating']=rest_rate
                    print "New rate for %s is %s"%(rest_name_update_rate,rest_rate)
                    print restaurant
            else:
                print "Invalide restaurant name"

        elif customer_choice== 3:
            print "Thankyou for visiting!"
            break





