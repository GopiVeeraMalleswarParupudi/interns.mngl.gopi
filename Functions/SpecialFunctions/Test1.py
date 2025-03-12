'''
write a program which will accepts line of text and decide whether the word is palindrome or not 
by using filter function
'''
words=[word for word in input().split()]
palindromeWords =list(map(lambda word: word.upper(),filter(lambda word: word[::-1]==word, words)))
print(words,'\n',palindromeWords)
print('-'*60)
palindrome=list(map(lambda word : word[::-1]==word, words))
print(palindrome)
print('-'*60)