# ============================================ №5*
input_word = input("Введите первое слово: ")

file_name = 'text.txt'
with open(file_name, "r", encoding="utf-8") as file:
    words = [word.strip() for word in file.readlines()]

for word in words:
    for index in range(1,len(word)):   
        if word[:-1*index] in input_word:
            if input_word.find(word[:-1*index])>1:
                print(input_word[:input_word.find(word[:-1*index])]+ word)
                break
