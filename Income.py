#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 15:57:42 2020

@author: michael
"""

from Hmis import Hmis

class Income(Hmis):
    def __init__(self, ee_id, client_uid, any_income, income_id,
                 provider, source, receiving_income, monthly_amount,
                 start_date, end_date, date_added):
        super().__init__(ee_id, client_uid)
        self.__any_income = any_income
        self.__income_id = income_id
        self.__provider = provider
        self.__source = source
        self.__receiving_income = receiving_income
        self.__monthly_amount = monthly_amount
        self.__start_date = start_date
        self.__end_date = end_date
        self.__date_added = date_added

    def get_any_income(self):
        return self.__any_income

    def get_income_id(self):
        return self.__income_id

    def get_provider(self):
        return self.__provider

    def get_source(self):
        return self.__source

    def get_receiving_income(self):
        return self.__receiving_income

    def get_monthly_amount(self):
        return self.__monthly_amount

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_date_added(self):
        return self.__date_added
