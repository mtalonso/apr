# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:50:51 2020
@author: Michael
"""

# import
from Client import Client
from Enrollment import Enrollment
from Exit import Exit
from HousingMoveIn import HousingMoveIn
from Interim import Interim
from Provider import Provider
from datetime import datetime
import sys


# Functions
def read_file(file_name):
    '''
    This function will read the passed file and return a nested list
    '''
    # Reading file and making a nested list variable
    with open(file_name, "r") as open_file:
        inventory_list = [[name for name in line.split(',')]
                          for line in open_file]
    # Close File
    open_file.close()

    # Assign Null Values
    for x in range(len(inventory_list)):
        for i in range(len(inventory_list[0])):
            if inventory_list[x][i] == '':
                inventory_list[x][i] = 'Null'

    return inventory_list


def create_client_objects():
    '''
    This function will create client objects from a read file
    and return a nested list
    '''
    # Declare Variables
    clients_list = []
    contents = []
    contents = read_file('Client Table.csv')

    # Create Client Objects
    for x in range(0, len(contents)):
        clients_list.append(Client(contents[x][0], contents[x][1],
                                   contents[x][2], contents[x][3],
                                   contents[x][4], contents[x][5],
                                   contents[x][6], contents[x][7],
                                   contents[x][8], contents[x][9],
                                   contents[x][10], contents[x][11],
                                   contents[x][12], contents[x][13],
                                   contents[x][14], contents[x][15],
                                   contents[x][16]))
    return clients_list


def create_enrollment_objects():
    '''
    This function will create enrollment objects from a read file
    and return a nested list
    '''
    # Declare Variables
    enrollment_list = []

    # Reading files and combining lists
    contents = read_file('Enrollment Table1.csv')
    contents2 = read_file('Enrollment Table2.csv')
    contents3 = read_file('Enrollment Table3.csv')
    contents.extend(contents2)
    contents.extend(contents3)

    # Create Client Objects
    for x in range(0, len(contents)):
        enrollment_list.append(Enrollment(contents[x][0], contents[x][1],
                                          contents[x][2], contents[x][3],
                                          contents[x][4], contents[x][5],
                                          contents[x][6], contents[x][7],
                                          contents[x][8], contents[x][9],
                                          contents[x][10], contents[x][11],
                                          contents[x][12], contents[x][13],
                                          contents[x][14], contents[x][15],
                                          contents[x][16], contents[x][17]))
    return enrollment_list


def create_exit_objects():
    '''
    This function will create exit objects from a read file
    and return a nested list
    '''
    # Declare Variables
    exit_list = []

    # Reading files and combining lists
    contents = read_file('Exit Table1.csv')
    contents2 = read_file('Exit Table2.csv')
    contents3 = read_file('Exit Table3.csv')
    contents.extend(contents2)
    contents.extend(contents3)

    # Create Client Objects
    for x in range(0, len(contents)):
        exit_list.append(Exit(contents[x][0], contents[x][1], contents[x][2],
                              contents[x][3], contents[x][4], contents[x][5],
                              contents[x][6]))
    return exit_list


def create_housing_move_in_objects():
    '''
    This function will create housing move in objects from a read file
    and return a nested list
    '''
    # Declare Variables
    move_in_list = []

    # Reading files and combining lists
    contents = read_file('Move In Table1.csv')
    contents2 = read_file('Move In Table2.csv')
    contents3 = read_file('Move In Table3.csv')
    contents.extend(contents2)
    contents.extend(contents3)

    # Create Client Objects
    for x in range(0, len(contents)):
        move_in_list.append(HousingMoveIn(contents[x][0], contents[x][1], contents[x][2],
                                          contents[x][3]))
    return move_in_list

def create_interim_objects():
    '''
    This function will create interim objects from a read file
    and return a nested list
    '''
    # Declare Variables
    interim_list = []
    contents = read_file('Interim Table.csv')

    # Create Client Objects
    for x in range(0, len(contents)):
        interim_list.append(Interim(contents[x][0], contents[x][1],
                                    contents[x][2], contents[x][3],
                                    contents[x][4], contents[x][5],
                                    contents[x][6], contents[x][7]))
    return interim_list


def create_provider_objects():
    '''
    This function will create provider objects from a read file
    and return a nested list
    '''
    # Declare Variables
    provider_list = []
    contents = read_file('Providers Table.csv')

    # Create Client Objects
    for x in range(0, len(contents)):
        provider_list.append(Provider(contents[x][0], contents[x][1],
                                      contents[x][2]))
    return provider_list


def set_report_range():
    '''
    This function will set the report range
    '''
    while True:
        start = input('Enter Report Start Date (m/d/yyyy): ').strip()
        try:
            start = datetime.strptime(start, '%m/%d/%Y').date()
            break
        except:
            print('Invalid date, Please try again.')

    while True:
        end = input('Enter Report End Date (m/d/yyyy): ').strip()
        try:
            end = datetime.strptime(end, '%m/%d/%Y').date()
            break
        except:
            print('Invalid date, Please try again.')

    return start, end


def get_index_number(provider_list, provider_code):
    '''
    This function checks to see if a value is in the passed object list
    and returns the integer index position and boolean value
    '''
    # Define variables
    present = False
    index = None

    # Searching object list for a match to passed argument name
    for x in range(len(provider_list)):
        if provider_code == provider_list[x].get_provider_id():
            index = x
            present = True

    return index, present


def get_provider_name():
    '''
    This function will use the provider code to return the provider name
    '''
    # Collecting and validating input
    while True:
        provider_code = input('Enter the Provider Number: ')
        try:
            provider_code = int(provider_code)
            break
        except:
            print('Invalid provider code entered. Please try again.')

    # Call to function to return list index position and boolean value
    index, present = get_index_number(providers, provider_code)

    # Validating provider code is in provider list
    if present is False:
        print('Invalid provider code. Please try again.')
        sys.exit()
    else:
        provider_name = providers[index].get_provider()

    return provider_name


def get_clients_served(enrollment_list, provider_name, start, end):
    '''
    This function will calculate the number of clients served
    '''
    # Declare variables
    served_list = []

    # Count clients with correct provider name and report range
    for x in range(len(enrollment_list)):
        if (enrollment_list[x].get_provider() == provider_name and
                datetime.strptime(enrollment_list[x].get_ee_entry_date(),
                                  '%m/%d/%Y').date() < end
                and datetime.strptime(enrollment_list[x].get_ee_entry_date(),
                                      '%m/%d/%Y').date() > start):
            served_list.append(enrollment[x].get_ee_uid())

    return served_list


# Begin Program
if __name__ == '__main__':
    # Declare Variables
    contents = []
    clients = []
    enrollment = []
    disability = []
    exit_table = []
    move_in_table = []
    income = []
    interim = []
    providers = []
    clients_served = []

    # Create object lists
    enrollment = create_enrollment_objects()
    providers = create_provider_objects()

    # Get Start and End dates. Get Provider Name
    start, end = set_report_range()
    provider_name = get_provider_name()

    # Retrieve clients served and print to console
    clients_served = get_clients_served(enrollment, provider_name, start, end)
    print('Total Number of Persons Served: {0}'.format(len(clients_served)))
