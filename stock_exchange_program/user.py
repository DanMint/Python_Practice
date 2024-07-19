class User:
    def __init__(self, assets):
        self.total_money = assets
        self.stock_owned = []
        self.stock_total_val = 0
        self.crypto_owned = []
        self.crypto_total_cal = 0
        
    def add_stock(self, stock, amount_bought):
        if self.total_money < (stock[1] * amount_bought):
            print("Not enough money")
            return
        
        input_stock = [i for i in stock]
        input_stock.append(amount_bought)

        self.stock_owned.append(input_stock)

    @property
    def get_total_money(self):
        return self.total_money

    @property
    def get_stocks(self):
        return [i[0] for i in self.stock_owned]
    
    @property
    def get_total_stock_val(self):
        return self.stock_total_val