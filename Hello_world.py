x = "dima"
words = []
while x != "end":
    x = input("Enter a word")
    if x != "end":
        words.append(x)
for word in words:
    print(word + " " + str(len(word)))
