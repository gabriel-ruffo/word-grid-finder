import json


class DictionaryChecker:
    def __init__(self):
        f = open("src/main/files/words_dictionary.json", "r")
        print(f)
        j = json.loads(f.read())
        self.dict_list = list(j.keys())


    def check_word_in_dictionary(self, word):
        return word in self.dict_list


    def check_if_word_starts_with_letters(self, letters):
        return any(word.startswith(letters) for word in self.dict_list)