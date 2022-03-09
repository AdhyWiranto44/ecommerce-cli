from product import Product
from cart import Cart
from cashier import Cashier


class Adistore:

    def start(self):
        self.main_menu()

    def main_menu(self):
        selected_menu = 999
        products = Product()
        my_cart = Cart()
        cashier = Cashier()

        while (selected_menu != 0):
            print("Welcome to Adistore!")
            print('''
                [1] List of Products
                [2] Add to Cart
                [3] Check My Cart
                [4] Checkout
                [5] Add New Product
                [6] Remove Product
                [0] Exit
                ''')

            try:
                myInput = input("Select menu: ")
                selected_menu = int(myInput)

                if (selected_menu == 1):
                    products.print_products()
                elif (selected_menu == 2):
                    input_code = input("Input product code: ")
                    input_stock = int(input("Input product stock: "))
                    decrease_status = products.decrease_stock(input_code, input_stock)
                    if decrease_status != -1:
                        my_cart.add_to_cart(products.get_products(), input_code, input_stock)
                elif (selected_menu == 3):
                    my_cart.check_my_cart()
                elif (selected_menu == 4):
                    cashier.checkout(my_cart)
                elif (selected_menu == 5):
                    products.add_new_product()
                elif (selected_menu == 6):
                    products.remove_product()
                else:
                    print("Menu not found!")
            except:
                print("Invalid input!")

        print("See you later!")


adistore = Adistore()
adistore.start()
