from mesa import Agent
import random

class CustomerAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.purchased_books = []

    def step(self):
        # Randomly buy 1-3 books if available
        books = [b for b in self.model.books if b.quantity > 0]
        if books:
            num_to_buy = random.randint(1, min(3, len(books)))
            selected_books = random.sample(books, num_to_buy)
            for b in selected_books:
                self.purchased_books.append(b.title)
                b.quantity -= 1
                self.model.total_income += b.price

class EmployeeAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

    def step(self):
        # Restock low stock books (<3)
        for b in self.model.books:
            if b.quantity < 3:
                b.quantity += random.randint(1, 5)
