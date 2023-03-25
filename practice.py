word = input("Enter Word")
print("original: ", word)
size = len(word)
for i in range(0, size-1, 2):
    print("index[", i, "]", word[i])
