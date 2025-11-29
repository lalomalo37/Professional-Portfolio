problems = []

def arithmetic_arranger(problems, answers = False):
    expression = ''
    result = 0
    response = ''
    if len(problems) > 5:
        response = 'Error: Too many problems.'
    elif len(problems) <= 5:
        amount_problems = len(problems)
        while amount_problems > 0 :
            for problem in problems:
                expression += problem
            amount_problems =- 1
        for char in expression:
            first_number += char
            if char == ' ':
                pass

        
        response = expression

    return response


print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40"]))