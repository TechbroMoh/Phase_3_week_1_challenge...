def count_vowels(text):
    count= 0
    vowels = ["a","e","i","o","u","A","E","I","O","U"]

    for character in text:
      if character in vowels:
         count += 1
        
    print(count)

count_vowels("techbromoh")            



