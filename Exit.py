# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:32:08 2020

@author: Michael
"""

from Hmis import Hmis

class Exit(Hmis):
    def __init__(self, ee_id='Null', ee_date_updated='Null',
                 ee_no_exit='Null', destination='Null', exit_date='Null',
                 reason='Null', destination_other='Null', reason_other='Null'):
        super().__init__(ee_id, client_uid='Null')
        self.__ee_date_updated = ee_date_updated
        self.__ee_no_exit = ee_no_exit
        self.__destination = destination
        self.__exit_date = exit_date
        self.__reason = reason
        self.__destination_other = destination_other
        self.__reason_other = reason_other

    def get_ee_date_updated(self):
        return self.__ee_date_updated

    def get_ee_no_exit(self):
        return self.__ee_no_exit

    def get_destination(self):
        return self.__destination

    def get_exit_date(self):
        return self.__exit_date

    def get_reason(self):
        return self.__reason

    def get_destination_other(self):
        return self.__destination_other

    def get_reason_other(self):
        return self.__reason_other
