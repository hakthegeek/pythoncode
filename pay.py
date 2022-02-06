#!/usr/bin/env python3

"""Module to calculate the amount of an employee’s paycheck."""

__author__ = 'Jeffrey Ochoa'
__date__ = '01/31/2022'

#input for hourly(h) or salary (s)
toe = input("Are you a Salary Employee?: ")

#for the salary  employees
if toe == ("yes"): # they are a salary employee
    print('You are a Salary Employee. ')
    srate = (float(input('What is your rate of pay?: ')))
    stotal = round(40*srate,2)
    print('Your weekly pay is:  $',stotal)
    
else: toe == ("no")
print('You are a Hourly Employee.')
hepayrate = (float(input('What is your hourly rate?: ')))
hehours = (float(input('How many Hours are you working?: ')))
if hehours < 40:
        regularpay = round(hehours * hepayrate, 2)
        holiquest = input('Are these Holiday Hours?: ')
        if holiquest == ("yes"):
                tpay = round(regularpay*2, 2)
                print('Your weekly pay is:  $',tpay)
        else: holiquest == ("no")
        print('Your weekly pay is: $',regularpay)
else: hehours > 40
regtpay = hepayrate*40
ot = hehours-40
otrate = hepayrate*1.5
otpay = round(otrate*ot, 2)
gpay = round(regtpay+otpay, 2)
otholiquest = input('Are these Holiday Hours?: ')
if otholiquest == ("yes"):
                othpay = round(gpay*2, 2)
                print('Your weekly pay is : $' ,othpay)
else: otholiquest == ('no')
print('Your weekly pay is: $' ,gpay)
