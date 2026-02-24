# def is_palindrome():
#     word = "ana"
#     reversed_word = "".join(reversed(word))
    
#     if word == reversed_word:
#         print("true")
#     else:
#         print("false")


# is_palindrome()


def echo_valid(name: str) -> bool:
    return name == name[::-1]

name = "hello"

print(name[1:3:-1])