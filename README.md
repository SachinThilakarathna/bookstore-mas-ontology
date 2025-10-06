# Bookstore Management System

An **ontology-based multi-agent bookstore management system** implemented in Python using **Owlready2**, **Mesa**, and **Flask**. This project simulates a bookstore with books, customers, and employees as agents, and visualizes inventory and sales in a responsive web dashboard.

## Features
- **Ontology Modeling:** Book, Customer, Employee, and Order classes with properties.
- **Agents:**
  - `CustomerAgent` buys books randomly.
  - `EmployeeAgent` restocks low inventory books.
- **Simulation:** Tracks purchases, low stock, and total income.
- **Dashboard:** Flask-based web dashboard with:
  - Book inventory table
  - Book stock chart
  - Sales income chart
  - Customer purchase records
- **Responsive Design:** Adapts to different screen sizes.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/<your-username>/bookstore-mas-ontology.git
    cd bookstore-mas-ontology
    ```
2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    pip install -r requirements.txt
    ```
3. Run the Flask application:
    ```bash
    python server.py
    ```

## Folder Structure

BookstoreManagementSystem/
│
├─ ontology.py # Owlready2 ontology
├─ model.py # Mesa agents and model
├─ server.py # Flask application
├─ templates/
│ └─ index.html # Dashboard HTML & CSS 
├─ requirements.txt # Python dependencies
└─ README.md


## Usage
- Open the browser at `http://127.0.0.1:5000` to view the dashboard.
- Click **Run Simulation** to simulate customer purchases and employee restocks.
- View charts and inventory tables updating dynamically.

## Technologies Used
- Python 3.x
- [Owlready2](https://owlready2.readthedocs.io/)
- [Mesa](https://mesa.readthedocs.io/)
- Flask
- Chart.js

## License
MIT License


