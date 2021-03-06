import re
from abc import ABC, abstractmethod


class System:
    def __init__(self, text: str):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor):
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class TextProcessor(ABC):
    @abstractmethod
    def process_text(self, text):
        pass


class WordCounter:
    def count_word(self, text: str):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()


class WordCounterAdapter(TextProcessor):
    def __init__(self, adaptee: WordCounter):
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_word(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words,
                      key=lambda x: self.adaptee.get_count(x),
                      reverse=True)


text = "Vasya likes to dance"

system = System(text=text)
counter = WordCounter()

adapter = WordCounterAdapter(adaptee=counter)

system.get_processed_text(adapter)
