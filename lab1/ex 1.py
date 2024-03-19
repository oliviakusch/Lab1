#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:09:28 2024

@author: oliviakusch
"""
### Exercise 1 ###

class WageCalculator:
    def __init__(self): # for when you want to make a function in itself, variables to be calculated
        self.hours = 0
        self.wages = 0
        
    def calc_gross_pay(self):
       return self.hours * self.wages

calculator = WageCalculator() #call function to be able to use 
calculator.hours = 35 #variable with function can be put aside the objects created in the class
calculator.wages = 12.5
gross_pay = calculator.calc_gross_pay() # made another variable with gross
print(gross_pay)






