# Rules
# The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that 
# describes an error that is meaningful to the user.

# Example Output:
#    32         1      9999      523
#  +  8    - 3801    + 9999    -  49
#  ----    ------    ------    -----
#    40     -3800     19998      474

# Situations that will return an error:
#   - If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
#   - The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. 
#     Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
#   - Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
#   - Each operand (aka number on each side of the operator) has a max of four digits in width. 
#     Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'

# If the user supplied the correct format of problems, the conversion you return will follow these rules:
#   - There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, 
#     both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
#   - Numbers should be right-aligned.
#   - There should be four spaces between each problem.
#   - There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. 
#     (The example above shows what this should look like.)


problems = []

def arithmetic_arranger(problems, answers = False):
    expression = []
    response = ''
    operand_one = 0
    operand_two = 0
    operator = ''
    result = 0
    
    # Verifies if there are more than 5 operations. 
    if len(problems) > 5:
        response = 'Error: Too many problems.'
    elif len(problems) <= 5:
        amount_problems = len(problems)
        
        # Iterates over each problem provided, seperately.
        while amount_problems > 0 :
            for problem in problems:
                expression = problem.split()
                operand_one = int(expression[0])
                operator = expression[1]
                operand_two = int(expression[2])
                if operator == '+':
                    result = operand_one + operand_two
                elif operator == '-':
                    result = operand_one - operand_two
                
                # Verifies that operands are only digits
                if type(operand_one) and type(operand_two) == int:
                    
                    # Verifies that each operand has 4 or less digits
                    if len(str(operand_one)) > 4 or len(str(operand_two)) > 4:
                        response = 'Error: Numbers cannot be more than four digits.'
                    else:
                        
                        # Verifies that the operator is either a summation or subtraction operator.
                        if operator == '+' or operator == '-':
                            
                            # Vertical formatter function that segments the current expression into vertical layers
                            def vertical_formatter(operand_one, operator, operand_two):
                                top_layer = ''
                                middle_layer = ''
                                bottom_layer = ''
                                reformatted_expression = ''
                                
                                # Operand formatter function that converts operands into a string with a maximum length of 4   
                                def operand_formatter(operand):
                                    operand_spaces = 4 - len(str(operand))
                                    if operand_spaces == 0:
                                        return str(operand)
                                    elif operand_spaces == 1:
                                        return str(operand)+' '
                                    elif operand_spaces == 2:
                                        return str(operand)+'  '
                                    elif operand_spaces == 3:
                                        return str(operand)+'   '
                                    
                                reformatted_operand_one = operand_formatter(operand_one)
                                reformatted_operand_two = operand_formatter(operand_two)

                                # Conditional checkpoint that verifies whether an unformatted operand in the expression is a length of 4, 3, or 2 in order 
                                # to format appropriately.     
                                if len(str(operand_one)) == 4 or len(str(operand_two)) == 4:
                                    top_layer = f'\n  {reformatted_operand_one}'
                                    middle_layer = f'{reformatted_operand_two} {operator}\n------'
                                    bottom_layer = result
                                    if answers == True:
                                        reformatted_expression = f'{top_layer}\n{middle_layer}\n{bottom_layer}'
                                    else:
                                        reformatted_expression = f'{top_layer}\n{middle_layer}'
                                elif len(str(operand_one)) == 3 or len(str(operand_two)) == 3:
                                    top_layer = f'\n {reformatted_operand_one}'
                                    middle_layer = f'{reformatted_operand_two} {operator}\n-----'
                                    bottom_layer = result
                                    if answers == True:
                                        reformatted_expression = f'{top_layer}\n{middle_layer}\n{bottom_layer}'
                                    else:
                                        reformatted_expression = f'{top_layer}\n{middle_layer}'
                                elif len(str(operand_one)) == 2 or len(str(operand_two)) == 2:
                                    top_layer = f'\n{reformatted_operand_one}'
                                    middle_layer = f'{reformatted_operand_two}{operator}\n----'
                                    bottom_layer = result
                                    if answers == True:
                                        reformatted_expression = f'{top_layer}\n{middle_layer}\n{bottom_layer}'
                                    else:
                                        reformatted_expression = f'{top_layer}\n{middle_layer}'
                                return reformatted_expression
                            
                            #The result of the vertical formatter function will be appended to a string that will contain all reformatted expressions 
                            response += vertical_formatter(operand_one, operand_two, operator)+'    '
                            if amount_problems == 0:
                                response += vertical_formatter(operand_one, operand_two, operator)
                        else:
                            response = f"Error: Operator must be '+' or '-'."
                else:
                    response = 'Error: Numbers must only contain digits.'

            amount_problems =- 1


    return response

result = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40"], True)
print(result)