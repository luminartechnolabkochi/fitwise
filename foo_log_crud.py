

from  mysql.connector import connect


class FoodLogCreateListRetriveUpdateDelete:

    def __init__(self,user=None,password=None,database=None):


        self.con = connect(
            user=user,
            host="localhost",
            password=password,
            database=database
        )

        self.cursor= self.con.cursor()

    def get(self):

        query = "select * from food_log"

        self.cursor.execute(query)

        records=self.cursor.fetchall()

        print(records)

    def post(self,title=None,meal_type=None,calories=None,serving_size=None,owner=None):

        query ="""

                insert into food_log (title,meal_type,calories,serving_size,owner) values(%s,%s,%s,%s,%s)
            """

        values=(title,meal_type,calories,serving_size,owner)

        self.cursor.execute(query,values)

        self.con.commit()

        print("food log added....")





food_log = FoodLogCreateListRetriveUpdateDelete(user="root",password="Password@123",database="fitwise_db")



food_log.post(title="tea",meal_type="break_fast",calories=100,serving_size="100ml",owner="hari")

food_log.get()
