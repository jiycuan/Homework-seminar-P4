with open("5_one.txt", "r") as file:
    poly_1 = file.read()
with open("5_one_too.txt", "r") as file:
    poly_2 = file.read()

poly_1 = str.replace(poly_1, "- ", "+ -").split()
poly_2 = str.replace(poly_2, "- ", "+ -").split()

poly_1 = list(filter(lambda x: x != "+" and x != "=" and x != "0", poly_1))

print(poly_1)

my_file = open("5_result.txt", "w+")
my_file.write(poly_1)
my_file.close()