# Pharmacy Order Management System – CSE182 Lab 4

This project is a simulated **pharmacy database system** developed as part of the CSE182 Databases course at UC Santa Cruz. The system integrates **PostgreSQL** and **Python** to manage customer transactions, update order statuses, and delete orders under specific constraints. It demonstrates skills in database design, SQL/PLpgSQL scripting, and backend integration.

---

## 📂 Project Structure


---

## ⚙️ Features Implemented

- 🔄 **Order Status Updater**  
  Appends `"AS OF <year>"` to all non-cancelled orders within a valid year range (2000–2030).

- 🧹 **Order Deletion Function**  
  Deletes all future orders for suppliers with a high number of past cancelled orders, up to a given maximum. Implements fair deletion prioritization by cancel count and supplier name.

- 🔍 **Customer Analytics**  
  Counts the number of distinct customers who made purchases at a specified pharmacy, with error handling for invalid IDs.

- 🔐 **Validation & Error Handling**  
  Includes safeguards for invalid input (non-existent pharmacy IDs, years out of bounds, negative deletion limits).

---

## 🛠️ Technologies Used

- **PostgreSQL 15+**
- **PL/pgSQL**
- **Python 3.2**
- **psycopg2**
- **Docker**

---

## 🧪 How to Run

1. **Start the Docker container**  
   (Assumes your container is named `container-psql`)
   ```bash
   docker exec -it container-psql psql -U cse182


## Learning Outcomes

Designed and implemented normalized relational database schemas

Practiced writing PL/pgSQL stored functions with conditionals, loops, and error handling

Used Python's psycopg2 to interact with a PostgreSQL backend

Integrated and tested full-stack database operations

Gained hands-on experience working with real-world transaction-like logic
