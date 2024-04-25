from pipe_orders import *

def test_pipe_construct():
  # setup
  pipe_type = "PEX"
  pipe_length = 50
  expected = pipe_type + " " + str(pipe_length) + "ft"

  # invoke
  pipe = Pipe(pipe_type,pipe_length)

  # analyze
  assert expected == repr(pipe)

def test_pipe_sort():
  # setup
  pipe1 = Pipe("PEX",20)
  pipe2 = Pipe("Black",10)
  pipe3 = Pipe("PVC",8)
  pipe4 = Pipe("Copper",12)
  expected = [pipe3,pipe2,pipe4,pipe1]

  # invoke
  actual = sorted([pipe1,pipe2,pipe3,pipe4])

  assert expected == actual

def test_order_construct():
  # setup
  expected_order_num = 19
  expected = "Order #" + str(expected_order_num) + " []"

  # invoke
  order = Order(expected_order_num)

  # analyze
  assert expected == repr(order)
  assert expected_order_num == order.get_order_num()

def test_order_add_pipe():
  # setup
  order_num = 19
  pipe1 = Pipe("PEX",20)
  pipe2 = Pipe("PVC",4)
  pipe3 = Pipe("PVC",6)
  expected = "Order #" + str(order_num) + " [" + repr(pipe1) \
              + ", " + repr(pipe2) + ", " + repr(pipe3) + "]"
  order = Order(order_num)   

  # invoke
  order.add_pipe(pipe1)
  order.add_pipe(pipe2)
  order.add_pipe(pipe3)

  # analyze
  assert expected == repr(order)

def test_order_complete():
  # setup
  order_num = 19
  pipe1 = Pipe("Black",7)
  pipe2 = Pipe("Black",4)
  pipe3 = Pipe("PEX",50)
  expected = "Order #" + str(order_num) + " [" + repr(pipe2) \
              + ", " + repr(pipe1) + ", " + repr(pipe3) + "]"
  order = Order(order_num)
  order.add_pipe(pipe1)
  order.add_pipe(pipe2)
  order.add_pipe(pipe3)

  # invoke
  order.complete()

  # analyze
  assert expected == repr(order)

def test_customer_construct():
  # setup
  customer_num = "W6021"
  expected_order_num = 23
  expected = "Cust #W6021 Order #23"

  # invoke
  customer = Customer(customer_num,expected_order_num)

  # analyze
  assert expected == repr(customer)
  assert expected_order_num == customer.get_order_num()

def test_customer_uniqueness():
  # setup
  customer1 = Customer("E6618",25)
  customer2 = Customer("E6618",27)
  customer3 = Customer("E6618",25)
  customer4 = Customer("T6515",28)
  expected_len = 2

  # invoke
  customers = {customer1,customer2,customer3,customer4}

  # analyze
  assert expected_len == len(customers)
  assert customer1 in customers
  assert customer2 in customers
  assert customer3 in customers
  assert customer4 in customers
""""""