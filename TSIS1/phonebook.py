import psycopg2
import json

conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="Apalon228a",
    host="localhost"
)
cur = conn.cursor()




def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group_id = input("Group ID (1-Family,2-Work,3-Friend): ")

    cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
    """, (name, email, birthday, group_id))

    conn.commit()

    phone = input("Phone: ")
    phone_type = input("Type (home/work/mobile): ")

    cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, phone_type))
    conn.commit()

    print("Contact added!")



def filter_by_group():
    group = input("Group name: ")

    cur.execute("""
        SELECT c.name, c.email
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group,))

    print(cur.fetchall())



def search_email():
    email = input("Email search: ")

    cur.execute("""
        SELECT name, email
        FROM contacts
        WHERE email ILIKE %s
    """, ('%' + email + '%',))

    print(cur.fetchall())



def sort_contacts():
    option = input("Sort by (name/birthday/date): ")

    if option == "name":
        cur.execute("SELECT name FROM contacts ORDER BY name")
    elif option == "birthday":
        cur.execute("SELECT name, birthday FROM contacts ORDER BY birthday")
    else:
        cur.execute("SELECT name FROM contacts ORDER BY id")

    print(cur.fetchall())


def pagination():
    limit = 5
    offset = 0

    while True:
        cur.execute(f"SELECT name FROM contacts LIMIT {limit} OFFSET {offset}")
        print(cur.fetchall())

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        else:
            break



def export_json():
    cur.execute("SELECT name, email, birthday FROM contacts")
    data = cur.fetchall()

    result = []
    for row in data:
        result.append({
            "name": row[0],
            "email": row[1],
            "birthday": str(row[2])
        })

    with open("contacts.json", "w") as f:
        json.dump(result, f, indent=4)

    print("Exported!")


def import_json():
    with open("contacts.json", "r") as f:
        data = json.load(f)

    for c in data:
        cur.execute("SELECT * FROM contacts WHERE name=%s", (c["name"],))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{c['name']} exists. skip/overwrite: ")

            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (c["name"],))

        cur.execute("""
            INSERT INTO contacts(name, email, birthday)
            VALUES (%s, %s, %s)
        """, (c["name"], c["email"], c["birthday"]))

    conn.commit()
    print(" Imported!")


def menu():
    while True:
        print("""
1. Add contact
2. Filter by group
3. Search email
4. Sort
5. Pagination
6. Export JSON
7. Import JSON
8. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            filter_by_group()
        elif choice == "3":
            search_email()
        elif choice == "4":
            sort_contacts()
        elif choice == "5":
            pagination()
        elif choice == "6":
            export_json()
        elif choice == "7":
            import_json()
        elif choice == "8":
            break


menu()