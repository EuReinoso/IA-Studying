from product import Product

product_list = []
product_list.append(Product("Geladeira Dako", 0.751, 999.90))
product_list.append(Product("Iphone 6", 0.0000899, 2911.12))
product_list.append(Product("TV 55' ", 0.400, 4346.99))
product_list.append(Product("TV 50' ", 0.290, 3999.90))
product_list.append(Product("TV 42' ", 0.200, 2999.00))
product_list.append(Product("Notebook Dell", 0.00350, 2499.90))
product_list.append(Product("Ventilador Panasonic", 0.496, 199.90))
product_list.append(Product("Microondas Electrolux", 0.0424, 308.66))
product_list.append(Product("Microondas LG", 0.0544, 429.90))
product_list.append(Product("Microondas Panasonic", 0.0319, 299.29))
product_list.append(Product("Geladeira Brastemp", 0.635, 849.00))
product_list.append(Product("Geladeira Consul", 0.870, 1199.89))
product_list.append(Product("Notebook Lenovo", 0.498, 1999.90))
product_list.append(Product("Notebook Asus", 0.527, 3999.00))


def gen_lists():
    names = []
    spaces = []
    valors = []
    for product in product_list:
        names.append(product.name)
        spaces.append(product.space)
        valors.append(product.price)
    return names,spaces,valors


