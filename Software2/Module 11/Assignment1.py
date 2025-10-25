class Publication:
    def __init__(self, name):
        self.name = name
    def print_information(self):
        print(f"Name of the book is: {self.name}")
class Book(Publication):
    def __init__(self, name, author, page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)
    def print_information(self):
        super().print_information()
        print(f"The author is {self.author} and paper count is {self.page_count}")
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        super().print_information()
        print(f"Chief editor: {self.chief_editor}")