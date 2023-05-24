def check_rhythm(poem):
    phrases = poem.split()  # Разделение стихотворения на фразы
    vowel_counts = []  # Список для хранения количества гласных в каждой фразе
    
    for phrase in phrases:
        words = phrase.split('-')  # Разделение фразы на слова
        total_vowels = 0  # Счетчик гласных
        
        for word in words:
            vowels = 0  # Счетчик гласных в текущем слове
            
            for letter in word:
                if letter.lower() in 'аеёиоуыэюя':
                    vowels += 1
            
            total_vowels += vowels
        
        vowel_counts.append(total_vowels)  # Добавление количества гласных в текущей фразе в список
    
    if len(set(vowel_counts)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"
        

poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)
