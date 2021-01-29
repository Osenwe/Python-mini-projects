# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:38:40 2021

@author: hp
"""


def arithmetic_arranger(problems, display = None):
    arranged_list_upper = ''
    arranged_list_lower = ''
    arranged_list_dashes = ''
    arranged_list_solution = ''
    arranged_problems = ''
    upper = []
    lower = []
    sums = []
    operators =  []
    max_length = []
    is_character_a_digit = []
    Character_length = []
    
    if len(problems) > 5:
        error_message = 'Error: Too many problems.'
        return error_message
    else:
            for prob in problems:
                try:
                    if '+' in prob:
                        separate = prob.partition('+')
                        #up, op,and bt signifies the number to be added and the operator
                        up = separate[0].strip(' ')
                        bt = separate[2].strip(' ')
                        op = separate[1].strip(' ')
                        
                        is_character_a_digit.append(up.isdigit())
                        Character_length.append(len(up) > 4)
                        is_character_a_digit.append(bt.isdigit())
                        Character_length.append(len(bt) > 4)
                        
                        upper.append(up)
                        lower.append(bt)
                        operators.append(op)
                        max_length.append(max([len(up), len(bt)]))
                        
                    elif '-' in prob:
                        separate = prob.partition('-')
                        up = separate[0].strip(' ')
                        bt = separate[2].strip(' ')
                        op = separate[1].strip(' ')
                        
                        is_character_a_digit.append(up.isdigit())
                        Character_length.append(len(up) > 4)
                        is_character_a_digit.append(bt.isdigit())
                        Character_length.append(len(bt) > 4)
                        
                        upper.append(up)
                        lower.append(bt)
                        operators.append(op)
                        max_length.append(max([len(up), len(bt)]))
                    else:
                        raise TypeError
                except:
                    return 'Error: Operator must be '+' or '-'.'
    
    if all(is_character_a_digit) == False: 
        return 'Error: Numbers must only contain digits.'      

    elif any(Character_length):
        return 'Error: Numbers cannot be more than four digits.'
    
    else:
        sums = [int(up)+int(bt) if op=='+' else int(up)-int(bt) for up, bt, op in zip(upper, lower, operators)]
        sum_as_string = [str(sm) for sm in sums]
        
        for item in range(len(sums)):
        #for this loop any of the list created here will have the same result because they all have the same length
            up = upper[item]
            bt = lower[item]
            op = operators[item]
            sol = sum_as_string[item]
            mx = max_length[item]
            mxd = mx +  2
            arranged_list_upper += '  ' + '{}'.format(up).rjust(mx) + '    '
            arranged_list_lower += '{} '.format(op) + '{}'.format(bt).rjust(mx) + '    '
            arranged_list_dashes += '-' * mxd + '    '
            arranged_list_solution += '{}'.format(sol).rjust(mxd) + '    '
            
        arranged_problems = arranged_list_upper + '\n' + arranged_list_lower + '\n' + arranged_list_dashes 
    
        #The prints here is to ensure that the code is correct at all points     
        #print(arranged_list_upper)
        #print(arranged_list_lower)
        #print(arranged_list_dashes)
        #print(arranged_list_solution)
        #print(sum_as_string)
        #print(max_length)
        #print(sums)
        #print(upper)
        #print(lower)
        #print(operators)'''
        #print(is_character_a_digit)
        #print(Character_length)
        
        if display == True:
            return arranged_problems  + '\n' + arranged_list_solution
        else:
            return arranged_problems           
 
    

    

x = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
print(x)