#       დავალება 1.

# დაწერეთ ფუნქცია, რომელიც უბრალოდ აბრუნებს არგუმენტად 
# გადაწოდებულ რიცხვს, დაუწერეთ დეკორატორი, რომელიც 
# შეამოწმებს, რომ რიცხვი უნდა იყოს დადებითი, თუ არის 
# უარყოფითი ამ შემთხვევაში დააბრუნეთ ValueError შესაბამისი
#  ტექსტით, სხვა შემთხვევაში აამოქმედეთ ფუნქცია, შედეგი 
# კი დაბეჭდეთ დეკორატორიდან.
# from typing import Any


# def check_positive(func):
#     def wrapper(number):
#         if number < 0:
#             raise ValueError("number must be positive")
#         result = func(number)
#         print(f"result: {result}")
#         return result
#     return wrapper

# @check_positive
# def return_number(number):
#     return number

# try:
#     return_number(5)
#     return_number(-5)
# except ValueError as e:
#     print(e)


# დავალება 2.

# დაწერეთ პირველი დავალება ფუნქტორის გამოყენებით

# class check_positive:
#     def __init__(self, func):
#         self.func = func
#     def __call__(self, number):
#         if number < 0:
#             raise ValueError("number must be positive")
#         result = self.func(number)
#         print(f"result: {result}")
#         return result
# @check_positive
# def return_number(number):
#     return number

# try:
#     return_number(5)
#     return_number(-5)
# except ValueError as e:
#     print(e)

# დავალება 3.

# დაწერეთ დეკორატორი, რომელიც გამოთვლის ფუნქციის მოქმედების 
# დროს და დაბეჭდავს ტერმინალში. დროის აღსაქმელად გამოიყენეთ
#  time.time()
# import time
# def masure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         elapsed_time = end_time - start_time
#         print(f"Function{func.__name__} took {elapsed_time}")
#         return result
#     return wrapper
# @masure_time
# def measure_time(n):
#     total = 0
#     for i in range(n):
#         total += i
#     return total
# measure_time(1000000)    


# დავალება 4.

# შექმენით მეტაკლასი LoggingMeta, რომელიც ყოველი კლასის 
# შექმნის დროს დაბეჭდავს თუ რა სახელის მქონე კლასი იქმნება.

class LogginigMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"creating class: {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=LogginigMeta):
    pass
class AnotherClass(metaclass=LogginigMeta):
    def method(self):
        pass