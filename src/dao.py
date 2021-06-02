class DAO:
    @staticmethod
    def writer(data, file_name):
        with open(f"{file_name}.txt", "a") as text:
            text.writelines(f"{data}\n")

    @staticmethod
    def reader(file_name):
        with open(f"{file_name}.txt", "r") as file:
            obj_list = []
            all_items = file.readlines()
            for item in all_items:
                item = item.replace("\n", "")
                obj_list.append(item)
            return obj_list


class ProductDAO(DAO):
    def save(self, data):
        self.writer(data, "product")
        return data

    def read(self):
        return self.reader("product")


class CategoryDAO(DAO):
    def save(self, data):
        self.writer(data, "category")
        return data

    def read(self):
        return self.reader("category")
