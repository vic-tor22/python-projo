def count_vowels(sentence):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Convert the sentence to lowercase to handle both uppercase and lowercase vowels
    sentence = sentence.lower()
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is a vowel
        if char in vowels:
            # Increment the vowel count
            vowel_count += 1
    
    return vowel_count

# Test case
sentence = "Hello World"
print(f'Input: "{sentence}" => Output: {count_vowels(sentence)}')
