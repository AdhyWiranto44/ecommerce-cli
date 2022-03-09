class Cashier:

    def __init__(self):
        pass

    def checkout(self, my_cart):
        try:
            my_cart.check_my_cart()
            total = self.sum_price(my_cart)
            print(f"Total: Rp {total}")
            money = int(input("Input amount of money, Rp "))

            if money > total:
                change = money - total
                print(f"Here's your change: Rp {change}")
                my_cart.clear_cart()
            elif money < total:
                need_more = total - money
                print(f"Money not enough, need Rp {need_more} more.")
                self.checkout(my_cart)
            else:
                print("Correct amount, have a nice day!")
        except:
            print("Cashier machine got error!")

    def sum_price(self, my_cart):
        total = 0
        for c in my_cart.get_cart():
            total += c['price']
        return total