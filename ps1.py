# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 18:53:04 2018

@author: Boran
"""

annual_salary = int(input("The starting annual salary: "))
portion_saved = float(input("The portion of salary to be saved: "))
total_cost = int(input("The cost of your dream home: "))
semi_annual_rate = float(input("Enter the semi­annual raise, as a decimal: "))
n=0
current_savings=0
while(current_savings<=total_cost*1/4):
    n = n + 1
    if (n % 6 == 1) and (n != 1):
        annual_salary=annual_salary*(1+semi_annual_rate)
    current_savings = current_savings + current_savings * 4/100 * 1/12 + annual_salary * portion_saved * 1/12  
print(n)


annual_salary = int(input("The starting annual salary: "))
annual_salary_first = annual_salary
p_max = 10000
p_min = 0
p_mid = (p_max + p_min)/2
total_cost = 1000000
semi_annual_rate = 0.07
epsilon=100.00000
current_savings=0
num_bisection=0
while abs(current_savings - total_cost*1/4) >= epsilon:
    current_savings = 0
    annual_salary = annual_salary_first
    p_mid = (p_max + p_min)/2
    num_bisection += 1
    for i in range(36):
        if (i % 6 == 0) and (i != 0):
            annual_salary = annual_salary * (1+semi_annual_rate)
        current_savings = current_savings + annual_salary * 1/12 * p_mid * 1/100 + current_savings * 0.04 * 1/12
        if (current_savings - total_cost * 1/4) > epsilon:
            break
    if current_savings > total_cost*1/4:
        p_max = p_mid
    else:
        p_min = p_mid
p_mid = p_mid/100
p_mid = round(p_mid,4)
if p_mid > 0.5:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: ", p_mid)
    print("Steps in bisection search: ", num_bisection)