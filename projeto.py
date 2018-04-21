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
table_up = []
x_axis = range(0, 25)


#%% Define function to compute j's
def calculation():
    #table_up = [] #cria tabela vazia #TODO mover para inicialização de dados, global
    
    #table[row][column]     
    for x in x_values:
        
        row_up = [] #cria lista vazia
        #UP
        j_up_ant = sin(x)/x     #j0
        row_up.append(j_up_ant)     #adiciona item a lista
        j_up_atual = sin(x)/(x**2) - cos(x)/x   #j1  
        row_up.append(j_up_atual)   #adiciona item a lista  
        for l in range(2, 25):  #Loop de 2 a 24 (0 e 1 já definidos, totalizando 25)
            j_up_prox = (2*l + 1)/x*j_up_atual - j_up_ant
            row_up.append(j_up_prox)    #adiciona item a lista
            j_up_ant = j_up_atual 
            j_up_atual = j_up_prox
        
        table_up.append(row_up)     #adiciona lista a tabela
         
        #DOWN    
        j_down_prox = j_up_atual
        j_down_atual = j_up_ant
        #guardar na tabela
        for l in range(23, 0, -1):
            j_down_ant = (2*l + 1)/x*j_down_atual - j_down_prox
            #guardar na tabela
            j_down_prox = j_down_atual 
            j_down_atual = j_down_ant
        j_down_zero = j_down_atual #TODO global ou então return, valor a ser usado na normalização
        
            #print j_down_atual

#%% Define function to normalize down recursion




#%% Define function to plot graphs

def plot_():
    for row in table_up:
        plot(x_axis,row)
        hold('on')

     
#%% Teste       
calculation()      

plot_()
#%% Main 

calculation()
    
        
    