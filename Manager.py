import Actions
import DB

def first_menu():
    while True:
        key = input("Choose an action:\n"
                    "1) Get information\n"
                    "2) Add data\n"
                    "3) Delete data\n"
                    "0) Exit\n"
                    "Enter:")
        if key == '1':
            return 10
        elif key == '2':
            return 20
        elif key == '3':
            return 30
        elif key == '0':
            return -1
        else:
            print("\nData entered incorrectly, please try again")
    return key


def second_menu(action):
    while True:
        key = input("\nChoose what to perform the operation on:\n"
                    "1) Students\n"
                    "2) Teachers\n"
                    "3) Groups\n"
                    "4) Subjects\n"
                    "0) Back\n"
                    "Enter:")

        if key == '1':
            return action+1
        elif key == '2':
            return action+2
        elif key == '3':
            return action+3
        elif key == '4':
            return action+4
        elif key == '0':
            return -1
        else:
            print("\nData entered incorrectly, please try again")


def main():
    db = DB.DB_Controller()
    db.create_tables()
    ac = Actions.Action()
    while True:
        key = first_menu()
        if key == -1:
            print("\nGoodbye")
            break
        else:
            key = second_menu(key)
            if key != -1:
                if key // 10 == 1:
                    ac.get_records(key % 10)
                elif key // 10 == 2:
                    ac.add_record(key % 10)
                elif key // 10 == 3:
                    ac.del_record(key % 10)
    db.close_db()

main()



