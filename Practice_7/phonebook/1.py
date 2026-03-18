import psycopg2
import csv
import os

# Подключение к базе
conn = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="2007",
    port=5432
)
cur = conn.cursor()
print("Connected to PostgreSQL!")

# Путь к папке скрипта и CSV
folder = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(folder, "phonebook.csv")

# Функции для каждого действия
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Contact added!")

def load_csv():
    if not os.path.exists(csv_file):
        print("CSV file not found!")
        return
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row["first_name"], row["phone"]))
    conn.commit()
    print("CSV data loaded!")

def show_all():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def search_name():
    name = input("Search name: ")
    cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def search_phone_part():
    part = input("Phone contains: ")
    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", ("%" + part + "%",))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def update_contact():
    name = input("Name to update: ")
    new_phone = input("New phone: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s", (new_phone, name))
    conn.commit()
    print("Updated!")

def delete_contact():
    name = input("Name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    conn.commit()
    print("Deleted!")

# Главное меню
def menu():
    while True:
        print("\n===== PHONEBOOK MENU =====")
        print("1. Add contact (console)")
        print("2. Load from CSV")
        print("3. Show all contacts")
        print("4. Search by name")
        print("5. Search by phone part")
        print("6. Update contact")
        print("7. Delete contact")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            load_csv()
        elif choice == "3":
            show_all()
        elif choice == "4":
            search_name()
        elif choice == "5":
            search_phone_part()
        elif choice == "6":
            update_contact()
        elif choice == "7":
            delete_contact()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

menu()

cur.close()
conn.close()
print("Connection closed.")