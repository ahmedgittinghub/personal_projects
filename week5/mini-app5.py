from python_packages5 import * 
from sql_packages import * 

import pymysql
import os
from dotenv import load_dotenv

connection, cursor = setup_db_connection()




# LOAD orders from orders.csv
orders_list = []
open_csv_orders('orders.csv',orders_list)

# CREATE order status list
order_status_list = ['starting','preparing','completed']


# PRINT main menu options
menu_options = [' Save & Exit app', 'Products Menu', 'Couriers Menu','Orders Menu']
# GET user input for main menu option
user_input = ''
cafe_open = True
while  cafe_open == True and user_input not in ['0','1','2','3']:
    enumerated_list(menu_options)

    user_input = input('please insert a number from 0,1,2,3: ')
    print('')
# IF user input is 0:
    if user_input == '0':
        #  SAVE orders list to order.csv
         close_csv_orders('orders.csv', orders_list)
        #  EXIT app
         os.system('clear')
         cafe_open = False


# # products menu
# ELSE IF user input is 1:
    elif user_input == '1':
        open_menu = True
        #PRINT product menu options
        menu_options1 = ['Return to main menu','Print product list','Create a new product','Update existing product','Delete existing product']
        enumerated_list(menu_options)
        user_input1 = ''
        os.system('clear')
        print('welcome to the products menu')
        print('\n')
    
#     GET user input for product menu option
        while  open_menu == True and user_input1 not in ['0','1','2','3','4']:
            
            enumerated_list(menu_options1)
            user_input1 = input('please insert a choice from 0,1,2,3,4:  ')

#     IF user inputs 0:
            if user_input1 == '0':
               #RETURN to main menu
                
                user_input = ''
                open_menu = False
                os.system('clear')
                print('Going back to Main menu')

#     # WEEK 5 UPDATE
#     ELSE IF user input is 1:
            elif user_input1 == '1':
                 print('\n')
                 os.system('clear')
                 # PRINT products list
                 table_printer(table_name='products')
                 
                 user_input1 = ''


#     # WEEK 5 UPDATE
#     ELSE IF user input is 2:
            elif user_input1 == '2':
                 os.system('clear')
                 check_name = ''

                 dict1 = {"product_name": "0", "product_price": "0"}
                 table_printer(table_name='products')

                # GET user input for product name
                 while dict1["product_name"] == "0" :
                    # here user is asked for name insert
                    print('please insert the correct product name')
                    dict1["product_name"] = name_insert(dict1["product_name"])
                    # resets if left empty, so a name is inserted for the product
                    if dict1["product_name"].strip() == '':
                        dict1["product_name"] = "0"
                    else:
                        #  check to ensure the new product being added isnt a duplicate
                        check_name = product_name_check(dict1["product_name"], check_name)
                        #  resets if product name already exist
                        if check_name == 'yes':
                            dict1['product_name'] = '0'
                        #  doesnt reset if product name exists
                        elif check_name == 'no':
                            break
                 

                 
                # GET user input for product price
                 while dict1["product_price"] == "0" :
                    dict1["product_price"] = price_insert(dict1["product_price"])
                    # price must be a float value, so that the field is not left empty
                    if type(dict1["product_price"]) != float:
                        dict1["product_price"] = "0"
                        print('please insert a valid input for price')
                    else:
                        # once a name and a price are obtained the new product is added 
                        add_product(dict1["product_name"], dict1["product_price"])
                
                 user_input1 = ''



#     # WEEK 5 UPDATE
#     ELSE IF user input is 3:
            elif user_input1 == '3':
                os.system('clear')

                dict13 = {"product_name": "0", "product_price": "0"}
                #PRINT products with their IDs
                table_printer(table_name = 'products')
                
                id_number = '$'
                checker = ''
                name_checker = ''
                #GET user input for product ID
               
                while id_number == '$' :
                    id_number , checker = id_number_check_products_table(id_number,checker)
                    # if user id doesnt exist the loop will resets and ask for id insert
                    if checker == 'no':
                        id_number = '$'

                # if the insert is left empty the code ends as the user doesnt desire to change anything
                if checker == 'no change':
                    print('No change desired going back to main menu')
                    
                # this if stament is activated when a correct courier ID is inserted
                elif checker == 'yes':
                    print('Id number exist Please fill in the following fields or leave empty if you dont  want to make a change')

                    #GET user input for product name
                    while dict13["product_name"] == "0":
                        # the user is asked for a new product name to alter existing product
                        print('please insert the new name')
                        dict13["product_name"] = name_insert(dict13["product_name"])

                        #if name insert is left empty no name taken and product name will be left the same
                        if dict13["product_name"].strip() == '':
                            print("product will not be changed")
                            break

                        #if the name insert is not left empty this elif statment is activated
                        elif dict13["product_name"].strip() != '':
                            name_checker = product_name_check(dict13["product_name"], name_checker)
                            # this checks if the product name already exists
                            if name_checker == 'yes':
                                # if the name is in the products table, name insert resets
                                dict13['product_name'] = '0'
                                # if the name doesnt exist product name is updated
                            elif name_checker == 'no':
                                product_name_change(id_number,dict13['product_name'])


                    #GET user input for product price
                    while dict13["product_price"] == "0":
                        # the users are asked for a price 
                        dict13["product_price"] = price_insert(dict13["product_price"])

                        # if the price is inserted correctly in float form the price of the product is updated
                        if type(dict13["product_price"]) == float :
                            product_price_change(id_number,dict13['product_price'])
                            break
                    #IF any inputs are empty, do not update them
                        elif dict13["product_price"].strip() == '':
                            print("product price will not be changed")
                            break
                        #IF input is incorrect sush as letters the code will reset and ask user for price
                        elif dict13["product_price"].strip() != '' and type(dict13["product_price"]) != float:
                            print('please insert a vlid input for the price ')
                            dict13["product_price"] == "0"

                user_input1 = ''
            


#     # WEEK 5 UPDATE
#     ELSE IF user input is 4:
            elif user_input1 == '4':
                os.system('clear')
                #PRINT products with their IDs
                table_printer(table_name='products')
                id_number = '$'
                checker = ''
                #GET user input for product ID
                while id_number == '$' :
                    id_number , checker = id_number_check_products_table(id_number,checker)
                    if checker == 'no':
                        id_number = '$'

                # If no Id is inserted no product is deleted 
                if checker == 'no change':
                    print('NO ENTRY WAS TAKEN GOING BACK TO MAIN MENU')
                    
                elif checker == 'yes':
                    # DELETE product in products table
                    delete_product(id_number)               
                user_input1 = ''
#         # STRETCH GOAL - DELETE product
        

    elif user_input == '2':
        os.system('clear')
        
        print('welcome to couries menu')
        
        #   open_couries_menu = True
        open_couries_menu = True

        #PRINT couries menu options
        menu_options2 = ['Return to main menu','Print courie list','Create a new courie','Update existing courie','Delete existing courie']
        

        user_input2 = ''

        #GET user input for product menu option
        while  open_couries_menu == True and user_input2 not in ['0','1','2','3','4']:
            enumerated_list(menu_options2)
            user_input2 = input('please insert a choice from 0,1,2,3,4:  ')

            if user_input2 == '0' :
                
               #RETURN to main menu
               print('returning to main menu')

               
               user_input = ''

               os.system('clear')
               open_couries_menu = False
            


            elif user_input2 == '1':
                #GET all couriers from couriers table
                #PRINT couriers
                print('\n')
                os.system('clear')
                table_printer(table_name='couriers')
                
                user_input2 = ''

            # CREATE new courier
            elif user_input2 == '2':
                os.system('clear')
                dict22 = {"name": "0","phone_number":"0"}
                checker = ''

                # GET user input for courier name
                while dict22["name"] == "0":
                    print('please insert the courier name you wish to add to this new courier')
                    dict22["name"] = name_insert(dict22["name"])
                    if dict22["name"].strip() == '':
                        dict22["name"] = "0"
                    else:
                        break

                # GET user input for courier phone number
                while dict22["phone_number"] == '0':
                    dict22["phone_number"] = phone_number_insert(dict22["phone_number"])
                    if dict22["phone_number"].replace(' ','').isdigit() == False:
                         dict22["phone_number"] = '0'
                    else:
                        checker = courier_phone_check(dict22['phone_number'],checker)
                        if checker == 'yes':
                            dict22['phone_number'] = '0'
                        elif checker == 'no':
                            #INSERT courier into couriers table  
                            add_courier(dict22['name'],dict22['phone_number'])
                            break
                 
                user_input2 = ''  

            elif user_input2 == '3':
                dict23 = {"name": "0","phone_number":"0"}
                os.system('clear')
                id_number = '$'
                checker = ''
                phone_number_checker = '' 

                table_printer(table_name='couriers')

                #GET user input for courier ID
                # retrieve courier Id then check if the ID number exists
                while id_number == '$' :
                    id_number , checker = id_number_check_couriers_table(id_number,checker)
                    #  if the Id inserted doesnt exist loop resets and ask for a another insert
                    if checker == 'no':
                        id_number = '$'
                # if no insert is added code breaks and goes back to main menu
                if checker == 'no change':
                    print('No change desired going back to main menu')
                    

                elif checker == 'yes':
                    print('Id number exist Please fill in the following fields or leave empty if you dont  want to make a change')
                    
                    #GET user input for courier name
                    while dict23['name'] == "0":
                        print('please insert the courier name you wish to change to')
                        dict23["name"] = name_insert(dict23["name"])
                        # if the user left the insert empty name doesnt change
                        if dict23["name"].strip() == '':
                            print("product will not be changed")
                            break
                        elif dict23["name"].strip() != '':
                            # ensures names are inserted in the correct format
                            if dict23['name'].replace(' ','').isalpha() == False:
                                print('Please insert a valid name with just letters')
                                # resets if incorrect input is added
                                dict23['name'] = '0'
                            else: 
                                print('Name will be changed')
                                #Courier name update
                                courier_name_change(id_number,dict23['name'])

                    
                    #GET user input for courier phone number
                    while dict23['phone_number'] == "0":
                        dict23['phone_number'] = phone_number_insert(dict23['phone_number'])
                        if dict23["phone_number"].strip() == '':
                            print("Phone Number will not be changed")
                            break
                        elif dict23["phone_number"].strip() != '':
                            # function checks if the phone number exists
                            phone_number_checker = courier_phone_check(dict23['phone_number'], phone_number_checker)
                            if phone_number_checker == 'yes':
                                # this ensures users don't insert a phone number already in the database
                                dict23["phone_number"] = '0'
                            elif phone_number_checker == 'no':
                                # command that alters the phone number
                                phone_number_change(id_number, dict23['phone_number'])
 
                user_input2 = ''       

            elif user_input2 == '4':
                os.system('clear')
                #PRINT products with their IDs
                table_printer(table_name='couriers')
                id_number = '$'
                checker = ''
                #GET user input for product ID
                while id_number == '$' :
                    # if id number inserted doesnt exist or input is incorrect the insert resets
                    id_number , checker = id_number_check_couriers_table(id_number,checker)
                    if checker == 'no':
                        id_number = '$'
                
                # if no id inserted, code breaks .
                if checker == 'no change':
                    print('NO ENTRY WAS TAKEN GOING BACK TO MAIN MENU')
                    
                elif checker == 'yes':
                    # DELETE courier with the id 
                    delete_courier(id_number)               
                

                user_input2 = ''   


    # ELSE IF user input is 3:
    elif user_input == '3':
        
        print('welcome to orders menue')

        open_orders_menu = True
        menu_options3 = ['Main Menu',' View Orders Dictionary','New order Input',' Update existing order status','update existing order details',' delete product']

        user_input3 = ''

        while  open_orders_menu == True and user_input3 not in ['0','1','2','3','4','5']:
            enumerated_list(menu_options3)
            user_input3 = input('please insert a choice from 0,1,2,3,4,5:  ')

            
            # IF user input is 0:
            if user_input3 == '0' :
               
                
               #RETURN to main menu
               print('returning to main menu')

               
               user_input = ''
               
               open_couries_menu = False
               os.system('clear')


             # ELSE IF user input is 1:
            elif user_input3 == '1':
                 print('\n')
                 os.system('clear')
                 # PRINT orders list
                 orders_table_printer()
                 user_input3 = ''



            # ELSE IF user input is 2:
            elif user_input3 == '2':
               os.system('clear')

               order_name = '0'
               order_address = '0'
               order_postcode = '0'
               order_city = '0'
               order_country = '0'
               order_phone_number = '0'
               order_courier_id = '$'
               status_id = '0'
               order_items = []

               
               
               # order name
               order_name = '0'
               while order_name == '0':
                    print('please insert the name you wish to assign the order to')
                    order_name = name_insert(order_name)
                    if order_name.replace(' ','').isalpha() == False: 
                        order_name = '0'
                    else:
                         break
          
              # order address
               while order_address == '0':
                    order_address = address_fucntion(order_address)
                    if order_address == '!':
                        print("Please insert a valid input for the address.")
                        order_address = '0'
                    elif order_address == '' :
                        print('cant leave this empty')
                        order_address = '0'
                    else:
                        print('thank you address inserted correctly')
                        break

                # order postcode
               while order_postcode == '0':
                    order_postcode = postcode_function(order_postcode)
                    if order_postcode == '!':
                        print("Please insert a valid input for the POSTCODE.")
                        order_postcode = '0'
                    elif order_postcode == '' :
                        print('cant leave this empty')
                        order_postcode = '0'
                    else:
                        print('thank you postcode inserted correctly')
                        break
               print(order_postcode)
                
                # order City
               while order_city == '0':
                    print('please onsert the city to which the order will be sent to')
                    order_city = name_insert(order_city)
                    if order_city.replace(' ','').isalpha() == False: 
                        order_city = '0'
                    else:
                         break
                
                # order Country
               while order_country == '0':
                    print('please insert the name of the country you wish to ship to')
                    order_country = name_insert(order_country)
                    if order_country.replace(' ','').isalpha() == False: 
                        order_country = '0'
                    else:
                         break

                #order Phone Number 
               while order_phone_number == '0':
                    checker = ''
                    order_phone_number = phone_number_insert(order_phone_number)
                    if order_phone_number.replace(' ','').isdigit() == False:
                         order_phone_number = '0'
                    else:
                        # check if phone number exists
                        checker = order_phone_check(order_phone_number,checker)
                        if checker == 'yes':
                            order_phone_number = '0'
                        elif checker == 'no':
                            print("Phone number valid, Thankyou")
                            break

                
                #GET user input for courier index to select courier
               print('now please choose a couries from the list below by typing in a index number')
               #PRINT couriers list with index value for each courier
               table_printer("couriers")
                #GET user input for courier index to select courier
               
               check_courier_id = '$'
               while order_courier_id == '$' :
                    order_courier_id, check_courier_id = id_number_check_couriers_table(order_courier_id, check_courier_id)
                    #  if the Id inserted doesnt exist loop resets and ask for a another insert
                    if check_courier_id == 'no':
                        order_courier_id = '$'
                    # if no insert is added code breaks and goes back to main menu
                    elif  check_courier_id == 'no change':
                        print("Cant leave this fiedl empty, please insert a Courier Id")
                        order_courier_id = '$'
                    

               if check_courier_id == 'yes':
                    print('Input valid, Id number exist ')

                    
                 
               #Customer Items
               print('Now taking items')
                # Inserting products from database to the items list in the dictionary    
               while bool(order_items) == False:
                    table_printer('products')
                    order_items = add_products_to_orders(order_items)
                    order_items = ','.join(order_items)
                    

                
               status_id = "1"
                # adding dictionary to list of orders    
               add_order(order_name, order_address, order_postcode, order_city, order_country, order_phone_number, order_courier_id, status_id, order_items)
               os.system('clear')
               
               user_input3 = ''

            # ELSE IF user input is 3:
            elif user_input3 == '3':
                 os.system('clear')

                 #     PRINT orders list with its index values
                 orders_table_printer()
                 print('\n')

                 switch_number = '$'
                 check_switch = ''
                # GET user input for order id
                 while switch_number == '$' :
                    switch_number , check_switch = id_number_check_status_table(switch_number,check_switch)
                    #  if the Id inserted doesnt exist loop resets and ask for a another insert
                    if check_switch == 'no':
                        switch_number = '$'
                # if no insert is added code breaks and goes back to main menu
                 if check_switch == 'no change':
                    print('No change desired going back to main menu')
                    

                 elif check_switch == 'yes':
                    print('Id number exist Please fill in the following fields or leave empty if you dont  want to make a change')
                    

                    #PRINT order status list with index values
                    table_printer('status_table')
                    change_status_number = '$'
                    check_status_number = ''
                    print('please select an approprite number that macthes the status you wish to change your order to')
                    while change_status_number  == '$' :
                        change_status_number , check_status_number = id_number_check_couriers_table( change_status_number, check_status_number )
                    #  if the Id inserted doesnt exist loop resets and ask for a another insert
                        if check_status_number == 'no':
                            change_status_number = '$'
                    
                    
               # if no insert is added, no change will be made 
                    if  check_status_number == 'no change':
                        print("Courier won't be changed")
                        
                # if a courier id that exists is inserted, the existing courier number will be changed.
                    elif check_status_number == 'yes':
                        print('Id number exist Please fill in the following fields or leave empty if you dont  want to make a change')
                        order_status_change(switch_number,change_status_number)
                        
                   

                 

                 print('\n')

                 user_input3 = ''
            
               
            

            elif user_input3 == '4':
                order_name4 = '0'
                order_address4 = '0'
                order_postcode4 = '0'
                order_city4 = '0'
                order_country4 = '0'
                order_phone_number4 = '0'
                order_courier_id4 = '$'
                status_id4 = '0'
                order_items4 = []
                
                dict34 = {'customer_name': '0', 'customer_address': '0', 'customer_phone': '0', 'courier': '', 'status': '0', 'items': [ ]}

                os.system('clear')
                orders_table_printer()

                order_change_number = '$'
                order_check_number = ''
                # GET user input for order id
                while order_change_number  == '$' :
                    order_change_number , order_check_number = id_number_check_status_table(order_change_number ,order_check_number)
                    #  if the Id inserted doesnt exist loop resets and ask for a another insert
                    if order_check_number == 'no':
                        order_change_number  = '$'
                # if no insert is added code breaks and goes back to main menu
                if order_check_number == 'no change':
                    print('No change desired going back to main menu')
                    

                elif order_check_number == 'yes':
                    print('Id number exist Please fill in the following fields or leave empty if you dont  want to make a change')

                    #customer name
                    while order_name4 == '0':
                        print('please insert a name for customer order or leave it empty')
                        order_name4 = name_insert(order_name4)
                        if order_name4.strip() == '' :
                            print('no name was inserted, name wont be changed')
                        elif order_name4.replace(' ','').isalpha() == True:
                            order_name_change(order_change_number,order_name4)
                        else:
                            print('insert a valid input or leaveit empty ')
                    print('\n')
               
                    # customer address
                    while order_address4 == "0":
                        print('please insert a new order address or leave it empty if you dont want to add a change')
                        order_address4 = address_fucntion(order_address4)

                        if order_address4 == "!":
                            order_address4 = '0'
                            print('address input is invalid')
                        elif order_address4 == '':
                            print('address will not be changed')
                        else:
                            order_address_change(order_change_number,order_address4)
                    print('\n')
                    
                    # customer postcode
                    while order_postcode4 == "0":
                        print('please insert a new postcode for the order or leave it empty if you dont want to add a change it')
                        order_postcode4  = address_fucntion(order_postcode4)

                        if order_postcode4  == "!":
                            order_postcode4  = '0'
                            print('address input is invalid')
                        elif order_postcode4 == '':
                            print('address will not be changed')
                        else:
                            order_postcode_change(order_change_number,order_postcode4 )
                    
                    # customer city
                    print('please insert a new order city location or leave it empty if you dont want to add a change')
                    while order_city4 == "0":
                        order_city4  =  name_insert(order_city4)

                        if order_city4.replace(' ','')  == '':
                            print('address was not inserted, not change will be added')
                        elif order_city4.replace(' ','').isalpha() == True:
                            print('order city will be changed')
                            order_city_change(order_change_number,order_city4)
                        else:
                            order_city4 = '0'
                            print('insert a correct input or leave it empty')
                    print('\n')

                    # customer country
                    while order_country4 == "0":
                        print('please insert a new order country or leave it empty if you dont want to add a change')
                        order_country4  =  name_insert(order_country4)

                        if order_country4.replace(' ','')  == '':
                            print('address was not inserted, not change will be added')
                        elif order_country4.replace(' ','').isalpha() == True:
                            print('order city will be changed')
                            order_country_change (order_change_number,order_country4)
                        else:
                            order_country4 = '0'
                            print('insert a correct input or leave it empty')
                    print('\n')
                            
        
                # customer phone 
                    while order_phone_number4 == '0':
                        print('please insert a new phone number for the order or leave it empty if you dont want to add a change')
                        check_phone4 = ''
                        order_phone_number4 = phone_number_insert(order_phone_number4)
                        if order_phone_number4.replace(' ','') == '':
                            print('phone number was not inserted, phone number will not be changed')
                        else:
                            #check if phone number exists
                            check_phone4 = order_phone_check(order_phone_number4,check_phone4)
                            if check_phone4 == 'yes':
                                order_phone_number4 = '0'
                            elif check_phone4 == 'no':
                                print("Phone number valid, Thankyou")
                                order_phone_number_change(order_change_number,order_phone_number4)
                                break
                            
 
                
                    #courier
                    table_printer("couriers")
                    courier_id_number = "$"
                    check_courier_id = ''

                    while courier_id_number == '$' :
                        courier_id_number, check_courier_id = id_number_check_couriers_table(courier_id_number, check_courier_id)
                        #if the Id inserted doesnt exist loop resets and ask for a another insert
                        if check_courier_id == 'no':
                            courier_id_number = '$'
                    
                    
                    #if no insert is added, no change will be made 
                    if  check_courier_id == 'no change':
                            print("Courier won't be changed")
                        
                    #if a courier id that exists is inserted, the existing courier number will be changed.
                    elif check_courier_id == 'yes':
                        print('Id number exist Please fill in the following fields or leave empty if you dont  want to make a change')
                        order_courier_change(order_change_number,courier_id_number)
                        
                
                    print('\n')
                    print('please select from the following options')

                    item_options = ['no change','add to items list','delete existing items list and start new one']
                


                    item_change_choice = ''

                    while item_change_choice not in ['0','1','2']:
                        os.system('clear')
                        print('please select from the following options')
                        print('\n')
                        enumerated_list(item_options)
                        print('\n')
                        one_orders_printer(order_change_number)
                        item_change_choice = input('so whats your choice in regards to the items list?  ')

                        if item_change_choice == '0':
                            print('no change was added to the items list')
                            break
                    
                        elif item_change_choice == '1':
                            table_printer("products")
                            existing_items = ''
                            new_list1 = []
                            existing_items = itemise_items(order_change_number,existing_items)
                            while bool(new_list1) == False:
                                new_list1 = add_products_to_orders(new_list1)
                                new_list1 = ','.join(new_list1)
                                existing_items = existing_items + ',' + new_list1
                            
                            order_items_change(order_change_number, new_list1)
                    
                        
                        elif item_change_choice == '2':
                            new_list2 = []
                            while bool(new_list2) == False:
                                table_printer('products')
                                new_list2 = add_products_to_orders(new_list2)
                                
                                new_list2 = ','.join(new_list2)
                            order_items_change(order_change_number, new_list2)
                                

                os.system('clear')
                user_input3 = ''
            
            
            elif user_input3 == '5':
                os.system('clear')
                orders_table_printer()
                order_id_number = '$'
                checker = ''
                #GET user input for order ID
                while order_id_number == '$' :
                    # if id number inserted doesnt exist or input is incorrect the insert resets
                    order_id_number , checker = id_number_check_orders_table (order_id_number, checker)
                    if checker == 'no':
                        order_id_number = '$'
                
                # if no id inserted, code breaks .
                if checker == 'no change':
                    print('NO Entry was taken, no order will be lated.')
                    
                elif checker == 'yes':
                    # DELETE courier with the id 
                    delete_order(order_id_number)               
        
                user_input3 = ''





























































