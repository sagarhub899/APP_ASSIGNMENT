
# Strategy Pattern Example

# Parent Class (Base Strategy)
class PaymentStrategy:
    def pay(self, amount):
        pass


# Credit Card Payment Strategy
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


# PayPal Payment Strategy
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


# Context Class
class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    # Change payment method at runtime
    def set_strategy(self, strategy):
        self.strategy = strategy

    # Execute payment
    def pay(self, amount):
        self.strategy.pay(amount)


# Main Program
credit = CreditCardPayment()
payment = PaymentContext(credit)

payment.pay(1000)

paypal = PayPalPayment()
payment.set_strategy(paypal)

payment.pay(500)
