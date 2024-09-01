def reverse_string(text):
    
    if isinstance(text, str):
        return text[::-1]
    else:
        return "Input is not a string"


print(reverse_string("google"))  
