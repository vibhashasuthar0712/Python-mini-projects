"""mini project-word_counter"""

text=input("enter a word:")
words=text.split()
print("word count:",len(words))








"""palindrome checker"""
text=input("enter a word:")
if text==text[::-1]:
    print("ooh yeah!!its a palindrome!!")
else:
    print("ooho!!,its not a palindrome.")




"""word -level palindrome"""
text = input("Enter a sentence: ")

word=text.split()
if word==word[::-1]:
    print("Ooh yeah!! It's a palindrome!!")
else:
    print("Ooho!! It's not a palindrome.")

             