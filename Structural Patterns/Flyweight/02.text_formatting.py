class FormattedText:
    def __init__(self, plain_text) -> None:
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)

    def capitalize(self, start, end):
        for idx in range(start, end):
            self.caps[idx] = True

    def __str__(self) -> str:
        return ''.join([
            letter.upper() if self.caps[idx]
            else letter
            for idx, letter in enumerate(self.plain_text)
        ])


class FlyweightFormattedText:
    def __init__(self, plain_text) -> None:
        self.plain_text = plain_text
        self.formatting = list()

    class TextRange:
        def __init__(self, start, end, capitalize=False) -> None:
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end

    def get_range(self, start, end):
        range = self.TextRange(start, end)
        self.formatting.append(range)
        return range

    def __str__(self) -> str:
        return ''.join([
            letter.upper() if any([
                range.covers(idx) and range.capitalize
                for range in self.formatting
            ])
            else letter
            for idx, letter in enumerate(self.plain_text)
        ])


if __name__ == '__main__':
    text = 'This is a brave new world'

    formatted_text = FormattedText(text)
    formatted_text.capitalize(10, 15)
    print(formatted_text)

    flywght_formatted_text = FlyweightFormattedText(text)
    flywght_formatted_text.get_range(16, 19).capitalize = True
    print(flywght_formatted_text)
