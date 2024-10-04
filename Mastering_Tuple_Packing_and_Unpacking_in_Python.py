# Task 1: Customer Order Processing

def display_order_details(orders):
    for order in orders:
        customer_name, product, quantity = order
        print(f"{customer_name} ordered {quantity} {product}.")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),

]

display_order_details(orders)
