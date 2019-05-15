class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None, total = 0, items = []):
      self.employee_discount = employee_discount
      self.total = total
      self.items = items
    def add_item(self, name, price, quantity=1):
      for i in range(0, quantity):
        self.items.append({name: price})
      self.total += (price * quantity)
      return "${:,.2f}".format(self.total)
       
    def mean_item_price(self):
        mean_values = self.total/len(self.items)
        return mean_values

    def median_item_price(self):
        prices = []
        for i in self.items:
            prices.append([x for x in i.values()][0])
        prices.sort
        if len(prices)%2 != 0:
            return prices[len(prices)//2]
        else:
            return (prices[len(prices)//2] + prices[(len(prices)//2) + 1])/2
        

    def apply_discount(self):
       if self.employee_discount == None:
           return("Sorry, there is no discount to apply to your cart :(")
       else:
           discount_total = self.total * (1 - (self.employee_discount/100))
           return "${:,.2f}".format(discount_total)
           
    def void_last_item(self):
        if len(self.items)==0:
            return "There are no items in your cart!"
        else:
            self.total -= [x for x in self.items[-1].values()][0]
            self.items.pop()