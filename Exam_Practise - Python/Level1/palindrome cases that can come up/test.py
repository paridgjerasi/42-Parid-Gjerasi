def is_palindrome():
    word = "ana"
    reversed_word = "".join(reversed(word))
    
    if word == reversed_word:
        print("true")
    else:
        print("false")


is_palindrome()