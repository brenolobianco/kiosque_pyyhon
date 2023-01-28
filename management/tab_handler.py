from menu import products

def calculate_tab(table):
    sum = 0
    for item_table in table[::]:
        for item_products in products:
            if item_table['_id'] == item_products['_id']:
                sum = item_products['price']*item_table['amount'] + sum
        subtotal = round(sum, 2)

    return {f"subtotal": f"${subtotal}"}
