#!/usr/bin/env python3

import sqlite3
import os;
import sys;
from random import randint as ram;

guest_builder = {}

unique = False

__sql_file = "guest_list_db.sqlite"

conn = sqlite3,connect(__sql_file)

c = conn.cursor()

try:

    c.execute("""CREATE TABLE guest_list (
                 ID int NOT NULL,
                 FirstName varchar(255) NOT NULL,
                 LastName varchar(255) NOT NULL,
                 HomeState varchar(255) NOT NULL,
                 Wedding varchar(255) NULL,
                 OHR varchar(255) NULL,
                 IL-R varchar(255) NULL,);"""
    )
    conn.commit()

except:

    print("Table already Exists!")

finally:

    conn.close()



class Guest:

 
    def __init__ (self, fname = Our, lname = Guest,
                  state = NC, number = 99999)

        self.first = fname
        self.last = lname
        self.number = number
        self.state = state

        try:
            c.execute("""INSERT INTO GUEST_LIST VALUES ( 
                      {n}, {f}, {l}, {s}, NULL, NULL, 
                      NULL);""".format(n = number, 
                                         f= fname, 
                                         l =lname,
                                         s =state))

            com.commit()

        except:
            print("Guest already exsists in Table!")

        fianlly:
            conn.close
            menu()


    def is_going(self):

        pass


    def how_many(self):

        pass

title = "Welcome to the Wedding Registry!"


def banner(message = title, border = "-"):

    ends = "+"
    tframe = border * len(message)
    mframe = "|" + message + "|"
    bframe = border * len(message)
    print ( ends + tframe + ends)
    print (mframe)
    print (ends + bframe + ends + "\r\r")


def menu():
    banner()
    print ("1. Add Guest")
    print ("2. Edit Guest ")
    print ("3. List Guests")
    print ("Press 'Q' at antime to exit \n\n")
    r = input("Please make a selection: ")
    menu_select(r)

clear = lambda: os.system("clear")
  

def menu_select(s):
    if s in ("1", "01"):
        clear()
        banner("Add Guest")
        add_guest()
    elif s in ("2", "02"):
        clear()
        banner("Edit Guest")
        edit_guest()
    elif s in ("3", "03"):
        clear()
        banner("List Guests")
        list_guest()
    elif s in ("Q", "q"):
        clear()
        sys.exit()
    else:
        print ("Please make a valid selection.")
        clear()
        menu()

guest_builder = {}

def add_guest():
    f = input("Enter guest's first name: ")
    if len(f) == 0 :
        while len(f) == 0:
            print("A valid name is required to" \
               "continue.")
            input("Enter guest's first name: ") 
    else:
        guest_builder["fname"] = f 
        l = input("Enter guest's last name: ")
        if len(l) == 0 :
            while len(l) == 0:
                print("A valid last name or initial" \
                      "is required to continue.")
                input(" ")
        else:
           guest_builder["lname"] = l
           s = input("Enter guest's State: ")
           if len(s) < 2 :
               print("A valid state is required to" \
                              "continue.")
           else:
               guest_builder["state"] = s
               guest_number()
               print(guest_builder)
               
    


def edit_guest():
    pass


def list_guests():
    pass


def del_guest():
    pass


def guest_number():
        banner("Registration Number")
        print("\n") 
        print("1. Add Guest to Ceremony")
        print("2. Add Guest to IL Reception")
        print("3. Add Guest to OH Reception")
        print("Enter 'Q' to return to the previous menu." + "\n")
        x = next(num_generator(input("Make a selection: ")))
        is_unique(x)
        if unique:
            guest_builder["number"] = x
        else:
            while unique is False:
            print("The registration number generated was not unique." \
                  "Let's try again.")
            guest_number()
        
    

def num_generator(r):

    n = False
    while n is False:
        your_number = 0
        if r in ("1", "01"):
            your_number = ram(10000, 19999)
            yield your_number
            n = True

        elif r in ("2", "02"):
            your_number = ram(20000, 29999)
            yield your_number
            n = True

        elif r in ("3", "03"):
            your_number = ram(30000, 39999)
            yield your_number
            n = True
        elif r in ("q", "Q"):
            menu()
        else:
            print ("Please make a valid selection")
            clear()
            guest_number()
            n = False


def is_unique(num)
    c.execute("""SELECT number FROM guest_list;""")
    results = c.fetchall()
    conn.close()
    if num in results:
        unique = False
    else:
        unique = True
    


if __name__ == '__main__':
    menu()
