# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:46:07 2020

@author: Michael
"""

from Hmis import Hmis

class Interim(Hmis):
    def __init__(self, client_uid='Null', ee_review_date='Null',
                 ee_review_added='Null', provider_creating='Null',
                 provider_updating='Null', review_type='Null',
                 user_creating='Null', user_updating='Null'):
        __ee_uid = 'Null'
        super().__init__(__ee_uid, client_uid)
        self.__ee_review_date = ee_review_date
        self.__ee_review_added = ee_review_added
        self.__provider_creating = provider_creating
        self.__provider_updating = provider_updating
        self.__review_type = review_type
        self.__user_creating = user_creating
        self.__user_updating = user_updating

    def get_ee_review_date(self):
        return self.__ee_review_date

    def get__ee_review_added(self):
        return self.__ee_review_added

    def get_provider_creating(self):
        return self.__provider_creating

    def get_provider_updating(self):
        return self.__provider_updating

    def get_review_type(self):
        return self.__review_type

    def get_user_creating(self):
        return self.__user_creating

    def get_user_updating(self):
        return self.__user_updating
