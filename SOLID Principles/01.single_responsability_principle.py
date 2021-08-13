class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]
        self.count -= 1

    def __str__(self) -> str:
        return '\n'.join(self.entries)

    ######################################################################
    # Additional responsability - persistency - wrong
    # def safe(self, filename):
    #     with open(filename, 'w') as file:
    #         file.write(str(self))

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass
    ######################################################################


# Proper separation - Persistence responsability with single class
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as file:
            file.write(str(journal))


if __name__ == '__main__':
    j = Journal()
    j.add_entry('First record')
    j.add_entry('Second record')

    print(
        'Printing directly from Journal object',
        f'Journal entries:\n{j}',
        sep='\n',
        end='\n\n'
    )

    file = 'assets/journal.txt'
    PersistenceManager.save_to_file(j, file)

    with open(file) as file_handler:
        print(
            'Printing form saved file',
            file_handler.read(),
            sep='\n',
            end='\n\n'
        )
