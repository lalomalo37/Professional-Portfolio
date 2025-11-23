def verify_card_number(card_number):
    sum_of_odd_digits = 0
    # Reversing card numbers since Luhn Algorithim reads card numbers from right to left
    card_number_reversed = card_number[::-1]
    # Seperating odd digits since those will remain the same and only the even digits will be doubled
    odd_digits = card_number_reversed[::2]

    # Adding all odd_digits in preparation for final evaluation
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    # Seperating even digits
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        # 'digit' iterator in this loop is a string, so integer operations cannot be applied until converted to int()
        number = int(digit) * 2
        # If the doubled even digit surpasses 9, the digits of the product must be summed.
        # E.g even digit is 8. 8 * 2 = 16. 16 > 9. So instead of 16 it will be the sum of 1 + 6 = 7. 
        if number >= 10:
            number = (number // 10) + (number % 10)
        # Adds the processed even number
        sum_of_even_digits += number
    # Final evaluation where this function will return true if the total is a multiple of 10 or false if it is not.
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1112-4555-1141'
    # Transform hyphens '-' found in card numbers to blank in order to use only numbers in Luhn Algorithm 
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()