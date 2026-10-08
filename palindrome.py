def palindrome(text):
    p_text = str(text).lower()
    
    #slicing method to reverse the string and check if it is equal to the original string
    return p_text == p_text[::-1]

text = input("Enter a string to check if it's a palindrome: ")
print(palindrome(text)) 
