from model import BookstoreModel

if __name__ == "__main__":
    model = BookstoreModel()
    steps = 10
    for i in range(steps):
        print(f"\n=== Step {i+1} ===")
        model.step()

    print("\n=== Final Book Inventory ===")
    for book in model.books:
        print(f"{book.title}: {book.quantity} copies remaining")
