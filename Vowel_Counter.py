print("="*5,"Counting Vowel","="*5)
count = 0
sentence = input("Enter a Sentence: ")
vowel = ("AEIOUaeiou")
for i  in sentence:
        if i in vowel:
            count +=1
print(count)