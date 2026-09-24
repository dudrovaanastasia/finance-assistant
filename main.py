from models.category import Category
from models.transaction import Transaction

if __name__ == "__main__":
    food_category = Category("Food", "Expenses for groceries and restaurants")
    t1 = Transaction(100, food_category.name, "2023-10-25")
    print(food_category)
    print(t1)