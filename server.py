from flask import Flask, render_template
from model import BookstoreModel

app = Flask(__name__)
model = BookstoreModel()

@app.route("/")
def index():
    # Prepare books for display
    books = [
        {
            "title": getattr(b, "hasTitle", "Unknown"),
            "genre": getattr(b, "hasGenre", "Unknown"),
            "price": getattr(b, "hasPrice", 0),
            "quantity": getattr(b, "hasQuantity", 0)
        }
        for b in model.books
    ]

    # Prepare customers for display
    customers = [
        {
            "name": f"Customer_{c.unique_id}",
            "purchased": [getattr(b, "hasTitle", "Unknown") for b in c.purchased_books]
        }
        for c in model.customers
    ]

    # Summary
    total_sold = sum(len(c["purchased"]) for c in customers)
    low_stock_books = [b["title"] for b in books if b["quantity"] < 3]
    total_income = model.total_income

    return render_template(
        "index.html",
        books=books,
        customers=customers,
        total_sold=total_sold,
        low_stock_books=low_stock_books,
        total_income=total_income
    )

@app.route("/step")
def step():
    # Run one simulation step
    model.step()
    return "Step completed!"

if __name__ == "__main__":
    app.run(debug=True)
