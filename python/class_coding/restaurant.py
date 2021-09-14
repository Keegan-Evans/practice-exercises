class Breakfast:

     def __init__(self, menu: dict):
         self.menu = menu
         self._order = []

     def order(self, *args):
         for item in args:
             if item not in self.menu:
                 print('sorry, you can\'t get %s here.' % item)
             self._order.append(item)
     def display_menu_items(self):
         for item in self.menu.keys():
             print(item)

     @property
     def sub_total(self):
         running_total = 0
         for item in self._order:
             running_total += self.menu[item]
         return running_total

     def show_total(self):
         print("With tax included, your total is %d" %
                 (self.sub_total * 1.08))


if __name__ == '__main__':

    menu = {'eggs': 0.50, 'bacon': 1.00, 'toast': 0.75}

    lucys = Breakfast(menu=menu)

    lucys.order('eggs', 'eggs', 'bacon')

    lucys.show_total()
