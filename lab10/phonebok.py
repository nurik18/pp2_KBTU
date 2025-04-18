import psycopg2
import csv

def connect():
    return psycopg2.connect(
        host = "localhost" ,
        database = "phonebook",
        user = "nurik",
        password = "icrash_ucrash"
    )

def createTable():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARHCHAR(20)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


def insertFromInput():
    name = input("Your name: ")
    phone = input("Your phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insertFromCSV(file_path):
    conn = connect()
    cur = conn.cursor()

    with open()(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            name, phone = row
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        
    conn.commit()
    cur.close()
    conn.close()

def updateData():
    field = input("Update what? (name/phone)").strip()
    old_value = input(f"What value of {field}: ")
    new_value = input(f"New value of {field}: ")

    conn = connect()
    cur = conn.cursor()

    if field == "name":
        cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (new_value, old_value))
    elif field == "phone":
        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_value, old_value))

    conn.commit()
    cur.close()
    conn.close()

def queryData():
    filter_by = input("Filter (name/phone):")
    value = input(f"Значение для {filter_by}: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM phonebook WHERE {filter_by} ILIKE %s", (f"%{value}%"))
    rows = cur.fetchall()

    for row in rows: 
        print(row)

    cur.close()
    conn.colse()

def deleteData():
    field = input("Delete by ? (name/phone): ")
    value = input(f"Value {field}:")

    conn = connect()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM phonebook WHERE {field} = %s", (value,))
    conn.commit()
    cur.close()
    conn.close()

def menu():
    while True:
        print("\n    PhoneBook    ")
        print("1. Create a table")
        print("2. Insert from input")
        print("3. Insert from CSV")
        print("4. Update Data")
        print("5. Find Data")
        print("6. Delete Data")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "0":
            break
        elif choice == "1":
            createTable()
        elif choice == "2":
            insertFromInput()
        elif choice == "3":
            file_path = input("Enter path to CSV-file")
            insertFromCSV(file_path)
        elif choice == "4":
            updateData()
        elif choice == "5":
            queryData()
        elif choice == "6":
            deleteData()
        else:
            print("Vvedite normalnoe chislo pls")

if __name__ == "__main__":
    menu()