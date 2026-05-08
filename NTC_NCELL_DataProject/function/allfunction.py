def decorate():
    print()
    print(f'Welcome to our data/voice pack services ')
    print("--"*30)
    print()
    
def subdecorate():
    print("--"*30)
    print()

def mainmenu():
    while True:
        print(f'1. All Time Data pack ')
        print(f'2. Reccurring pack ')
        print(f'3. Unlimited Facebook/YouTube Pack ')
        print(f'4. SMS Pack')
        print(f'5. Exit ')
        print()
        choice=int(input("Enter your choice ? : "))
        if choice == 1:
            alltimedatapack()
        elif choice == 2:
            recurringpack()
        elif choice==3:
            unlimitedfy()
        elif choice==4:
            smspack()
        elif choice == 5:
            subdecorate()
            print('Thank you for using NTC Data Pack Service')
            subdecorate()
            exit()
        else:
            subdecorate()
            print('Invalid choice please enter a valid choice [1-5]')
            subdecorate()
            print()

def alltimedatapack():
    while True:
        print(f'1. 1GB @ Rs 30 – 1 Day ')
        print(f'2. 5GB @ Rs 109 – 7 Day ')
        print(f'3. 4GB @ Rs 99 – 1 Day ')
        print(f'4. 12GB @ Rs 199 – 7 Day ')
        print(f'5. Main Menu ')
        print()
        choice=int(input("Enter your choice ? : "))
        if choice == 1:
            subdecorate()
            print("1GB Data pack activated Succesfully for 1 day...")
            subdecorate()
            exit()
        elif choice == 2:
            subdecorate()
            print("5GB Data pack activated Succesfully for 7 days...")
            subdecorate()
            exit()
        elif choice==3:
            subdecorate()
            print("4GB Data pack activated Succesfully for 1day...")
            subdecorate()
            exit()
        elif choice==4:
            subdecorate()
            print("12GB Data pack activated Succesfully for 7 days...")
            subdecorate()
            exit()
        elif choice == 5:
            mainmenu()
        else:
            subdecorate()
            print('Invalid choice please enter a valid choice [1-5]')
            subdecorate()
            print()

def recurringpack():
    while True:
        print(f'1. 700MB / Day @ Rs 299 – 28 Days')
        print(f'2. 1.5GB / Day @ Rs 599 – 28 Days')
        print(f'3. Main Menu ')
        print()
        choice=int(input("Enter your choice ? : "))
        if choice == 1:
            subdecorate()
            print("700MB/Day Recurring pack activated Succesfully for 28 days...")
            subdecorate()
            exit()
        elif choice == 2:
            subdecorate()
            print("1.5GB/Day Recurring pack activated Succesfully for 28 days...")
            subdecorate()
            exit()
        elif choice == 3:
            mainmenu()
        else:
            subdecorate()
            print('Invalid choice please enter a valid choice [1-3]')
            subdecorate()
            print()

def  unlimitedfy():
    while True:
        print(f'1. Unlimited Facebook @ Rs 55 – 3 Days')
        print(f'2. Unlimited YouTube @ Rs 55 – 3 Days')
        print(f'3. Main Menu ')
        print()
        choice=int(input("Enter your choice ? : "))
        if choice == 1:
            subdecorate()
            print("Unlimited Facebook pack activated Succesfully for 3 days...")
            subdecorate()
            exit()
        elif choice == 2:
            subdecorate()
            print("Unlimited YouTube pack activated Succesfully for 3 days...")
            subdecorate()
            exit()
        elif choice == 3:
            mainmenu()
        else:
            subdecorate()
            print('Invalid choice please enter a valid choice [1-3]')
            subdecorate()
            print()

def smspack():
    while True:
        print(f'1. 200 SMS @ Rs 35 – 1 Day')
        print(f'2. 200 SMS @ Rs 60 – 7 Days')
        print(f'3. 500 SMS @ Rs 150 – 28 Days')
        print(f'4. Main Menu ')
        print()
        choice=int(input("Enter your choice ? : "))
        if choice == 1:
            subdecorate()
            print("200 SMS pack activated Succesfully for 1 day...")
            subdecorate()
            exit()
        elif choice == 2:
            subdecorate()
            print("200 SMS pack activated Succesfully for 7 days...")
            subdecorate()
            exit()
        elif choice==3:
            subdecorate()
            print("500 SMS pack activated Succesfully for 28 days...")
            subdecorate()
            exit()
        elif choice == 4:
            mainmenu()
        else:
            subdecorate()
            print('Invalid choice please enter a valid choice [1-4]')
            subdecorate()
            print()