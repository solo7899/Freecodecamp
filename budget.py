from math import trunc


class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category
        self.__balance = 0
        self.spent = 0
        
    def __repr__(self) -> str:
        text = [self.category.center(30, '*'),]
        for item in self.ledger:
            des = item['description'][:23]
            amount = f'{item["amount"]:.2f}'
            ft = f"{des}{' ' *(30 - sum([len(des), len(amount)]))}{amount}"
            text.append(ft)
        total = f'Total: {self.__balance:.2f}'
        text.append(total)
        return '\n'.join(text)
        
    def deposit(self, amount, description=""):
        self.ledger.append(
            {"amount": amount,
             "description": description,
            }
        )
        self.__balance += amount
        
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": -amount,
                "description": description,
                }
            )
            self.__balance -= amount
            self.spent += amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance
    
    def transfer(self, amount, instance):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {instance.category}")
            instance.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
            
    def check_funds(self, amount):
        return amount <= self.__balance
    
    
def create_spend_chart(categories:list) -> str:
    # categories.sort(key=lambda x: x.category)
    title = "Percentage spent by category"
    labels = {
        '100|':[],
        ' 90|':[],
        ' 80|':[],
        ' 70|':[],
        ' 60|':[],
        ' 50|':[],
        ' 40|':[],
        ' 30|':[],
        ' 20|':[],
        ' 10|':[],
        '  0|':[],
    }
    
    percentages =[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    whole_withdraw = sum([i.spent for i in categories])
    cat_spent_per = []
    for item in categories:
        cat_spent_per.append([item.category, trunc((item.spent/whole_withdraw* 100)/10) *10])
    # cat_spent_per.sort(key=lambda x: x[0])
    
    for item in cat_spent_per:
        for j in percentages:
            if j <= item[1]:
                labels[f"{j}|".rjust(4)].append('o')
            else:
                labels[f"{j}|".rjust(4)].append(" ")
                
    txt = ''
    txt += title + '\n'
    max_len = 0
    for key, value in labels.items():
        txt += f"{key} {'  '.join(value)}  \n"
        if len('  '.join(value)) > max_len:
            max_len = len('  '.join(value))
    txt += '    ' + (max_len + 3) * '-' + '\n'
    
    names = [item.category for item in categories]
    max_length = max([len(item) for item in names])
    names = [item.ljust(max_length) for item in names]
    for i in range(max_length):
        chars_partition = '   '
        for name in names:
            chars_partition += f'  {name[i]}'
        if i + 1 != max_length:
            chars_partition += '  \n'
        else:chars_partition += '  '
        txt += chars_partition
        
    return txt
    
    
if __name__ == "__main__":
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")
    
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    actual = create_spend_chart([business, food, entertainment])
    
    print(actual)
    