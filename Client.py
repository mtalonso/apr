# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 13:20:14 2020

@author: Michael
"""

from Hmis import Hmis

class Client(Hmis):
    
    def __init__(self, ssn='Null',  client_suffix='Null', last='Null',
                 ssn_quality='Null', first='Null', name_quality='Null', 
                 ee_id='Null', client_uid='Null', middle_name='Null',
                 alias='Null', veteran='Null', dob='Null', age='Null',
                 gender='Null', race='Null', secondary_race='Null',
                 ethnicity='Null'):
        super().__init__(ee_id, client_uid)
        self.__ssn = ssn
        self.__client_suffix = client_suffix
        self.__last = last
        self.__ssn_quality = ssn_quality
        self.__first = first
        self.__name_quality = name_quality
        self.__middle_name = middle_name
        self.__alias = alias
        self.__veteran = veteran
        self.__dob = dob
        self.__age = age
        self.__gender = gender
        self.__race = race
        self.__secondary_race = secondary_race
        self.__ethnicity = ethnicity
    
    def get_ssn(self):
        return self.__ssn

    def get_client_suffix(self):
        return self.__client_suffix

    def get_last(self):
        return self.__last

    def get_ssn_quality(self):
        return self.__ssn_quality

    def get_first(self):
        return self.__first

    def get_name_quality(self):
        return self.__name_quality

    def get_middle_name(self):
        return self.__middle_name

    def get_alias(self):
        return self.__alias

    def get_veteran(self):
        return self.__veteran

    def get_dob(self):
        return self.__dob

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_race(self):
        return self.__race

    def get_secondary_race(self):
        return self.__secondary_race

    def get_ethnicity(self):
        return self.__ethnicity

    def __str__(self):
        return '{}'.format(super().get_client_uid())