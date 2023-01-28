from menu import products

def get_product_by_id(product_id):
    if type(product_id) != int:
        raise TypeError('product id must be an int')

    if product_id == int(product_id):
        for item in products:
            if item['_id'] == product_id:
                return item
        else:
            return {}

def get_products_by_type(product_type):
    if type(product_type) != str:
        raise TypeError('product type must be a str')
    new_products = []
    for item in products:
        if item['type'] == product_type:
            new_products.append(item)
    return new_products


def add_product(original_menu: list, **kwargs):
    original_menu.append(kwargs)
    qtd_id = len(original_menu)
    original_menu[-1]['_id'] = qtd_id

    return kwargs

def menu_report():
    sum_price = 0
    product_count = len(products)
    for item in products:
        sum_price += item['price']
    average_price = round(sum_price/product_count, 2)
    common_type = max(products, key=products.count)['type']

    return f'Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {common_type}'
