message = input(">")

# usually when input receives a string of characters, it will read it as a string
# but with split method we can separate the string into different words
# split will separate my input message, and will create a list of words
words = message.split(' ')

emojis = {
    ":)": "😊",
    ":(": "😒",
    ":D": "😁",
    "<3": "❤"
}

output = ""
for word in words:
    # output va citi fiecare input de la tastatura (care a fost transformat intr-o lista denumita words)
    # emojis.get (primul word) va citi fiecare cuvant si ii va atribui valoarea
    # daca key nu exista in dict atunci (al 2-lea word) word va primi key-ul + valoarea  lui insusi
    print(emojis.get(word, word), end=" ")
print(output)
