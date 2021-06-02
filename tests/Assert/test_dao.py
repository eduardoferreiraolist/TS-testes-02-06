from src.dao import DAO, CategoryDAO, ProductDAO
from src.models import Category, Product


def test_product_dao():

    dao = ProductDAO()
    assert type(dao) == ProductDAO
    assert isinstance(dao, ProductDAO)
    assert issubclass(ProductDAO, DAO)

    data = Product("teste", 10, "desc")

    assert dao.save(data) == data
    assert dao.read()[-1] == str(data)


def test_category_dao():

    dao = CategoryDAO()
    assert type(dao) == CategoryDAO
    assert isinstance(dao, CategoryDAO)
    assert issubclass(CategoryDAO, DAO)

    data = Category("teste", "desc")

    assert dao.save(data) == data
    assert dao.read()[-1] == str(data)
