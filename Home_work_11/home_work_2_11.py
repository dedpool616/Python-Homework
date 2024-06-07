def letter_quantity(word):
    b = 0
    c = 0
    for i in word:
        c+=1
        if i == word[0]:
            b += 1
            j = word[c+1:]
    print(j,b)

            



g = letter_quantity('abrakadabra')
print(g)


