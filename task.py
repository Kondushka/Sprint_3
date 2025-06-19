class OnlineSalesRegisterCollector:
    def __init__(self):
          self.__name_items = []
          self.__number_items = 0
          self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
          self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    def add_item_to_cheque(self, name):
        try:
            if len(name)==0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            if name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            # if name in self.__name_items:
            #     self.delete_item_from_check(name)
            #     return
            self.__name_items.append(name)
            self.__number_items+=1
            print(f'Список товаров в чеке: {self.__name_items}')
            print(f'Кол-во товаров в чеке: {self.__number_items}')
        except (ValueError, NameError) as e:
            print(e)  

                 
    def delete_item_from_check(self,name):
        try:
            if name not in self.__name_items:
              raise NameError('Позиция отсутствует в чеке')
            self.__name_items.remove(name)
            self.__number_items-=1
            print(f'Удаление товара: {name}')
            print(f'Кол-во товаров в чеке после удаления: {self.__number_items}')
        except NameError as e:
            print(e)
        
    def check_amount(self):
        total=0
        for i in self.__name_items:
            total += self.__item_price[i]
        if len(self.__name_items) > 10:
            total*=0.9
        print(f'Общая сумма чека: {total}')

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax=[]
        self.nds_20=0
        total=0
        for i in self.__name_items:
            if self.__tax_rate[i] == 20:
                twenty_percent_tax.append(i)
                total+=self.__item_price[i]
        if len(self.__name_items) > 10:
            total *= 0.9

        self.nds_20=total*0.2

        print(f'Товары с налогом 20%: {twenty_percent_tax}')
        print(f'Общая стоимость товаров с налогом 20%: {total}. Сумма налога: {self.nds_20}.')

    def ten_percent_tax_calculation(self):
        ten_percent_tax=[]
        self.nds_10=0
        total=0
        for i in self.__name_items:
            if self.__tax_rate[i] == 10:
                ten_percent_tax.append(i)
                total+=self.__item_price[i]
        if len(self.__name_items) > 10:
            total *= 0.9
            
        self.nds_10=total*0.1

        print(f'Товары с налогом 10%: {ten_percent_tax}')
        print(f'Общая стоимость товаров с налогом 10%: {total}. Сумма налога: {self.nds_10}.')

    def total_tax(self):
        nds = self.nds_20 + self.nds_10
        print(f'Общая сумма НДС: {nds}')

    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            if type(telephone_number) != int:
                raise ValueError('Необходимо ввести цифры')
            if len(str(telephone_number)) != 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            print(f'+7{telephone_number}')
        except ValueError as e:
            print(e)  
        


         
unit=OnlineSalesRegisterCollector()
unit.add_item_to_cheque('чипсы')
unit.add_item_to_cheque('молоко')
unit.add_item_to_cheque('печенье')
unit.add_item_to_cheque('квас')
unit.add_item_to_cheque('')
unit.add_item_to_cheque('печенье')
unit.add_item_to_cheque('кефир')
unit.add_item_to_cheque('молоко')
unit.delete_item_from_check('молоко')
unit.delete_item_from_check('кефир')
unit.delete_item_from_check('печенье')
unit.delete_item_from_check('кола')
unit.delete_item_from_check('квас')
unit.delete_item_from_check('')
unit.add_item_to_cheque('кола')
unit.add_item_to_cheque('чипсы')
unit.add_item_to_cheque('кефир')
unit.add_item_to_cheque('кефир')
unit.add_item_to_cheque('кефир')
unit.add_item_to_cheque('кефир')
unit.add_item_to_cheque('кефир')
unit.add_item_to_cheque('кефир')
unit.check_amount()
unit.twenty_percent_tax_calculation()
unit.ten_percent_tax_calculation()
unit.total_tax()
unit.get_telephone_number(8765432198)
unit.get_telephone_number('djnsdf')
unit.get_telephone_number(87654321)