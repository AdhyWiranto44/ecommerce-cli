from cart import Cart


class Product:

    def __init__(self):
        self.products = [
            {
                "code": "PROD001",
                "name": "Wireless Headphone",
                "stock": 12,
                "price": 75500
            },
            {
                "code": "PROD002",
                "name": "Wireless Speaker",
                "stock": 3,
                "price": 135000
            },
        ]

    def get_products(self):
        return self.products

    def print_products(self):
        print("=== List of Products ===")

        if len(self.products) == 0:
            print("Cart empty")
            return -1

        for product in self.get_products():
            print(f"Code: {product['code']}\nName: {product['name']}\nStock: {product['stock']}\nPrice: {product['price']}\n")

    def add_new_product(self):
        input_code = input("Input code: ")
        input_name = input("Input name: ")
        input_stock = input("Input stock: ")
        input_price = input("Input price: ")
        filtered_products = [product for product in self.products if str.lower(product['code']) == str.lower(input_code)]

        if (input_code == "" or input_name == "" or input_stock == "" or input_price == ""):
            print("Incorrect input! Please try again.")
            return -1

        if len(filtered_products) < 1:
            new_product = {"code": input_code, "name": input_name, "stock": int(input_stock), "price": int(input_price)}
            self.products.append(new_product)
            print("New product added!")
        else:
            filtered_products[0]['stock'] += int(input_stock)

    def remove_product(self):
        input_code = input("Input code to remove product: ")

        print("Process to remove ...")
        filtered_products = [product for product in self.products if product['code'] != input_code]
        self.products = filtered_products
        print("Product successfully removed!")

    def decrease_stock(self, code, stock):
        try:
            filtered_products = [product for product in self.products if product['code'] == code]

            if len(filtered_products) < 1:
                print("Product not found")
                return -1
            elif filtered_products[0]['stock'] == 0:
                print("Product stock empty 2")
                return -1
            else:
                if filtered_products[0]['stock'] - stock >= 0:
                    filtered_products[0]['stock'] -= stock
                else:
                    print("Stock can't be negative!")
                    return -1
        except:
            print("Decrease stock failed!")