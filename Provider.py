# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:01:13 2020

@author: Michael
"""

class Provider:
    def __init__(self, provider, provider_id, provider_type='Null'):
        self.__provider = provider
        self.__provider_id = provider
        self.__provider_type = provider_type

    def get_provider(self):
        return self.__provider

    def get_provider_id(self):
        return self.__provider_id

    def get_provider_type(self):
        return self.__get_provider_type