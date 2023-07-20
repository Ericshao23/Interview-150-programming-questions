# dict = {
# 		'a':1,
# 		'b':2,
# 		'c':3
# }
# # 遍历dict的key
# for key in dict.keys():    # 等价于 for key in dict:
#     print(key, dict[key])

# # 遍历dict的value
# for value in dict.values():
#     print(value)

# # 同时遍历dict的key和value
# for key, value in dict.items():
#     print(key, value)

# class Student(object):
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         print("This is __init__ method for Student")

# s = Student('Eric', '22', 'male')    
# print(s.name, s.age, s.gender)


# class Student(object):
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         print("This is __init__ method for Student")
    
#     def __new__(cls, *args, **kwargs):
#         print("This is __new__ method")
#         id = object.__new__(cls)
#         print(id)
#         return id

# s = Student('Eric', '22', 'male')    
# print(s.name, s.age, s.gender)
# print(s)    

# class Student(object):
#     def __init__(self,name):
#         self.name = name
# stu = Student("tom")
# print(type(stu),type(Student))
# print(stu.__class__, Student.__class__, stu.__class__.__class__)
# '''结果如下：
# <class '__main__.Student'> <class 'type'>
# <class '__main__.Student'> <class 'type'> <class 'type'>
# '''

# # str.find(str1, start, end) str1 为子串，start开始位置，end 结束位置
# # 若找到返回从0开始的下标位置，否则返回-1
# str1 = "This is a test case"
# print(str1.find('est', 0, len(str1)))
# print(str1.find('est', -4, -1))

# # str.index(str1, start, end) str1 为子串，start开始位置，end 结束位置
# # 若找到返回从0开始的下标位置，否则报错
# str1 = "This is a test case"
# print(str1.index('est', 0, len(str1)))
# print(str1.index('est', -4, -1))

# # in() 用于检查列表或者字符串中是否有指定元素
# str1 = "This is a test case"
# list1 = ["This", "is", "test", "case"]
# print('est' in str1)
# print('est' in list1)


# # count() 返回指定元素出现的次数
# str1 = "This is a test case"
# list1 = ["This", "is", "test", "case"]
# print(str1.count('est'))
# print(list1.count('est'))

# # startswith()函数用于检查字符串是否以指定前缀开头，并返回True或False。
# # endswith()函数用于检查字符串是否以指定后缀结尾，并返回True或False。
# str1 = "This is a test case, such as str, list"
# print(str1.startswith('This i'))
# print(str1.endswith('est'))


# 反转列表
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)