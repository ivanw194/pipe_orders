import node_stack
import node_queue
import csv


"""
Part 1 - Complete the pipe class
"""
class Pipe:
    def __init__(self, type, length):
        self.__length = int(length)
        self.__type = str(type)

    def __str__(self):
        return "[" + self.__type + str(self.__length) + "]"
    
    def __lt__(self, other):
        return self.__length < other.__length
    
class Order:
    def __init__(self, pipes, order_num, length, type):
        self.__pipes = pipes
        self.__order_num = order_num
        self.__length = length
        self.__type = type

    def type(self):
        return self.__type

    def __len__(self):
        return len(self.__pipes)

    def get_order_num(self):
        order_num = 0
        for letter in self.__pipes:
            x = letter.strip(",")
            for x in letter:
                if x != "":
                    order_num += 1
        return order_num

    def is_full(self):
        return len(self.__pipes) >= self.__order_num

    def is_empty(self):
        return not bool(self.__pipes)

    def add_pipe(self):
        if self.is_full():
            raise ValueError("Amount of orders is full")
        self.__order_num += 1
        return self.__order_num

    def complete(self):
        self.__pipes.sort()

    def __repr__(self):
        return "[" + str(self.__order_num) + "]" + "[" + str(self.complete()) + "]"
#  Complete the create_orders function below to generate the
    # orders of pipes
def create_orders(filename):
    orders = []

    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header line
        
        for row in csv_reader:
            order_num = row[0]
            pipes = [pipe.strip() for pipe in row[1:] if pipe.strip()]  # Strip whitespace and remove empty pipes
            length = len(pipes)  # Length is determined by the number of pipes in the order
            type = [pipe.split()[0] for pipe in pipes]  # Extract the type from each pipe (assuming it's the first word)
            order = Order(pipes, order_num, length, type)
            orders.append(order)

    return orders
#  Complete the Customer class below 
class Customer:
    def __init__(self, number, order_num):
        self.__number = number
        self.__order_num = order_num

    def set_order_num(self):
        if self.__order_num in Order.create_orders():
            self.__order_num += 1

    def __eq__(self, other):
        return self.__number == other.__number

    def __hash__(self):
        return hash(self.__number)
    
    def __str__(self):
        return "[" + self.__number + "]" + "[" + str(self.__order_num) + "]"
    
# Complete the create_customers function below to generate a
#   line of customers.
def create_customers(filename):
    customers_queue = node_queue.Queue()  # Creating an instance of the Queue class

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header line
        for row in csv_reader:
            customer_number = row[0]
            order_num = row[1] # Assuming order_num should be an integer
            customer = Customer(customer_number,order_num)
            customers_queue.enqueue(customer)  # Enqueue the customer into the queue

    return customers_queue
# Complete the pick_up_orders function below to have customers pick up their orders
def pick_up_orders(orders, customers):
    back_in_line_counts = {}
    order_index = 0

    while not customers.empty() and order_index < len(orders):
        customer = customers.get()
        order = orders[order_index]
        
        if customer.type() in order:
            if customer in back_in_line_counts:
                back_in_line_counts[customer] += 1
            else:
                back_in_line_counts[customer] = 1
            order_index += 1
        else:
            customers.put(customer)

    return back_in_line_counts
 #don't forget to return A data structure (hint: dictionary) that associates each customer to their back-in-line count
def main():
    # Parts 1 - 3: Create a stack of orders of pipes
    orders = create_orders("data/pipe_orders.csv")
    print("Orders (must match exactly):")
    print("Actual:   " + str(orders))
    print("Expected: " + EXPECTED_ORDERS)

    print()
    # Parts 4 - 5: Create and line up customers
    customers = create_customers("data/pipe_customers.csv")
    print("Customers (must match exactly):")
    print("Actual:   " + str(customers))
    print("Expected: " + EXPECTED_CUSTOMERS)

    print()
    # Part 6: Customers pick up their orders
    back_in_line_counts = pick_up_orders(orders, customers)
    print("Back In Line Counts (order of customer and counts does not need to match):")
    print("Actual:   " + str(back_in_line_counts))
    print("Expected: " + EXPECTED_BACK_IN_LINE_COUNTS)

# Extra Testing
EXPECTED_ORDERS = "[Order #112 [PEX 3ft, PEX 3ft, BLACK 9ft, ABS 15ft, COPPER 17ft], Order #113 [PEX 20ft], Order #111 [PVC 5ft, COPPER 6ft], Order #115 [BLACK 14ft, PVC 17ft, PEX 20ft, ABS 39ft], Order #114 [BLACK 7ft, COPPER 7ft, PEX 8ft]]"
EXPECTED_CUSTOMERS = "[Cust #X8521 Order #113, Cust #R7468 Order #115, Cust #A2563 Order #114, Cust #L1386 Order #112, Cust #M7427 Order #111]"
EXPECTED_BACK_IN_LINE_COUNTS = "{Cust #X8521 Order #113: 1, Cust #R7468 Order #115: 2, Cust #A2563 Order #114: 2, Cust #L1386 Order #112: 0, Cust #M7427 Order #111: 1}"

if __name__ == "__main__":
    main()