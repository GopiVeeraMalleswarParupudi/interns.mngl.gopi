'''
write a program which will accept a word and deide whether it is vowel word or not.
'''
vowel = lambda a :"Given word '{}' is a vowel word".format(a) if a.lower() in ['a','e','i','o','u'] else "Given word '{}' is not a vowel word".format(a)

print(vowel(input("Enter the word : ")))