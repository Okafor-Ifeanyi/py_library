class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.value = 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= len(self.words):
            raise StopIteration
        current = self.value
        self.value += 1
        return self.words[current]

sent = Sentence('This is a test')
# print(list(sent))

# for word in sent:
    # print(word)

# Genarator
def list_words(sent):
    for word in sent.split():
        yield word
        
words = list_words('This is a test')

# print(list(words))
# print(words)

for word in words:
    print(word)