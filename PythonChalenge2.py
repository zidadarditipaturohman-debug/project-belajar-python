number = ("+49 (176) 123-456")
print(number.replace("+", "00").replace("-", "").replace(" ", "").replace("(", "").replace(")", ""))

First = ("Zidad")
last = ("Arditi")

print(First + " " + last)

#so i can use split to replace all data and using ","
#for example
random1= "18-02-2004 12:45"
print(random1.split(" "))
print(random1.split("-"))
print(random1[0:4])

full_name = "Zidad Arditi Paturohman"
print(full_name[:5])

variavle_strip = " pionir dialektika"
print(variavle_strip.lstrip()) #lstrip use to remove space on first word L for left
Varaible_rstrip = "Pionir dialektika  "
print(Varaible_rstrip.rstrip()) #rstrip use to remove space in the end sentence.
variable_strip1 = "  Pionir Dialektika  "
print(variable_strip1.strip()) #Strip use  to remove first and end sentence, but it cannot remove inside sentence
Variable_strip2 = "####Pionir Dialektika####"
print(Variable_strip2.strip("#")) #strip also can remove some spesifik letter on sentence

#whitspaceClean
# this used to know my data clean or no
data1 = "  pionir"
total = print(len(data1))
after_Clean = print(len(data1.strip()))

total_space = len(data1) - len(data1.strip())
my_data_clean = len(data1) == len(data1.strip())
print(total_space)
print(my_data_clean)