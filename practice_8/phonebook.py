from connect import get_connection

def call_upsert(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()


def search(pattern):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def paginate(limit, offset):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s)",
        (limit, offset)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()


def bulk_insert(names, phones):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "CALL bulk_insert_contacts(%s, %s)",
        (names, phones)
    )
    conn.commit()
    cur.close()
    conn.close()


def delete(value):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    #  upsert
    call_upsert("Ali", "87001234567")

    #  search
    search("Ali")

    # pagination
    paginate(5, 0)

    # bulk insert
    bulk_insert(
        ["A", "B", "C"],
        ["87001234567", "invalid", "87771234567"]
    )

    #  delete
    delete("Ali")