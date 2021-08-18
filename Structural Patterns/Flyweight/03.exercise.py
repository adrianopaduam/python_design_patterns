class FormattedWord:
    def __init__(self, word, capitalize=False) -> None:
        self.word = word
        self.capitalize = capitalize


class Sentence(list):
    def __init__(self, plain_text):
        for word in plain_text.split(' '):
            self.append(FormattedWord(word))

    def __str__(self) -> str:
        return ' '.join([
            formatted.word.upper() if formatted.capitalize
            else formatted.word
            for formatted in self
        ])


if __name__ == '__main__':
    sentence = Sentence('hello world')

    sentence[1].capitalize = True

    print(sentence)
