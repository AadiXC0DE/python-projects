import datetime

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

class Bill:
    def __init__(self, customer):
        self.customer = customer
        self.timestamp = datetime.datetime.now()
        self.bill_items = []

    def add_bill_item(self, item):
        self.bill_items.append(item)

    def generate_bill(self):
        print("**********************")
        print("       Bill")
        print("**********************")
        print("Customer Name:", self.customer.name)
        print("Date:", self.timestamp.strftime("%Y-%m-%d %H:%M:%S"))
        print("----------------------")
        print("Items Purchased:")
        for item in self.bill_items:
            print(item.name, "\t\tQty:", item.quantity, "\t\tPrice: $", item.price)
        print("----------------------")
        total = self.customer.calculate_total()
        print("Total Amount: $", total)
        print("**********************")

def create_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter item quantity: "))
    return Item(name, price, quantity)

def create_customer():
    name = input("Enter customer name: ")
    return Customer(name)

def main():
    print("Welcome to the Billing System!")
    customer = create_customer()
    bill = Bill(customer)

    while True:
        print("\n1. Add item to cart")
        print("2. Remove item from cart")
        print("3. Generate bill")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item = create_item()
            customer.add_item(item)
            bill.add_bill_item(item)
            print("Item added to cart.")
        elif choice == "2":
            if len(customer.items) > 0:
                print("Items in cart:")
                for i, item in enumerate(customer.items):
                    print(f"{i+1}. {item.name}")
                item_index = int(input("Enter the item number to remove: ")) - 1
                if 0 <= item_index < len(customer.items):
                    item = customer.items[item_index]
                    customer.remove_item(item)
                    bill.bill_items.remove(item)
                    print("Item removed from cart.")
                else:
                    print("Invalid item number.")
            else:
                print("No items in the cart.")
        elif choice == "3":
            bill.generate_bill()
            break
        elif choice == "4":
            print("Thank you for using the Billing System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
