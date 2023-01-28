from menu import products
from management.product_handler import  get_product_by_id,add_product,menu_report
from management.tab_handler import  calculate_tab

new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }   

if __name__ == "__main__":
   
    print(get_product_by_id(5)) 


   
