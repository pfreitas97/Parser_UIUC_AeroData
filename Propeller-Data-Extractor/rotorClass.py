#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:56:51 2020

@author: pedroaugustofreitasdearaujo
"""

class Rotor:
    
    name = ""
    
    def __init__(self, rotor_name,path_to_rotor_data):
        
        self.name = rotor_name
        
        self.path = path_to_rotor_data
        
        
    def returnNahmen(self):
        return self.name
    
    