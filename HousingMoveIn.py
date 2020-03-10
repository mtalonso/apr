# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:28:28 2020

@author: Michael
"""

from Hmis import Hmis

class HousingMoveIn(Hmis):
    def __init__(self, client_id='Null', move_in_date='Null', ee_id='Null',
                 ee_review_id='Null'):
        super().__init__(ee_id, client_id)
        self.__move_in_date = move_in_date
        self.__ee_review_id = ee_review_id