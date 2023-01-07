from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Cookie_orders:
    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.cookie_type= data['cookie_type']
        self.num_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_orders"
        results = connectToMySQL('cookie_orders').query_db(query)
        orders=[]
        for row in results:
            print(row)
            orders.append(cls(row))
        return orders

    @classmethod
    def create(cls, data):
        query= """
                INSERT INTO cookie_orders (name, cookie_type, number_of_boxes )
                VALUES(%(name)s, %(cookie_type)s, %(number_of_boxes)s)
                """
        return connectToMySQL('cookie_orders').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cookie_orders where id = %(id)s;"
        results = connectToMySQL('cookie_orders').query_db(query, data)
        return cls(results[0])

    @classmethod
    def edit_cookie(cls, data):
        query = f"UPDATE cookie_orders SET name=%(name)s, cookie_type=%(cookie_type)s, number_of_boxes=%(number_of_boxes)s where id=%(id)s" 
        return connectToMySQL('cookie_orders').query_db(query, data)

    @staticmethod
    def user_validate(cookie_data):
        print('in user validate')
        is_valid = True
        if len(cookie_data['name']) <=2:
            flash("Name must be atleast 2 characters!")
            is_valid= False
        if len(cookie_data['cookie_type']) <=2:
            flash("Cookie type must be atleast 2 characters!")
            is_valid= False
        if len(cookie_data['number_of_boxes']) <=0:
            flash("Please select a value greater than 0!")
            is_valid= False
        print(is_valid)
        return is_valid
