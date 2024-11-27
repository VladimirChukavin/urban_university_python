# Домашнее задание по теме "Оператор "with"

class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            word_list = []
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    for char in punctuation:
                        line = line.replace(char, '')
                    word_list += line.lower().split()
                all_words[file_name] = word_list

        return all_words

    def find(self, word):
        position_word = {}
        for name, words in self.get_all_words().items():
            position_word[name] = words.index(word.lower()) + 1
        return position_word

    def count(self, word):
        number_words = {}
        for name, words in self.get_all_words().items():
            number_words[name] = words.count(word.lower())
        return number_words


finder1 = WordsFinder('Mother Goose - Monday’s Child.txt', )
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder2 = WordsFinder('Rudyard Kipling - If.txt', )
print(finder2.get_all_words())
print(finder2.find('if'))
print(finder2.count('if'))

finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder3.get_all_words())
print(finder3.find('captain'))
print(finder3.count('captain'))

finder4 = WordsFinder('test_file.txt')
print(finder4.get_all_words())
print(finder4.find('TEXT'))
print(finder4.count('teXT'))

finder5 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder5.get_all_words())
print(finder5.find('the'))
print(finder5.count('the'))