# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:17:14 2020

@author: Michael
"""

from Hmis import Hmis
from datetime import datetime

class Enrollment(Hmis):

    def __init__(self, ee_id='Null', user='Null', client_id='Null',
                 provider='Null', approx_date_homeless='Null',
                 disability='Null', ee_entry_date='Null', start_date='Null',
                 ee_household_id='Null', months_homeless='Null', los='Null',
                 es_or_sh='Null', times_homeless='Null', relation_to_hoh='Null',
                 prior_living='Null', total_months_homeless='Null', age='Null',
                 provider_type='Null'):
        super().__init__(ee_id, client_id)
        self.__user = user
        self.__provider = provider
        self.__approx_date_homeless = approx_date_homeless
        self.__disability = disability
        self.__ee_entry_date = ee_entry_date
        self.__start_date = start_date
        self.__ee_household_id = ee_household_id
        self.__months_homeless = months_homeless
        self.__los = los
        self.__es_or_sh = es_or_sh
        self.__times_homeless = times_homeless
        self.__relation_to_hoh = relation_to_hoh
        self.__prior_living = prior_living
        self.__total_months_homeless = total_months_homeless
        self.__age = age
        self.__provider_type = provider_type


    def get_user(self):
        return self.__user

    def get_provider(self):
        return self.__provider

    def get_approx_date_homeless(self):
        return self.__approx_date_homeless

    def get_disability(self):
        return self.__disability

    def get_ee_entry_date(self):
        return self.__ee_entry_date

    def get_start_date(self):
        return self.__start_date

    def get_ee_household_id(self):
        return self.__ee_household_id

    def get_months_homeless(self):
        return self.__months_homeless

    def get_los(self):
        return self.__los

    def get_es_or_sh(self):
        return self.__es_or_sh

    def get_times_homeless(self):
        return self.__times_homeless

    def get_relation_to_hoh(self):
        return self.__relation_to_hoh

    def get_prior_living(self):
        return self.__prior_living

    def get_total_months_homeless(self):
        return self.__total_months_homeless

    def get_age(self):
        return self.__age

    def get_provider_type(self):
        return self.__provider_type