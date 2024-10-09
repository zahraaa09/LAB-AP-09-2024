def palindrome():
    kata = input("Masukkan kata: ")
    palindrome = (''.join(reversed(kata)))

    if kata == palindrome:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome()