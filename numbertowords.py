def number_to_words(number):
    
    words = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
        'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
        'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    
    
    tens = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety'
    ]
    
    if number < 20:
        
        return words[number]
    
    elif number < 100:
        
        tens_place = number // 10
        ones_place = number % 10
        
        if ones_place == 0:
            return tens[tens_place]
        else:
            return tens[tens_place] + '-' + words[ones_place]
    
    elif number < 1000:
        
        hundreds_place = number // 100
        remainder = number % 100
        
        if remainder == 0:
            return words[hundreds_place] + ' hundred'
        else:
            return words[hundreds_place] + ' hundred and ' + number_to_words(remainder)
    
    elif number < 1000000:
        
        thousands_place = number // 1000
        remainder = number % 1000
        
        if remainder == 0:
            return number_to_words(thousands_place) + ' thousand'
        else:
            return number_to_words(thousands_place) + ' thousand ' + number_to_words(remainder)
    
    else:
        return 'Number out of range'
        
# Test the function
number = int(input("Enter a number: "))
words = number_to_words(number)
print(f"{number} in words: {words}")
