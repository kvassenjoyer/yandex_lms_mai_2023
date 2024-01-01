class RedButton:
    # Не нажимай красную кнопку!
    
    def __init__(self):
        self.click_counter = 0

    def click(self):
        print("Тревога!")
        self.click_counter += 1

    def count(self):
        return self.click_counter
