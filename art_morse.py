#!/usr/bin/env python3

"""Module to make our own Art Morse Code."""

__author__ = 'Jeffrey Ochoa'
__date__ = '01/31/2022'

morsecode = input('Please enter code:')
print()

if morsecode == '....':
    print('the code translate to @')
elif morsecode == '...-':
    print('the code translate to >')
elif morsecode == '..-.':
    print('the code translate to <')
elif morsecode == '..--':
    print('the code translate to -')
elif morsecode == '.-..':
    print('the code translate to (')
elif morsecode == '.-.-':
    print('the code translate to )')
elif morsecode == '.--.':
    print('the code translate to ^')
elif morsecode == '.---':
    print('the code translate to _')
elif morsecode == '-...':
    print('the code translate to ''')
elif morsecode == '-..-':
    print('the code translate to "')
elif morsecode == '-.-.-':
    print('the code translate to |')
elif morsecode == '-.--':
    print('the code translate to =')
else:
    print('invalid code')