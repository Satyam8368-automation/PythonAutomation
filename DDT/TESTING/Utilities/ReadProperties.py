import configparser


def readData(file_path):
    con=configparser.ConfigParser()
    con.read(file_path)
    return con
file_path= "C:\\Users\\ADMIN\\PycharmProjects\\DDT\\TESTING\\Data.ini"
properties=readData(file_path)
# print(properties.get("Login","Url"))

# properties =readData(file_path="C:\Users\ADMIN\PycharmProjects\DDT\TESTING\Data.ini")
