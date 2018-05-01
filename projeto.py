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
#Escolher x_values abaixo
#Valor do roteiro
x_values = [0.1, 1.0, 10.0]
#Valor para teste
#x_values = linspace(0.1,10.0,1)
table_up = []
table_down = []
table_down_normal = []
table_error = []
list_j0 = []
#Escolher l_axis abaixo
#Valor do roteiro
l_axis = range(0, 25) 
#Valor para teste
#l_axis = range(0,2)
#%% Define function to compute j's up
def compute_j_up():
    for x in x_values:       
        row_up = []                 
    
        j0 = sin(x)/x               #j0
        list_j0.append(j0)          #adiciona à lista de j0's

        j_up_ant = j0               
        row_up.append(j_up_ant)                         #adiciona à lista de js
        j_up_atual = sin(x)/(x**2) - cos(x)/x           #j1  
        row_up.append(j_up_atual)                       #adiciona à lista de js
        for l in range(2, size(l_axis)):                          #loop de 2 a 24
            j_up_prox = j_up_atual*(2*l + 1)/x - j_up_ant       #cálculo de js
            row_up.append(j_up_prox)                            #adiciona à lista de js
            j_up_ant = j_up_atual                       #atualiza o valor de jl-1
            j_up_atual = j_up_prox                      #atualiza o valor de jl
        
        table_up.append(row_up)     #adiciona a lista de js à tabela
     
#%% Define function to compute j's down
def compute_j_down():      
    for x in x_values:  
        row_down = []
        
        j_down_prox = size(l_axis)
        row_down.append(j_down_prox)
        j_down_atual = size(l_axis)         #TODO corrigir valor
        row_down.append(j_down_atual)
        for l in range((size(l_axis)-2), 0, -1):
            j_down_ant = j_down_atual*(2*l + 1)/x - j_down_prox
            row_down.append(j_down_ant)
            j_down_prox = j_down_atual 
            j_down_atual = j_down_ant
        
        row_down = list(reversed(row_down))         #Inverte ordem dos elementos
        table_down.append(row_down)                 #adiciona a lista de js à tabela
        
#%% Define function to normalize j's
## jl_nor = jl_comp * j0_analy/j0_comp
def normalize():
    for i in range(0,size(x_values)):
        row_normal = []
        for j in range(0,size(l_axis)):
            jl_normal = table_down[i][j] * list_j0[i] / table_down[i][0] 
            row_normal.append(jl_normal)
        table_down_normal.append(row_normal)

#%% Define function to calculate error
#abs( jup - jdown )/ ( abs(jup) + abs(jdown))
def calc_error():
    for i in range(0,size(x_values)):
        row_error = []
        for j in range(0,size(l_axis)):
            #print '%.20f' %( abs(table_up[i][j]) - abs(table_down_normal[i][j]) )
            if ( ( abs(table_up[i][j]) - abs(table_down_normal[i][j]) ) == 0 ):
                j_error = 0.005 #TODO corrigir só pra evitar float division by zero
            else:
                j_error = abs(table_up[i][j]- table_down_normal[i][j]) / ( abs(table_up[i][j]) - abs(table_down_normal[i][j]) ) 
            row_error.append(j_error)
        table_error.append(row_error)


#%% Define function to plot f(l)

def plot_l(table,y_label):
    for row in table:
        plot(l_axis,row)
    xlabel('Valores de l')
    ylabel(y_label)
    show()
     
#%% Define function to plot f(x)
    
def plot_x(table,y_label):
    for i in range(0,size(l_axis)):
        teste = []
        for j in range(0,size(x_values)):
            teste.append(table[j][i])
        plot(x_values,teste)
    xlabel('Valores de x')
    ylabel(y_label)
    show()    
    
#%% Teste       

compute_j_up()
compute_j_down()
normalize()
calc_error()
plot_l(table_up,'jl(x) (up)')
plot_l(table_down_normal,'jl(x) (down)')
plot_l(table_error,'Erro relativo')
plot_x(table_down_normal,'jl(x) down')
plot_x(table_up,'jl(x) up')
#%% Main 
   