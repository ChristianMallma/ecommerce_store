class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "quantity": quantity,
                "price": str(product.price),
                "image": product.image.url,
                "category": product.category.name,
                "subtotal": str(quantity * product.price)
            }
        else:
            # To Update quantity
            for key, product_obj in self.cart.items():
                if key == str(product.id):
                    product_obj['quantity'] = str(int(product_obj['quantity']) + quantity)
                    product_obj['subtotal'] = str(float(product_obj['subtotal']) + float(quantity*product_obj['price']))
                    break

        self.save()

    def delete(self, product):
        pass

    def clear(self):
        pass

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True
