# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:55:35 2022

@author: sklad_2
"""

from application.salary import calculater_salary
from application.db.people import get_employes

if __name__ =='__main__':
    calculater_salary()
    get_employes()