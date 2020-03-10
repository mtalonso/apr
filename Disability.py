# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:40:59 2020

@author: Michael
"""

from Hmis import Hmis

class Disability(Hmis):
    def __init__(self, ee_id='Null', client_uid='Null', disability='Null',
                 disability_id='Null', provider='Null', disability_type='Null',
                 disability_determination='Null', disability_start='Null',
                 disability_end='Null', disability_added='Null'):
        super().__init__(ee_id, client_uid)
        self.__disability = disability
        self.__disability_id = disability_id
        self.__provider = provider
        self.__disability_type = disability_type
        self.__disability_determination = disability_determination
        self.__disability_start = disability_start
        self.__disability_end = disability_end
        self.__disability_added = disability_added

    def get_disability(self):
        return self.__disability

    def get_disability_id(self):
        return self.__disability_id

    def get_provider(self):
        return self.__provider

    def get_disability_type(self):
        return self.__disability_type    

    def get_disability_determination(self):
        return self.__disability_determination

    def get_disability_start(self):
        return self.__disability_start

    def get_disability_end(self):
        return self.__disability_end

    def get_disability_added(self):
        return self.__disability_added