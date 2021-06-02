from src.dao import CategoryDAO, ProductDAO
from src.models import Category, Product


def view():

    option = True
    while option:
        print(
            """
        1.Adicionar Produto
        2.Listar Produtos
        3.Adicionar Categoria
        4.Listar Categoria
        5.Sair
        """
        )
        option = input("Digite a opção desejada: ")
        if option == "1":
            product_name = input("Digite o nome do produto: ")
            product_description = input("Digite a descrição do produto: ")
            product_price = input("Digite o preço do produto: ")
            product = Product(product_name, product_description, product_price)
            ProductDAO().save(product)

        elif option == "2":
            product_list = ProductDAO().read()
            for product in product_list:
                print(product)

        elif option == "3":
            category_name = input("Digite o nome da categoria: ")
            category_description = input("Digite a descrição da categoria: ")
            category = Category(category_name, category_description)
            CategoryDAO().save(category)

        elif option == "4":
            for category in CategoryDAO().read():
                print(category)

        elif option == "5":
            option = False
            print("Valeu")

        elif option != "":
            print("\n Opção inválida")
