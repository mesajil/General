
def esPalindromo (text):
    return text == text[::-1]


if __name__ == "__main__":
    if (esPalindromo(input ())):
        print ("Es Palindromo")
    else:
        print ("No Es Palindromo")


