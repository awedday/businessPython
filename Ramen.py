#py -u "d:\учеба\Гацкан\Бизнес\Ramen.py" 
import pyodbc
import random

def Connection():
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
# Trusted Connection to Named Instance
    cursor=connection.cursor()

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
# Trusted Connection to Named Instance
cursor=connection.cursor()
cursor.execute("SELECT Login_Admin, Password_Admin FROM [Admin]")
rows = cursor.fetchmany(100)

for row in rows:
    print(row)
    # for i in row:
    #     row.append(row)
    # print(row)

BalanceAdmin = float(0)
BalanceUser = float(0)

def OrderForUser():
    
    print("Заказ \n\n")
    print("\nВведите номер телефона, пожалуйста (+7(***)***-**-**)")
    PhoneOrder = input()
    print("\nВведите желаемое количество блюд")
    amount = int(input())
    i= 0
    while(i<amount):
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"select [ID_Users] from [dbo].[Users] where [Phone_Users]='{PhoneOrder}'")
        user = cursor.fetchall()
        for row in user:
            userID = row[0]
            print("ID",userID)
            if len(user) == 0:
                print("Неверный номер телефона")
        
            else:
        # userint = int(user[0])
                print("\nПрием заказа\n")
                print("Мясо: Говядина | Курица | Свинина")
                Meat = input()
                print("Бульон: Говяжий | Куриный")
                Bouillon = input()
                print("Лапша: Рисовая | Гречневая | Яичная")
                Noodles = input()
                print("Яйца: Сырое | Всмятку | В мешочек")
                Egg = input()
                print("Морковь: Вареная | Свежая")
                Carrot = input()
                print("Огурец: Свежий | Маринованный")
                Cucumber = input()
                print("Картофель: Сладкий картофель | Русский картофель")
                Potato = input()
                connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
                cursor=connection.cursor()
                cursor.execute(f"INSERT INTO [Dish] ([Meat_Dish],[Bouillon_Dish],[Noodles_Dish],[Egg_Dish],[Carrot_Dish],[Cucumber_Dish],[Potato_Dish])  VALUES ('{Meat}', '{Bouillon}','{Noodles}','{Egg}','{Carrot}','{Cucumber}','{Potato}')")
                cursor=connection.cursor()
                connection.commit()
                cursor=connection.cursor()
                cursor.execute(f"select [ID_Dish] from [dbo].[Dish] where [Meat_Dish]='{Meat}' and [Bouillon_Dish] = '{Bouillon}' and [Noodles_Dish] = '{Noodles}' and [Egg_Dish] = '{Egg}' and [Carrot_Dish] = '{Carrot}' and [Cucumber_Dish] = '{Cucumber}' and [Potato_Dish] = '{Potato}'")
                dish = cursor.fetchall()
                connection.commit()
                for row in dish:
                    dishID = row[0]
                    if len(dish) == 0:
                        print("Неверный номер телефона")
                    else:
                        

            # print("tuple", test[0])
            # print("User",qqqq)
            # print("Dish",y)
                        cursor=connection.cursor()
                        cursor.execute(f"INSERT INTO [Order] ([Data_Order],[Users_ID],[Dish_ID]) VALUES (getdate(), {userID},{dishID})")
                        connection.commit()
                        print("\nХотите добавить топинги в заказ?\n 1 - да\n 2 - нет")
                        topping = int(input())
                        if topping == 1:
                            print("\nКакой топинг вы хотите добавить?\n 1 - ростки сои\n 2 - сыр\n 3 - нарутомаки")
                            topSelect = int(input())
                            if topSelect == 1:
                                print("\nРостки сои")
                                SoySprouts_Toppings = 35
                                print("Заказ принят")
                                cursor=connection.cursor()
                                cursor.execute(f"select [Total_Price] from [dbo].[Price_Quantity]")
                                price = cursor.fetchall()
                                cursor.commit()
                                for row in price:
                                    TotalCost = row[0]
                                    if len(price) == 0:
                                        print("Ошибка")
                                    else:
                                        Dictionary = random.randint(0,10)
                                        if Dictionary == 5:
                                            print("\nОй, в блюде русско-корейский словарь\nУ вас скидка 30 процентов")
                                            Procent = (TotalCost+SoySprouts_Toppings)*30/100
                                            cursor=connection.cursor()
                                            cursor.execute(F"UPDATE [Users] SET [Balance_Users]=[Balance_Users]-'{TotalCost}'-'{SoySprouts_Toppings}'+'{Procent}' where [Phone_Users] = '{PhoneOrder}'")
                                            cursor.commit()
                                        else:
                                            cursor=connection.cursor()
                                            cursor.execute(F"UPDATE [Users] SET [Balance_Users]=[Balance_Users]-'{TotalCost}' - '{SoySprouts_Toppings}' where [Phone_Users] = '{PhoneOrder}'")
                                            cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Users] SET [Loyalty_Card_Users]=+1 where [Phone_Users] ='{PhoneOrder}'")
                                    cursor.commit()
                                    Amount = 1
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Bouillon_Quantity]=[Bouillon_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Meat_Quantity]=[Meat_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Noodles_Quantity]=[Noodles_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Egg_Quantity]=[Egg_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Carrot_Quantity]=[Carrot_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Cucumber_Quantity]=[Cucumber_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Potato_Quantity]=[Potato_Quantity]-{Amount}")
                                    cursor.commit()
                                    print("Деньги сняты)")
                                    print("Деньги сняты)")
                                    i += 1
                            elif topSelect == 2:
                                print("\nСыр")
                                Cheese_Toppings = 40
                                print("Заказ принят")
                                cursor=connection.cursor()
                                cursor.execute(f"select [Total_Price] from [dbo].[Price_Quantity]")
                                price = cursor.fetchall()
                                cursor.commit()
                                for row in price:
                                    TotalCost = row[0]
                                    if len(price) == 0:
                                        print("Ошибка")
                                    else:
                                        Dictionary = random.randint(0,10)
                                        if Dictionary == 5:
                                            print("\nОй, в блюде русско-корейский словарь\nУ вас скидка 30 процентов")
                                            Procent = (TotalCost+Cheese_Toppings)*30/100
                                            cursor=connection.cursor()
                                            cursor.execute(F"UPDATE [Users] SET [Balance_Users]=[Balance_Users]-'{TotalCost}'-'{Cheese_Toppings}'+'{Procent}' where [Phone_Users] = '{PhoneOrder}'")
                                            cursor.commit()
                                        else:
                                            cursor=connection.cursor()
                                            cursor.execute(F"UPDATE [Users] SET [Balance_Users]=[Balance_Users]-'{TotalCost}' - '{Cheese_Toppings}' where [Phone_Users] = '{PhoneOrder}'")
                                            cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Users] SET [Loyalty_Card_Users]=+1 where [Phone_Users] ='{PhoneOrder}'")
                                    cursor.commit()
                                    Amount = 1
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Bouillon_Quantity]=[Bouillon_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Meat_Quantity]=[Meat_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Noodles_Quantity]=[Noodles_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Egg_Quantity]=[Egg_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Carrot_Quantity]=[Carrot_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Cucumber_Quantity]=[Cucumber_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Potato_Quantity]=[Potato_Quantity]-{Amount}")
                                    cursor.commit()
                                    print("Деньги сняты)")
                                    print("Деньги сняты)")
                                    i += 1
                            elif topSelect ==3:
                                print("\nНарутомаки")
                                Narutomaki_Toppings = 35
                                print("Заказ принят")
                                cursor=connection.cursor()
                                cursor.execute(f"select [Total_Price] from [dbo].[Price_Quantity]")
                                price = cursor.fetchall()
                                cursor.commit()
                                for row in price:
                                    TotalCost = row[0]
                                    if len(price) == 0:
                                        print("Ошибка")
                                    else:
                                        Dictionary = random.randint(0,10)
                                        if Dictionary == 5:
                                            print("\nОй, в блюде русско-корейский словарь\nУ вас скидка 30 процентов")
                                            Procent = (TotalCost+Narutomaki_Toppings)*30/100
                                            cursor=connection.cursor()
                                            cursor.execute(F"UPDATE [Users] SET [Balance_Users]=[Balance_Users]-'{TotalCost}'-'{Narutomaki_Toppings}'+'{Procent}' where [Phone_Users] = '{PhoneOrder}'")
                                            cursor.commit()
                                        else:
                                            cursor=connection.cursor()
                                            cursor.execute(F"UPDATE [Users] SET [Balance_Users]=[Balance_Users]-'{TotalCost}' - '{Narutomaki_Toppings}' where [Phone_Users] = '{PhoneOrder}'")
                                            cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Users] SET [Loyalty_Card_Users]=+1 where [Phone_Users] ='{PhoneOrder}'")
                                    cursor.commit()
                                    Amount = 1
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Bouillon_Quantity]=[Bouillon_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Meat_Quantity]=[Meat_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Noodles_Quantity]=[Noodles_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Egg_Quantity]=[Egg_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Carrot_Quantity]=[Carrot_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Cucumber_Quantity]=[Cucumber_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Potato_Quantity]=[Potato_Quantity]-{Amount}")
                                    cursor.commit()
                                    print("Деньги сняты)")
                                    print("Деньги сняты)")
                                    i += 1
                        elif topping == 2:
                            print("Заказ принят")
                            cursor=connection.cursor()
                            cursor.execute(f"select [Total_Price] from [dbo].[Price_Quantity]")
                            price = cursor.fetchall()
                            cursor.commit()
                            for row in price:
                                TotalCost = row[0]
                                if len(price) == 0:
                                    print("Ошибка")
                                else:
                                    Dictionary = random.randint(0,10)
                                    if Dictionary == 5:
                                        print("\nОй, в блюде русско-корейский словарь\nУ вас скидка 30 процентов")
                                        Procent = TotalCost*30/100
                                        cursor=connection.cursor()
                                        cursor.execute(F"UPDATE [Users] SET [Balance_Users]=[Balance_Users]-'{TotalCost}'+'{Procent}' where [Phone_Users] = '{PhoneOrder}'")
                                        cursor.commit()
                                    else:
                                        cursor=connection.cursor()
                                        cursor.execute(F"UPDATE [Users] SET [Balance_Users]=[Balance_Users]-'{TotalCost}' where [Phone_Users] = '{PhoneOrder}'")
                                        cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Users] SET [Loyalty_Card_Users]=+1 where [Phone_Users] ='{PhoneOrder}'")
                                    cursor.commit()
                                    Amount = 1
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Bouillon_Quantity]=[Bouillon_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Meat_Quantity]=[Meat_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Noodles_Quantity]=[Noodles_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Egg_Quantity]=[Egg_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Carrot_Quantity]=[Carrot_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Cucumber_Quantity]=[Cucumber_Quantity]-{Amount}")
                                    cursor.commit()
                                    cursor=connection.cursor()
                                    cursor.execute(F"UPDATE [Price_Quantity] SET [Potato_Quantity]=[Potato_Quantity]-{Amount}")
                                    cursor.commit()
                                    print("Деньги сняты)")
                                    i += 1
                        else:
                            print("\nВыберите действие")


        
def PurchaseGoods():
    print("\nЗакупка товаров\nНаличие: ")
    print("Мясо  |  Бульон  |  Лапша  |  Яйца  |  Морковь  |  Огурец  |  Картофель")
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
    cursor=connection.cursor()
    cursor.execute("SELECT [Meat_Quantity],[Bouillon_Quantity],[Noodles_Quantity],[Egg_Quantity],[Carrot_Quantity],[Cucumber_Quantity],[Potato_Quantity] FROM [Price_Quantity]")
    rows = cursor.fetchmany(100)
    print(rows)
    print("Желаете преобрести какую-то позицию?\n 1 - да\n 2 - нет")
    Availability = input()
    if Availability == '1':
        print("Какую позицию вы хотите приобрести?\n 1 - Мясо\n 2 -Бульон\n 3 - Лапша\n 4- Яйца\n 5 - Морковь\n 6 - Огурец \n 7 - Картофель")
        Choice = input()
        if Choice == '1':
            print("Какое количество желаете приобрести?")
            Amount = float(input())
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Price_Quantity] SET [Meat_Quantity]=[Meat_Quantity]+{Amount}")
            cursor.commit()
            MeatCost = 70
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Admin] SET [Balance_Admin]=[Balance_Admin]-{MeatCost}")
            cursor.commit()
            AdminFunctionSelection()
        elif Choice =='2':
            print("Какое количество желаете приобрести?")
            Amount = float(input())
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Price_Quantity] SET [Bouillon_Quantity]=[Bouillon_Quantity]+{Amount}")
            cursor.commit()
            BouillonCost = 40
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Admin] SET [Balance_Admin]=[Balance_Admin]-{BouillonCost}")
            cursor.commit()
            AdminFunctionSelection()
        elif Choice =='3':
            print("Какое количество желаете приобрести?")
            Amount = float(input())
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Price_Quantity] SET [Noodles_Quantity]=[Noodles_Quantity]+{Amount}")
            cursor.commit()
            NoodlesCost = 40
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Admin] SET [Balance_Admin]=[Balance_Admin]-{NoodlesCost}")
            cursor.commit()
            AdminFunctionSelection()
        elif Choice =='4':
            print("Какое количество желаете приобрести?")
            Amount = float(input())
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Price_Quantity] SET [Egg_Quantity]=[Egg_Quantity]+{Amount}")
            cursor.commit()
            EggCost = 40
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Admin] SET [Balance_Admin]=[Balance_Admin]-{EggCost}")
            cursor.commit()
            AdminFunctionSelection()
        elif Choice =='5':
            print("Какое количество желаете приобрести?")
            Amount = float(input())
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Price_Quantity] SET [Carrot_Quantity]=[Carrot_Quantity]+{Amount}")
            cursor.commit()
            CarrotCost = 40
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Admin] SET [Balance_Admin]=[Balance_Admin]-{CarrotCost}")
            cursor.commit()
            AdminFunctionSelection()
        elif Choice =='6':
            print("Какое количество желаете приобрести?")
            Amount = float(input())
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Price_Quantity] SET [Cucumber_Quantity]=[Cucumber_Quantity]+{Amount}")
            cursor.commit()
            CucumberCost = 40
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Admin] SET [Balance_Admin]=[Balance_Admin]-{CucumberCost}")
            cursor.commit()
            AdminFunctionSelection()
        elif Choice =='7':
            print("Какое количество желаете приобрести?")
            Amount = float(input())
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Price_Quantity] SET [Potato_Quantity]=[Potato_Quantity]+{Amount}")
            cursor.commit()
            PotatoCost = 40
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Admin] SET [Balance_Admin]=[Balance_Admin]-{PotatoCost}")
            cursor.commit()
            AdminFunctionSelection()
        else:
            print("Вы не выбрали действие!")
    elif Availability == '2':
        print("Наличие остается неизменным")
        AdminFunctionSelection()
    else: 
        print("Вы не выбрали действие")

def ChangeCost():
    print("Изменение цены блюда(составляющих)\n")
    print("\nИзначальная цена: \n")
    print("Общая цена  |  Мясо  |  Бульон  |  Лапша  |  Яйца  |  Морковь  |  Огурец  |  Картофель")
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
    cursor=connection.cursor()
    cursor.execute("SELECT [Total_Price],[Meat_Price],[Bouillon_Price],[Noodles_Price],[Egg_Price],[Carrot_Price],[Cucumber_Price],[Potato_Price] FROM [Price_Quantity]")
    rows = cursor.fetchmany(100)
    print(rows)
    print("Хотите ли вы изменить цену блюду?\n 1 - да\n 2 - нет")
    Choice = input()
    if Choice == '1':
        print("\nИзменение цены блюда:\n")
        print("Напишите стоимость мяса : \n")
        MeatCost = float(input())
        cursor=connection.cursor()
        cursor.execute(F"UPDATE [Price_Quantity] SET [Meat_Price]='{MeatCost}'")
        cursor.commit()
        print("Напишите стоимость бульона : \n")
        BouillonCost = float(input())
        cursor=connection.cursor()
        cursor.execute(F"UPDATE [Price_Quantity] SET [Bouillon_Price]='{BouillonCost}'")
        cursor.commit()
        print("Напишите стоимость лапши : \n")
        NoodlesCost = float(input())
        cursor=connection.cursor()
        cursor.execute(F"UPDATE [Price_Quantity] SET [Noodles_Price]='{NoodlesCost}'")
        cursor.commit()
        print("Напишите стоимость яиц : \n")
        EggCost = float(input())
        cursor=connection.cursor()
        cursor.execute(F"UPDATE [Price_Quantity] SET [Egg_Price]='{EggCost}'")
        cursor.commit()
        print("Напишите стоимость моркови : \n")
        CarrotCost = float(input())
        cursor=connection.cursor()
        cursor.execute(F"UPDATE [Price_Quantity] SET [Carrot_Price]='{CarrotCost}'")
        cursor.commit()
        print("Напишите стоимость огурцов : \n")
        CucumberCost = float(input())
        cursor=connection.cursor()
        cursor.execute(F"UPDATE [Price_Quantity] SET [Cucumber_Price]='{CucumberCost}'")
        cursor.commit()
        print("Напишите стоимость картофеля : \n")
        PotatoCost = float(input())
        cursor=connection.cursor()
        cursor.execute(F"UPDATE [Price_Quantity] SET [Potato_Price]='{PotatoCost}'")
        cursor.commit()
        TotalCostRamen = float(MeatCost + BouillonCost + NoodlesCost + EggCost + CarrotCost + CucumberCost + PotatoCost)
        print("\nИтоговая цена рамена: ", TotalCostRamen)
        cursor=connection.cursor()
        cursor.execute(F"UPDATE [Price_Quantity] SET [Total_Price]='{TotalCostRamen}'")
        cursor.commit()
        AdminFunctionSelection()
    elif Choice == '2':
        print("\nЦена остается прежней")
        AdminFunctionSelection()
    else:
        print("\nВы не выбрали действие!")

def UserFunctionSelection():
    while(True):
        print(" \n\nВы авторизовались как пользователь. Ниже предоставлен список возможностей: \n\n")
        print("\nВыберите действие!\n1 - Покупка рамена\n2 - История покупок\n3 - Карта лояльности\n")
        AdminFunction = input()
        if AdminFunction == '1':
            print("Покупка рамена")
            OrderForUser()
        elif AdminFunction == '2':
            print("\nИстория покупок")
            UserShoppingList()
        elif AdminFunction == '3':
            print("\nКарта лояльности")
            UserLoyaltyCardForUser()
    
        else:
            print("Вы не выбрали действие!") 

def UserShoppingList():
    print("Список покупок пользователей\n\n")
    print("\nВведите номер телефона покупателя, пожалуйста (+7(***)***-**-**)")
    PhoneShopping = input()
    cursor=connection.cursor()
    cursor.execute(f"select [Data_Order], [Phone_Users],[Name_Users] ,[Meat_Dish],[Bouillon_Dish],[Noodles_Dish],[Egg_Dish],[Carrot_Dish],[Cucumber_Dish],[Potato_Dish] from [dbo].[Order] inner join [dbo].[Users] on [Users_ID] = [ID_Users] inner join [dbo].[Dish] on [Dish_ID] = [ID_Dish] where [Phone_Users]='{PhoneShopping}' order by [Data_Order] ASC")
    rows = cursor.fetchmany(100)
    if len(rows) == 0:
        print("Неверный номер телефона")
        
    else:
        print("Дата заказа  |  Номер покупателя  |  Имя покупателя  |  Мясо  |  Бульон  |  Лапша  |  Яйца  |  Морковь  |  Огурец  |  Картофель")
        print(rows)
        AdminFunctionSelection()

def UserLoyaltyCard():
    print("Карта лояльности пользователя\n\n")
    print("\nВведите номер телефона покупателя, пожалуйста (+7(***)***-**-**)")
    PhoneCard = input()
    cursor=connection.cursor()
    cursor.execute(f"select [Phone_Users],[Name_Users], [Loyalty_Card_Users] from [dbo].[Users] where [Phone_Users]='{PhoneCard}'")
    rows = cursor.fetchmany(100)
    if len(rows) == 0:
        print("Неверный номер телефона")
        
    else:
        print("Номер покупателя   |  Имя пользователя  |  Карта лояльности")
        print(rows)
        AdminFunctionSelection()

def UserLoyaltyCardForUser():
    print("Карта лояльности \n\n")
    print("\nВведите номер телефона, пожалуйста (+7(***)***-**-**)")
    PhoneCard = input()
    cursor=connection.cursor()
    cursor.execute(f"select [Phone_Users],[Name_Users], [Loyalty_Card_Users] from [dbo].[Users] where [Phone_Users]='{PhoneCard}'")
    rows = cursor.fetchmany(100)
    if len(rows) == 0:
        print("Неверный номер телефона")
        
    else:
        print("Номер   |  Имя |  Карта лояльности")
        print(rows)
        UserFunctionSelection()

def ChangeDish():
    print("Введите, пожалуйста, ингредиент, который хотите удалить\n1 - Мясо\n2 - Бульон\n3 - Лапша\n4 - Яйца\n5 - Морковь\n6 - Огурец\n7 - Картофель")
    IngredientChange = input()
    if IngredientChange == '1':
        print("Мясо")
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] DROP CONSTRAINT [CH_Meat_Dish]")
        connection.commit()
        print("\nВам необходимо будет ввести два новых выбора мяса\n")
        print("\nВведите первый вариант для мяса: \n")
        OneMeat = input()
        print("\nВведите второй вариант для мяса: \n")
        TwoMeat = input()
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] ADD CONSTRAINT [CH_Meat_Dish] check ([Meat_Dish] in ('{OneMeat}','{TwoMeat}'))")
        print("Вы успешно изменили 'Мясо'")
        AdminFunctionSelection()
    elif IngredientChange == '2':
        print("Бульон")
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] DROP CONSTRAINT [CH_Bouillon_Dish]")
        connection.commit()
        print("\nВам необходимо будет ввести два новых выбора бульона\n")
        print("\nВведите первый вариант для бульона: \n")
        OneBouillon = input()
        print("\nВведите второй вариант для бульона: \n")
        TwoBouillon = input()
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] ADD CONSTRAINT [CH_Bouillon_Dish] check ([Bouillon_Dish] in ('{OneBouillon}','{TwoBouillon}'))")
        print("Вы успешно изменили 'Бульон'")
        AdminFunctionSelection()
    elif IngredientChange == '3':
        print("Лапша")
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] DROP CONSTRAINT [CH_Noodles_Dish]")
        connection.commit()
        print("\nВам необходимо будет ввести два новых выбора лапши\n")
        print("\nВведите первый вариант для лапши: \n")
        OneNoodles = input()
        print("\nВведите второй вариант для лапши: \n")
        TwoNoodles = input()
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] ADD CONSTRAINT [CH_Noodles_Dish] check ([Noodles_Dish] in ('{OneNoodles}','{TwoNoodles}'))")
        print("Вы успешно изменили 'Лапша'")
        AdminFunctionSelection()
    elif IngredientChange == '4':
        print("Яйца")
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Egg] DROP CONSTRAINT [CH_Egg_Dish]")
        connection.commit()
        print("\nВам необходимо будет ввести два новых выбора яиц\n")
        print("\nВведите первый вариант для яиц: \n")
        OneEgg = input()
        print("\nВведите второй вариант для яиц: \n")
        TwoEgg = input()
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] ADD CONSTRAINT [CH_Egg_Dish] check ([Egg_Dish] in ('{OneEgg}','{TwoEgg}'))")
        print("Вы успешно изменили 'Яйца'")
        AdminFunctionSelection()
    elif IngredientChange == '5':
        print("Морковь")
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Carrot] DROP CONSTRAINT [CH_Carrot_Dish]")
        connection.commit()
        print("\nВам необходимо будет ввести два новых выбора морковь\n")
        print("\nВведите первый вариант для моркови: \n")
        OneCarrot = input()
        print("\nВведите второй вариант для моркови: \n")
        TwoCarrot = input()
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] ADD CONSTRAINT [CH_Carrot_Dish] check ([Carrot_Dish] in ('{OneCarrot}','{TwoCarrot}'))")
        print("Вы успешно изменили 'Морковь'")
        AdminFunctionSelection()
    elif IngredientChange == '6':
        print("Огурец")
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] DROP CONSTRAINT [CH_Cucumber_Dish]")
        connection.commit()
        print("\nВам необходимо будет ввести два новых выбора оугрца\n")
        print("\nВведите первый вариант для огурца: \n")
        OneCucumber = input()
        print("\nВведите второй вариант для огурца: \n")
        TwoCucumber = input()
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] ADD CONSTRAINT [CH_Cucumber_Dish] check ([Cucumber_Dish] in ('{OneCucumber}','{TwoCucumber}'))")
        print("Вы успешно изменили 'Огурец'")
        AdminFunctionSelection()
    elif IngredientChange == '7':
        print("Картофель")
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] DROP CONSTRAINT [CH_Potato_Dish]")
        connection.commit()
        print("\nВам необходимо будет ввести два новых выбора картофеля\n")
        print("\nВведите первый вариант для картофеля: \n")
        OnePotato = input()
        print("\nВведите второй вариант для картофеля: \n")
        TwoPotato = input()
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
        cursor=connection.cursor()
        cursor.execute(f"ALTER TABLE [dbo].[Dish] ADD CONSTRAINT [CH_Potato_Dish] check ([Potato_Dish] in ('{OnePotato}','{TwoPotato}'))")
        print("Вы успешно изменили 'Картофель'")
        AdminFunctionSelection()
    else:
        print("Вы не ввели ингредиент!")   

def AdminFunctionSelection():
    while(True):
        print(" \n\nВы авторизовались как администратор. Ниже предоставлен список возможностей: \n\n")
        print("\nВыберите действие!\n1 - Закупка товара\n2 - Изменение цены блюд(составляющих)\n3 - Смена ингредиентов в блюде \n4 - просмотр покупок пользователей\n5 - Просмотр карты лояльности пользователей")
        AdminFunction = input()
        if AdminFunction == '1':
            print("Закупка товаров")
            PurchaseGoods()
        elif AdminFunction == '2':
            print("\nИзменение цены блюд(составляющих)")
            ChangeCost()
        elif AdminFunction == '3':
            print("\nСмена ингредиентов в блюде")
            ChangeDish()
        elif AdminFunction == '4':
            print("\nПросмотр покупок пользователя")
            UserShoppingList()
        elif AdminFunction == '5':
            print("\nПросмотр карты лояльности пользователей")
            UserLoyaltyCard()
        else:
            print("Вы не выбрали действие!")   

def Input_Function():
    print("Введите логин от аккаунта")
    Login_Input = input()
    print("Введите пароль от аккаунта")
    Password_Input = input()
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
    
    cursor=connection.cursor()
    cursor.execute(f"SELECT Login_Admin, Password_Admin FROM [dbo].[Admin] WHERE [Login_Admin] = '{Login_Input}' AND [Password_Admin] = '{Password_Input}'")
    row = cursor.fetchmany(100)
    if len(row) == 0:
        cursor=connection.cursor()
        cursor.execute(f"SELECT Login_Users, Password_Users FROM [dbo].[Users] WHERE [Login_Users] = '{Login_Input}' AND [Password_Users] = '{Password_Input}'")
        row = cursor.fetchmany(100)
        if len(row) == 0:
            print("Введен неверный логин или пароль")
            
        else:
            print("Ура, вы авторизовались")
            BalanceUser = 1000
            cursor=connection.cursor()
            cursor.execute(F"UPDATE [Users] SET [Balance_Users]='{BalanceUser}' WHERE [Login_Users] = '{Login_Input}' AND [Password_Users] = '{Password_Input}'")
            cursor.commit()
            UserFunctionSelection()

            
    else:
        print("Ура, вы авторизовались")
        BalanceAdmin = 10000
        cursor=connection.cursor()
        cursor.execute(F"UPDATE [Admin] SET [Balance_Admin]='{BalanceAdmin}' WHERE [Login_Admin] = '{Login_Input}' AND [Password_Admin] = '{Password_Input}'")
        cursor.commit()

        AdminFunctionSelection()

    

def Registration():
    print("Регистрация аккаунта!\nЗаполните, пожалуйста, все строки.\n\n")
    print("Введите Имя пользователя")
    Name_Input = input()
    print("Введите Номер телефона (+7(***)***-**-**)")
    Phone_Input = input()
    print("Введите логин")
    Login_Input_R = input()
    print("Введите пароль")
    Password_Input_R = input()
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
    cursor=connection.cursor()
    cursor.execute(f"INSERT INTO [Users] ([Name_Users],[Phone_Users],[Login_Users],[Password_Users]) VALUES ('{Name_Input}', '{Phone_Input}','{Login_Input_R}','{Password_Input_R}')")
    cursor=connection.cursor()
    connection.commit()
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-AQ3KUDTV\IDONTKNOW;DATABASE=Ramen_Database;Trusted_Connection=yes;')
    cursor.execute(f"SELECT Login_Users, Password_Users FROM [dbo].[Users] WHERE [Login_Users] = '{Login_Input_R}' AND [Password_Users] = '{Password_Input_R}'")
    row = cursor.fetchmany(100)
    if len(row) == 0:
        print("Ошибка логина или пароля")
        
    else:
        print("Ура, вы зареганы")
        RegisterAvtor()
        
        



def RegisterAvtor():
    while(True):
        print('Здравствуйте! Вас приветсвует новая раменичная "DAEBAK". Выберите дальнейшее действие, пожалуйста!')
        print("\n\n 1 - Регистрация \n 2 - Вход \n ")
        RegisterOrInput = input()
        if RegisterOrInput == '1':
            Registration()
            print("\nПосле регистрации, пожалуйста, пройдите авторизацию!\n")
            RegisterAvtor()
        elif RegisterOrInput == '2':
            Input_Function()
        else:
            print("Выберите действие!")


        
        
RegisterAvtor()



#cursor.execute("SELECT * FROM Admin")
#for row in cursor.fetchall():
#    print(row)

#cursor.close()
#connection.close()