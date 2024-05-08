class Stock:
    def __init__(self, symbol, price, investors=None):
        self.symbol = symbol
        self.price = price
        self.investors = investors if investors is not None else []

    def register_investor(self, investor):
        self.investors.append(investor)

    def unregister_investor(self, investor):
        self.investors.remove(investor) 

    def update_price(self, price):
        self.price = price
        for investor in self.investors:
            investor.update(self, price)
            
class Investor:
    def __init__(self, name, stocks):
        self.name = name
        self.stocks = stocks
    
    def update(self, stock, price):
        print(f"Stock {stock.symbol} was updated to new price {price}")