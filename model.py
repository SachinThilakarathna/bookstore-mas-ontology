from mesa import Agent, Model
from mesa.time import RandomActivation
import random
from ontology import onto, Book, Customer, Employee

class CustomerAgent(Agent):
    def __init__(self, unique_id, model, customer_onto):
        super().__init__(unique_id, model)
        self.customer_onto = customer_onto
        self.purchased_books = []

    def step(self):
        # Randomly buy 0-2 books per step
        books_available = [b for b in self.model.books if b.hasQuantity > 0]
        if books_available:
            to_buy_count = random.randint(0, min(2, len(books_available)))
            to_buy_books = random.sample(books_available, k=to_buy_count)
            for book in to_buy_books:
                # Reduce stock
                book.hasQuantity -= 1
                # Record purchase
                self.purchased_books.append(book)
                self.model.total_income += book.hasPrice
                # SWRL-like effect: add book to customer's ontology purchases
                self.customer_onto.purchases.append(book)

class EmployeeAgent(Agent):
    def __init__(self, unique_id, model, employee_onto):
        super().__init__(unique_id, model)
        self.employee_onto = employee_onto

    def step(self):
        # Restock books with low quantity (<3)
        for book in self.model.books:
            if book.hasQuantity < 3:
                restock_amount = random.randint(2, 5)
                book.hasQuantity += restock_amount
                # SWRL-like effect: can log restock in employee ontology
                self.employee_onto.worksAt.append(book)

class BookstoreModel(Model):
    def __init__(self):
        self.schedule = RandomActivation(self)
        self.books = list(Book.instances())
        self.total_income = 0

        # Create ontology customers and agents
        self.customers = []
        for i, c in enumerate(list(Customer.instances()), start=1):
            agent = CustomerAgent(i, self, c)
            self.customers.append(agent)
            self.schedule.add(agent)

        # Create ontology employees and agents
        self.employees = []
        for i, e in enumerate(list(Employee.instances()), start=101):
            agent = EmployeeAgent(i, self, e)
            self.employees.append(agent)
            self.schedule.add(agent)

    def step(self):
        self.schedule.step()

