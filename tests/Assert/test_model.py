from src.models import Category, Product


def test_product():

    product = Product()
    assert type(product) == Product
    assert isinstance(product, Product)

    name = "Stella"
    description = "Melhor cerveja, de milho,  do mundo"
    value = 0.89

    product.name = name
    product.description = description
    product.value = value

    assert product.name == name
    assert product.description == description
    assert product.value == value

    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.value, float)


def test_category():

    category = Category()
    assert type(category) == Category
    assert isinstance(category, Category)

    name = "Cerveja de trigo"
    description = "Trigo de melhor qualidade"

    category.name = name
    category.description = description

    assert category.name == name
    assert category.description == description

    assert isinstance(category.name, str)
    assert isinstance(category.description, str)
