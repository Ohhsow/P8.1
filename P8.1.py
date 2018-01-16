# -*- coding: utf-8 -*-
# Created by Andrei Kisel


class CreatedInstancesCounter(object):
    c = 0
    def __init__(self):
        self.__class__.c += 1

    @classmethod
    def get_created_object_count(cls):
        return cls.c

class Store(object):

    """Class creation of the store"""

    def __init__(self, shop, over_sum_no_discount=0, over_sum_yes_discount=0):
        """Constructor """
        self.shop = shop
        self.over_sum_no_discount = over_sum_no_discount
        self.over_sum_yes_discount = over_sum_yes_discount

    def add_item(self, item):

        """ Add new item into store"""
        self.shop.append(item)
        self.overall_price_yes_discount(item)
        self.overall_price_no_discount(item)


    def remove_item(self, item):

        """Delete item from the store"""
        if item in self.shop:
            self.shop.remove(item)
            self.change_overall(item)
        else:
            print("This element isn't in this store, please check input")

    def overall_price_yes_discount(self, item):
        """Returns overall price with discount"""
        if item.discount > 0:
            self.over_sum_yes_discount += item._price

    def overall_price_no_discount(self, item):
        """Returns overall price without discount"""
        if item.discount == 0:
            self.over_sum_no_discount += item._price

    def change_overall(self, item):
        if self.over_sum_yes_discount > 0 and item.discount > 0:
            self.over_sum_yes_discount -= item._price
        if self.over_sum_no_discount > 0 and item.discount == 0:
            self.over_sum_no_discount -= item._price


class GroceryStore(Store):
    """Class inheritor of Store Class"""

    def __init__(self, shop=[]):
        super(GroceryStore, self).__init__(shop)
        shop = []
    def add_item(self, *item):
        """Add item into Grocery store"""
        for add in item:
            if add.type == 'Grocery':
                super(GroceryStore, self).add_item(add)
            else:
                raise TypeError("Incorrect !")

    def remove_item(self, *item):
        """Delete item from Grocery store"""
        for i in item:
            super(GroceryStore, self).remove_item(i)


class HardwareStore(Store):
    """Class inheritor of HardwareClass"""

    def __init__(self, shop=[]):
        """Create new Hardware Store"""
        super(HardwareStore, self).__init__(shop)

    def add_item(self, *item):
        """Fdd item into Hardware Store"""
        for add in item:
            if add.type == 'Tool':
                super(HardwareStore, self).add_item(add)
            else:
                raise TypeError("Incorrect!")

    def remove_item(self, *item):
        """Delete item from Hardware Store"""
        for i in item:
            super(HardwareStore, self).remove_item(i)


class Goods(object):
    """Class ancestor for all goods"""

    def __init__(self, price, discount=0, freezing=True, type=None):
        """Constructor of goods"""
        self._price = price
        self.discount = discount
        self.freezing = freezing
        self.type = type


    @property
    def protected_price(self):
        return self._price

    @protected_price.setter
    def protected_price(self, value):
        """Enabling/disabling freezing of price"""
        if self.freezing == False:
            self._price = value
        else:
            raise ValueError("Changing of price is denied")

    def set_discount(self, discount):
        """Sets discount of the good"""
        self.discount = discount
        decrement = 1 - self.discount / 100.0
        self._price *= decrement

    def reset_discount(self):
        """Disable discount for good"""
        increment = 1 - self.discount / 100.0
        self._price *= 1 / increment
        self.discount = 0


class Food(Goods):
    """Class  creates new food item"""

    def __init__(self, price):
        super(Food, self).__init__(price, type='Grocery')

    def set_discount(self, discount):
        super(Food, self).set_discount(discount)

    def reset_discount(self):
        super(Food, self).reset_discount()


class Tools(Goods):
    """Class creates new tool item"""

    def __init__(self, price):
        super(Tools, self).__init__(price, type='Tool')

    def set_discount(self, discount):
        super(Tools, self).set_discount(discount)

    def reset_discount(self):
        super(Tools, self).reset_discount()


class Banana(Food):
    """Class creates bananas"""

    def __init__(self, price):
        super(Banana, self).__init__(price)


class Apple(Food):
    """Class creates apples"""

    def __init__(self, price):
        super(Apple, self).__init__(price)


class Ham(Food):
    """Class creates bananas"""

    def __init__(self, price):
        super(Ham, self).__init__(price)


class Nail(Tools):
    """Class creates nail"""

    def __init__(self, price):
        super(Nail, self).__init__(price)


class Axe(Tools):
    """Class  creates axes"""

    def __init__(self, price):
        super(Axe, self).__init__(price)


class Saw(Tools):
    """Class creates saws"""

    def __init__(self, price):
        super(Saw, self).__init__(price)


if __name__ == '__main__':

    """Create Stores"""

    belmarket = GroceryStore()
    oma = HardwareStore()
    milie = HardwareStore()

    """Creation of items"""

    banana = Banana(6)    # create a banana with 6$ price
    ham = Ham(22)
    nail = Nail(2)
    saw = Saw(6)

    """Checking """

    ham.set_discount(10)
    belmarket.add_item(ham, banana)
    print('Overall goods price without discount :', belmarket.over_sum_no_discount)
    print('Overall goods price with discount :', belmarket.over_sum_yes_discount)
    belmarket.remove_item(ham)
    print('Overall goods price without discount:', belmarket.over_sum_no_discount)
    print('Overall goods price with discount:', belmarket.over_sum_yes_discount)
    ham.reset_discount()
    belmarket.add_item(ham)
    print('Overall goods price without discount:', belmarket.over_sum_no_discount)
    print('Overall goods price with discount:', belmarket.over_sum_yes_discount)
    try:
        belmarket.add_item(nail)
    except TypeError:
        print("This good isn't suitable for this store ")

    """Checking """

    saw.set_discount(50)
    oma.add_item(saw, nail)
    print('Overall goods price without discount :', oma.over_sum_no_discount)
    print('Overall goods price with discount:', oma.over_sum_yes_discount)
    oma.remove_item(saw)
    print('Overall goods price without discount :', oma.over_sum_no_discount)
    print('Overall goods price with discount:', oma.over_sum_yes_discount)
    saw.reset_discount()
    oma.add_item(saw)
    print('Overall goods price without discount :', oma.over_sum_no_discount)
    print('Overall goods price with discount:', oma.over_sum_yes_discount)
    try:
        oma.add_item(banana)
    except TypeError:
        print("This good isn't suitable for this store ")

    """Checking of price freezing"""

    try:
        nail.freeze_value = 6
        print('Price was changed on {}'.format(nail._price))
    except ValueError:
        print('Changing of price is denied')
    nail.freezing = False
    try:
        nail.freeze_value = 8
        print('Price was changed on {}'.format(nail._price))
    except ValueError:
        print('Changing of price is denied')

