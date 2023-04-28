import unittest

class TestCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
    

    # Test adding a new item
    def test_add(self):
        
        self.cart.add('apple', 2, 0.5)
        self.assertEqual(self.cart.grocery_dict, {'apple': {'quantity': 2, 'price': 0.5}})



    # Test removing an item
    def test_remove(self):
        
        self.cart.grocery_dict = {'apple': {'quantity': 5, 'price': 0.5}}
        self.cart.remove('apple', 2)
        self.assertEqual(self.cart.grocery_dict, {'apple': {'quantity': 3, 'price': 0.5}})


    def test_show(self):
        # Test showing an empty cart
        self.cart.grocery_dict = {}
        self.cart.show()
        self.assertEqual(self.cart.grocery_dict, {})
        


