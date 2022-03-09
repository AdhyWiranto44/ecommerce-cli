class Cart:

    def __init__(self):
        self.cart = [
            {
                "code": "PROD001",
                "name": "Wireless Headphone",
                "stock": 3,
                "price": 75500
            },
        ]

    def get_cart(self):
        return self.cart

    def check_my_cart(self):
        print("=== My Cart ===")

        if len(self.cart) == 0:
            print("Cart empty")
            return -1

        for c in self.cart:
            print(f"Code: {c['code']}\nName: {c['name']}\nStock: {c['stock']}\nPrice: {c['price']}\n")

    def add_to_cart(self, products, input_code, input_stock):
        try:
            filtered_products = [product for product in products if product['code'] == input_code]
            filtered_cart = [c for c in self.cart if c['code'] == input_code]

            if len(filtered_cart) < 1:
                new_item = {
                    "code": filtered_products[0]['code'],
                    "name": filtered_products[0]['name'],
                    "stock": input_stock,
                    "price": filtered_products[0]['price']
                }

                self.cart.append(new_item)
                print("Success add to cart!")
            else:
                filtered_cart[0]['stock'] += input_stock
                print("Success increase cart!")
        except:
            print("Add to cart failed!")

    def clear_cart(self):
        self.cart = []