class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for i in args:
            self.file_names.append(i)
    def get_all_words(self):
        all_words = {}
        de = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                words = []
                for j in file:
                    j = j.lower()
                    for k in de:
                        j = j.replace(k, ' ')
                    words += j.split()
                all_words.update({i : words})
        return all_words
    def find(self, word):
        res = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                pos = 1
                for j in words:
                    if j == word.lower():
                        break
                    pos += 1
                res.update({name : pos})
        return res
    def count(self, word):
        res = {}
        for name, words in self.get_all_words().items():
            summ = 0
            for j in words:
                if j == word.lower():
                    summ += 1
            res.update({name: summ})
        return res

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего