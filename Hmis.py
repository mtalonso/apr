# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:19:24 2020

@author: Michael
"""

class Hmis():
    def __init__(self, ee_uid='Null', client_uid='Null'):
        self.__ee_uid = ee_uid
        self.__client_uid = client_uid
    
    def get_ee_uid(self):
        return self.__ee_uid

    def get_client_uid(self):
        return self.__client_uid