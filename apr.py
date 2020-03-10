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
        clients_list.append(Client(contents[x][0], contents[x][1], contents[x][2],
                               contents[x][3], contents[x][4], contents[x][5],
                               contents[x][6], contents[x][7], contents[x][8],
                               contents[x][9], contents[x][10], contents[x][11],
                               contents[x][12], contents[x][13], contents[x][14],
                               contents[x][15], contents[x][16]))   
    return clients_list

def create_enrollment_objects():
    '''
    This function will create enrollment objects from a read file
    and return a nested list
    '''
    # Declare Variables
    enrollment_list = []

    contents = read_file('Enrollment Table1.csv')
    contents2 = read_file('Enrollment Table2.csv')
    contents3 = read_file('Enrollment Table3.csv')
    contents.extend(contents2)
    contents.extend(contents3)   

    # Create Client Objects
    for x in range(0, len(contents)):
        enrollment_list.append(Enrollment(contents[x][0], contents[x][1], contents[x][2],
                               contents[x][3], contents[x][4], contents[x][5],
                               contents[x][6], contents[x][7], contents[x][8],
                               contents[x][9], contents[x][10], contents[x][11],
                               contents[x][12], contents[x][13], contents[x][14],
                               contents[x][15], contents[x][16],
                               contents[x][17]))   
    return enrollment_list

def create_exit_objects():
    '''
    This function will create exit objects from a read file
    and return a nested list
    '''
    # Declare Variables
    exit_list = []

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
        interim_list.append(Interim(contents[x][0], contents[x][1], contents[x][2],
                               contents[x][3], contents[x][4], contents[x][5],
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
    
    enrollment = create_enrollment_objects()

    start, end = set_report_range()
   
    for x in range(len(enrollment)):
        if (enrollment[x].get_provider() == 'AL500 - First Light (ES)(800)' and 
            datetime.strptime(enrollment[x].get_ee_entry_date(), '%m/%d/%Y').date() < end
            and datetime.strptime(enrollment[x].get_ee_entry_date(), '%m/%d/%Y').date() > start):
            clients_served.append(enrollment[x].get_ee_uid())
    
    print('Total Number of Persons Served: {0}'.format(len(clients_served)))