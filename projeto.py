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
table_down = []
table_down_normal = []
list_j0 = []
x_axis = range(0, 25)

#%% Define function to compute j's up
def compute_j_up():
    for x in x_values:       
        row_up = [] #cria lista vazia
    
        #Calculates j0
        j0 = sin(x)/x
        list_j0.append(j0)
        
        j_up_ant = j0     #j0
        row_up.append(j_up_ant)     #adiciona item a lista
        j_up_atual = sin(x)/(x**2) - cos(x)/x   #j1  
        row_up.append(j_up_atual)   #adiciona item a lista  
        for l in range(2, 25):  #Loop de 2 a 24 (0 e 1 já definidos, totalizando 25)
            j_up_prox = (2*l + 1)/x*j_up_atual - j_up_ant
            row_up.append(j_up_prox)    #adiciona item a lista
            j_up_ant = j_up_atual 
            j_up_atual = j_up_prox
        
        table_up.append(row_up)     #adiciona lista a tabela
     
#%% Define function to compute j's down
def compute_j_down():      
    for x in x_values:  
        row_down = []
        
        j_down_prox = 2000 #TODO corrigir valor
        row_down.append(j_down_prox)
        j_down_atual = 2000 #TODO corrigir valor
        row_down.append(j_down_atual)
        for l in range(23, 0, -1):
            j_down_ant = (2*l + 1)/x*j_down_atual - j_down_prox
            row_down.append(j_down_ant)
            j_down_prox = j_down_atual 
            j_down_atual = j_down_ant
        
        row_down = list(reversed(row_down)) #Muda a ordem dos elementos, pra deixar de 1 a 25 e nao de 25 a 1 como estava

        table_down.append(row_down) #append linha na tabela
        
#%% Define function to normalize j's
def normalize():
    for i in range(0,3):
        row_normal = []
        for j in range(0,25):
           jl_normal = table_down[i][j] * list_j0[i] / table_down[i][0] # jl_nor = jl_comp * j0_analy/j0_comp
           row_normal.append(jl_normal)
        table_down_normal.append(row_normal)


#%% Define function to plot graphs

def plot_():
    for row in table_up:
        plot(x_axis,row)
        hold('on')

     
#%% Teste       
compute_j_up()      

plot_()
#%% Main 

calculation()
    
        
    