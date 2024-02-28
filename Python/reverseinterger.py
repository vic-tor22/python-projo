def capitalize_words(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]
    
    # Join the capitalized words back into a string
    result = ' '.join(capitalized_words)
    
    return result

# Test cases
test_strings = ["hi", "i love programming"]
for string in test_strings:
    print(f'Input: "{string}" => Output: "{capitalize_words(string)}"')
