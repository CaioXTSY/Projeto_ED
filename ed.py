class Node:
    def __init__(self, name, day, month):
        self.name = name
        self.day = day
        self.month = month
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, name, day, month):
        if not self.validate_date(day, month):
            print("Data inválida. Tente novamente.")
            return

        new_node = Node(name, day, month)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def validate_date(self, day, month):
        if month < 1 or month > 12:
            return False

        if day < 1 or day > 31:
            return False

        if month in [4, 6, 9, 11] and day > 30:
            return False

        if month == 2:
            if day > 29:
                return False
            elif day == 29 and not self.is_leap_year():
                return False

        return True

    def is_leap_year(self):
        year = datetime.datetime.now().year
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def remove_node(self, name):
        current_node = self.head

        if current_node is not None:
            if current_node.name == name:
                self.head = current_node.next
                if self.head is None:
                    self.tail = None
                else:
                    current_node.next.prev = None
                current_node = None
                return

        while current_node is not None:
            if current_node.name == name:
                break

            current_node = current_node.next

        if current_node is None:
            return

        if current_node.next is not None:
            current_node.next.prev = current_node.prev
        else:
            self.tail = current_node.prev

        if current_node.prev is not None:
            current_node.prev.next = current_node.next

    def list_all(self):
        current_node = self.head
        while current_node is not None:
            print("-"*50)
            print(f"Name: {current_node.name}, Aniversario: {current_node.day}/{current_node.month}")
            current_node = current_node.next

    def list_birthday(self):
        dates = []
        current_node = self.head
        while current_node is not None:
            dates.append((current_node.name, current_node.day, current_node.month))
            current_node = current_node.next
        sorted_dates = sorted(dates, key=lambda x: (x[2], x[1]))
        print ("-"*50)	
        print("Datas de aniversário ordenadas:")
        for date in sorted_dates:
            print(f"{date[0]}: {date[1]}/{date[2]}")
            print("-"*50)

def menu():
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Listar todos")
    print("4 - Listar ordenadamente")
    print("5 - Sair")

def main():
    double_linked_list = DoubleLinkedList()
    while True:
        menu()
        option = int(input("Digite uma opção: "))
        if option == 1:
            name = input("Digite o nome: ")
            day = int(input("Digite o dia: "))
            month = int(input("Digite o mês: "))
            double_linked_list.add_node(name, day, month)
        elif option == 2:
            name = input("Digite o nome: ")
            double_linked_list.remove_node(name)
        elif option == 3:
            double_linked_list.list_all()
        elif option == 4:
            double_linked_list.list_birthday()
        elif option == 5:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()