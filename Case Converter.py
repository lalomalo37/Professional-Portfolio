def convert_to_snake_case(pascal_or_camel_cased_string):
    # Created a list comprehension inside of snake_cased_char_list. 
    # A list comprehension is a construct that allows you to generate a new list by applying an expression to each item in an existing iterable. 
    # And optionally filtering items with a condition. 
    # In this case the expression is to add an underscore and convert the iterable ('char') into a lower case. 
     
    snake_cased_char_list = [
        # Note: In a list comprehension, the condition is stated before the for loop, after the expression. 
        # In this case it evaluates if a character inside the string is upper case If it is, it applies the underscore + lower case expression and appends it to the list. 
        # If not it just appends the character as is.
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    # The join function appends a character to a string array
    # The strip function removes from a string any leading or trailing characters among a set of characters passed as its argument
    # We apply this because there's a chance of having an extra underscore at the start of the string.
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()