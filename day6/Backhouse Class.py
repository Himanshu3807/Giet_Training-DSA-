#Write a python program to implement BakeHouse class
class BakeHouse:
    def __init__(self):
        self.occupied_table_list = []

    def get_occupied_table_list(self):
        return self.occupied_table_list

    def allocate_table(self):
        for table_number in range(1, 11):
            if table_number not in self.occupied_table_list:
                self.occupied_table_list.append(table_number)
                return table_number
        return None

    def deallocate_table(self, table_number):
        if table_number in self.occupied_table_list:
            self.occupied_table_list.remove(table_number)

bh = BakeHouse()
print(bh.allocate_table())
print(bh.get_occupied_table_list())

print(bh.allocate_table())
print(bh.get_occupied_table_list())  

bh.deallocate_table(1)
print(bh.get_occupied_table_list()) 
        
