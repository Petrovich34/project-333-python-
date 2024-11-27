
#
# print("File open")
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     c = a / b
#     print("Data save")
#     print(c)
# except:
#     print("Error in file")
# finally:
#     print("File closing")
#
# print("Stop")


# def checker(var):
#     if type(var) != str:
#         raise TypeError(f"var {type(var)}is not string")
#     return var
#
# try:
#     a = 10
#     print(checker(a))
# except(Exception) as ex:
#     print(ex)


names = {"Serg":20, "Anna":15}
print(names["Anna"])
keys = list(names.keys())
if n not in keys:
    raise
print(keys)
names.get("Serg211")