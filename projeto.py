#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 18:00:07 2018

@author: Débora Ferreira dos Santos e Túlio André Pereira de Oliveira
"""

#%% Import library

from matplotlib.pyplot import *
from numpy import *
from math import *

#%% Data initialization
x_values = [0.1, 1.0, 10.0]



#%% Define function to compute j's

table_up = [] #cria tabela vazia

#table[row][column]     
for x in x_values:
    
    row_up = [] #cria lista vazia
    #UP
    j_up_ant = sin(x)/x #j0
    row.append(j_up_ant) #adiciona item a lista
    j_up_atual = sin(x)/(x**2) - cos(x)/x #j1  
    row.append(j_up_atual) #adiciona item a lista  
    for l in range(2, 25): #Loop de 2 a 24 (0 e 1 já definidos, totalizando 25)
        j_up_prox = (2*l + 1)/x*j_up_atual - j_up_ant
        row.append(j_up_prox) #adiciona item a lista
        j_up_ant = j_up_atual 
        j_up_atual = j_up_prox
    
    table_up.append(row) #adiciona lista a tabela
     
    #DOWN    
    j_down_prox = j_up_atual
    j_down_atual = j_up_ant
    #guardar na tabela
    for l in range(23, 0, -1):
        j_down_ant = (2*l + 1)/x*j_down_atual - j_down_prox
        #guardar na tabela
        j_down_prox = j_down_atual 
        j_down_atual = j_down_ant
    
        #print j_down_atual


#%% Teste       
    
teste = [[00,01],[10,11],[20,21]]    
print 'x: ', teste[2][0]    


        
        
        
    