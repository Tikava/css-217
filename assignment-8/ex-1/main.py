from stock import Stock, Investor

def main():
    
    stock1 = Stock("BTC", 62500, None)
    stock2 = Stock("ETC", 3000, None)
    
    stocks = [stock1, stock2]
    
    investor1 = Investor("Toilybay", stocks)
    investor2 = Investor("Almat", [stock1])
    
    stock1.register_investor(investor1)
    stock1.register_investor(investor2)
    
    stock2.register_investor(investor1)
    
    stock1.update_price(63000)
    stock2.update_price(3030)

if __name__ == "__main__":
    main()