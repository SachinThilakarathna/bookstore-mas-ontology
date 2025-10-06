from owlready2 import *
import random

# Create ontology
onto = get_ontology("http://test.org/bookstore.owl")

with onto:
    # Classes
    class Book(Thing):
        pass

    class Customer(Thing):
        pass

    class Employee(Thing):
        pass

    class Order(Thing):
        pass

    # Data Properties
    class hasTitle(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class hasGenre(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [str]

    class hasPrice(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [float]

    class hasQuantity(DataProperty, FunctionalProperty):
        domain = [Book]
        range = [int]

    # Object Properties
    class purchases(ObjectProperty):
        domain = [Customer]
        range = [Book]

    class worksAt(ObjectProperty):
        domain = [Employee]
        range = [Thing]

# Create some books
books_list = []

b1 = Book("Book1")
b1.hasTitle = "The Alchemist"
b1.hasGenre = "Fiction"
b1.hasPrice = 200
b1.hasQuantity = 10
books_list.append(b1)

b2 = Book("Book2")
b2.hasTitle = "Python 101"
b2.hasGenre = "Programming"
b2.hasPrice = 300
b2.hasQuantity = 5
books_list.append(b2)

b3 = Book("Book3")
b3.hasTitle = "AI Basics"
b3.hasGenre = "Technology"
b3.hasPrice = 250
b3.hasQuantity = 7
books_list.append(b3)

b4 = Book("Book4")
b4.hasTitle = "Data Science"
b4.hasGenre = "Technology"
b4.hasPrice = 400
b4.hasQuantity = 4
books_list.append(b4)

b5 = Book("Book5")
b5.hasTitle = "Meditation Guide"
b5.hasGenre = "Self-help"
b5.hasPrice = 450
b5.hasQuantity = 8
books_list.append(b5)

# SWRL-like functions (simulation-ready)
def purchase_book(customer):
    """
    Customer randomly buys 1 or 2 books if available.
    Updates book quantity and records purchase.
    """
    available_books = [b for b in books_list if b.hasQuantity > 0]
    if not available_books:
        return
    to_buy = random.sample(available_books, k=min(random.randint(1, 2), len(available_books)))
    for book in to_buy:
        # Reduce stock
        book.hasQuantity -= 1
        # Record customer purchase
        customer.purchases.append(book)

def restock_book(employee):
    """
    Employee restocks books with low quantity (<3)
    """
    for book in books_list:
        if book.hasQuantity < 3:
            book.hasQuantity += 5  # restock 5 copies

# Example: create employees and customers for simulation
customers_list = []
employees_list = []

for i in range(1, 6):
    c = Customer(f"Customer{i}")
    c.purchases = []
    customers_list.append(c)

for i in range(1, 4):
    e = Employee(f"Employee{i}")
    employees_list.append(e)

# Optional: Save ontology
onto.save(file="bookstore.owl")
