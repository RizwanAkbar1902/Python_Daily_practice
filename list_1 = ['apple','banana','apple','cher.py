sentense = input("Enter a sentense: ")
sentense_1= sentense.split()
frequency_count_of_each_word = {}
for word in sentense_1:
    if word in frequency_count_of_each_word:
        frequency_count_of_each_word[word] += 1
    else:
        frequency_count_of_each_word[word] = 1
print(frequency_count_of_each_word)


