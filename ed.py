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
        new_node = Node(name, day, month)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

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

def menu():
    print("\nMenu:")
    print("1. Adicionar pessoa")
    print("2. Remover pessoa")
    print("3. Listar todas as pessoas")
    print("4. Sair")
    choice = int(input("Selecione uma opção: "))
    return choice

def main():
    dll = DoubleLinkedList()
    while True:
        choice = menu()

        if choice == 1:
            name = input("Digite o nome da pessoa: ")
            day = int(input("Digite o dia do aniversário: "))
            month = int(input("Digite o mês do aniversário: "))
            dll.add_node(name, day, month)
        elif choice == 2:
            name = input("Digite o nome da pessoa que deseja remover: ")
            dll.remove_node(name)
        elif choice == 3:
            print("Listando todas as pessoas:")
            dll.list_all()
        elif choice == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()