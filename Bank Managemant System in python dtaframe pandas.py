import os
import platform
import pandas as pd
import csv


def deposit():
    data = pd.read_csv("bank.csv")
    print(data)
    x = int(input("Enter Account Number  "))
    data1 = data.loc[data['Accno'] == int(x)]
    if data1.empty:
        print("RECORD NOT FOUND")
    else:
        y = int(input("Enter amount to be deposit  "))
        k = int(data1["Bal"])
        # print(k)
        k = k + y;
        data.loc[data['Accno'] == int(x), 'Bal'] = k
        # create empty frame with only column name
        column_names = ["Accno", "Name", "Typeacc", "Bal"]
        data2 = pd.DataFrame(columns=column_names)
        data2.to_csv('bank.csv', index=False)
        # add data
        data.to_csv('bank.csv', index=False, mode='a', header=False)


def withdraw():
    data = pd.read_csv("bank.csv")
    print(data)
    x = int(input("Enter Account Number  "))
    data1 = data.loc[data['Accno'] == int(x)]
    if data1.empty:
        print("RECORD NOT FOUND")
    else:
        y = int(input("Enter amount to be Withdraw  "))
        k = int(data1["Bal"])
        # print(k)
        if k > y:
            k = k - y;
            data.loc[data['Accno'] == int(x), 'Bal'] = k
            # create empty frame with only column name
            column_names = ["Accno", "Name", "Typeacc", "Bal"]
            data2 = pd.DataFrame(columns=column_names)
            data2.to_csv('bank.csv', index=False)
            # add data
            data.to_csv('bank.csv', index=False, mode='a', header=False)
        else:
            print("Bal is less for withdraw ")


def update_account():
    data = pd.read_csv("bank.csv")
    print(data)
    x = int(input("Enter Account Number  "))
    y = input("Enter the new name ")
    data.loc[data['Accno'] == int(x), 'Name'] = y
    # print(data)
    # create empty frame with only column name
    column_names = ["Accno", "Name", "Typeacc", "Bal"]
    data1 = pd.DataFrame(columns=column_names)
    data1.to_csv('bank.csv', index=False)
    # add data
    data.to_csv('bank.csv', index=False,
                mode='a', header=False)


def del_account():
    data = []
    data = pd.read_csv("bank.csv")
    print(data)
    x = input("enter Account number ")
    data = data.drop(data[data['Accno'] == int(x)].index, inplace=False)

    # create empty frame with only column name
    column_names = ["Accno", "Name", "Typeacc", "Bal"]
    data1 = pd.DataFrame(columns=column_names)
    data1.to_csv('bank.csv', index=False)
    # add data
    data.to_csv('bank.csv', index=False, mode='a', header=False)


def search_account():
    df = pd.read_csv("bank.csv")
    x = int(input("enter customer account number to be search "))
    df1 = df.loc[df['Accno'] == x]
    if df1.empty:
        print("Recoed Does not Exist ")
    else:
        print("Record Found");
        print(df1);


def view_account():
    data = pd.read_csv("bank.csv")
    # print(data)
    print("Accno\tName\t\tTypeAcc\t\t\tBalance")
    for index, row in data.iterrows():
        print(row["Accno"], '\t', row["Name"], '\t\t',
              row["Typeacc"], '\t\t', row["Bal"], "\n")


def add_account():
    global info
    # info=pd.DataFrame()
    file_size = 0
    if (os.path.isfile('bank.csv')):
        pass
    else:
        column_names = ["Accno", "Name", "Typeacc", "Bal"]
        info = pd.DataFrame(columns=column_names)
        info.to_csv('bank.csv', index=False)
        # print("OK")
    # read csv file
    data = pd.read_csv("bank.csv")
    # print(data)
    # read last account number
    if data.empty:
        ac = 100
    else:
        ac = data["Accno"].iloc[-1]
    # add 1 in last account number
    acc = int(ac) + 1
    name = input("Enter the Name : ")
    type_acc = input("Enter S/C for Saving/Current Account : ")
    if (type_acc == 'S'):
        type_acc = "SAVING"
    else:
        type_acc = "CURRENT"

    bal = input("Enter the Balance : ")
    info = pd.DataFrame(columns=["Accno", "Name",
                                 "Typeacc", "Bal"])
    info = info.append({'Accno': acc, 'Name': name, 'Typeacc': type_acc, 'Bal': bal},
                       ignore_index=True)
    info.to_csv('bank.csv', index=False, mode='a', header=False)


def Main_Menu(ch):
    while (ch == 'Y' or ch == 'y'):
        print("Enter 1 : TO ADD NEW ACCOUNT")
        print("Enter 2 : TO VIEW CUSTOMER DEATILS ")
        print("Enter 3 : TO SEARCH CUSTOMER ")
        print("Enter 4 : TO DELETE CUSTOMER ACCOUNT ")
        print("Enter 5 : TO Update Name ")
        print("Enter 6 : TO Deposit Amount  ")
        print("Enter 7 : TO Withdraw Amount ")
        print("Enter 8 : TO Exit")

        try:  # Using Exceptions For Validation
            userInput = int(input("Please Select An Above Option: "))  # Will Take Input From User
        except ValueError:
            exit("\nHy! That's Not A Number")  # Error Message
        else:
            print("\n")  # Print New Line
        if (userInput == 1):
            add_account()
            # print("Add")
        elif (userInput == 2):
            view_account()
            # print("View")
        elif (userInput == 3):
            search_account()
            # print("Search")
        elif (userInput == 4):
            del_account()
            # print("Del")
        elif (userInput == 5):
            update_account()
            # print("Update Name ")
        elif (userInput == 6):
            deposit()
        elif (userInput == 7):
            withdraw()
        elif (userInput == 8):
            exit()

        else:
            print("Enter correct choice. . . ")


Main_Menu('Y')
