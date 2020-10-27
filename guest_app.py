#!/usr/bin/env python3

"""
Create a trackable guest list for an event that requires RSVPs.
Run in an HTML file or Web Hosted Server. SQLite3 is used for the table
creation and it is recommended to have a version of SQLite3 pre-installed.
SQLite3 is come preinstalled with most current Python 3.xx distrobutions.
Guest, Menu, menu_select, banner, add_guest, edit_guest, del_guest, num_generator
"""

import sqlite3
import os;
import sys;
from random import randint as ram;


__sql_file = "Guest_List.db"
conn = sqlite3,connect(__sql_file)
c = conn.cursor()

try:

    c.execute("""CREATE TABLE IF NOT EXISTS guest_list (
                 guest_id int,
                 first_name varchar(255),
                 last_name varchar(255),
                 phone_num varchar(15),
                 address varchar(255),
                 city varchar(255),
                 state varchar(255),
                 zip_code varchar(10),
                 email varchar(255),);"""
                 )
    conn.commit()

except:

    print("Table already Exists!")
    response = input("Delete this table? ('y' or 'n')")
    if response.lower() == 'y':
        c.execute("""DROP TABLE guest_list;""")
    else:
        raise

finally:

    conn.close()



class Guest:
  """
  Create the guest objects that get sent to the SQL database.
  Args(positional): fname: first name, lname: last name,
  number: A unique number generated from the num_generator function.
  """

    def __init__ (self,fname,lname,number)
        self.first = fname
        self.last = lname
        self.number = number


    def is_going(self, answer):
        """
        Allow for the RSVP response.
        Saved as 'Y or N'.
        """
        pass


    def how_many(self, party):

        """Enter how many
         will be attending
         with the guest."""

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
    print ("3. Delete Guest" + "\n" + "\n")
    r = int(input("Please make a selection: "))
    menu_select(r)

def screen_clear():
    os.system("clear");


def menu_select(s):
    if s== 1:
        banner("Add Guest to Registery")
        add_guest();
    elif s == 2:
        banner("Edit Guest")
        edit_guest()
    elif s == 3:
        banner("Delete Guest")
        del_guest()
    else:
        print ("Please make a valid selection: ")
        menu()


def add_guest():
    pass


def edit_guest():
    pass


def del_guest():
    pass


def num_generator():
    """
    Create a random
    5 digit number based
    on user input.

    """
    n = False
    while n is False:
        r = input("Make a selection: ")
        your_number = 0
        if r == 1:
            your_number = ram(10000, 19999)
            print your_number
            n = True

        elif r == 2:
            your_number = ram(20000, 29999)
            print your_number
            n = True

        elif r == 3:
            your_number = ram(30000, 39999)
            print your_number
            n = True
        else:
            print "Please make a valid selection"
            n = False


if __name__ is '__main__':
    menu()
