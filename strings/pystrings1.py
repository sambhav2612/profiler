# strr = 'Sambhav Jain'
# print strr
# strr[7] = 'X'   #immuntable
# print strr

a = 'Sambhav'
print a
a += ' Jain'    # works fine now - original string remains immutable - work done on the copy
print a

single = 'Single Quote String'
double = "Double Quote String"
triple = '''Triple Quote String'''
print single, double, triple

# slicing
print single[1:5]
print double[5:9]
print triple[9:12]

# methods
b = a.find("Jain")
print b          # returns index to where it finds the substring
b = a.rfind("a")
print b          # return last index to substring

# if-else in working
if (a.startswith("S") & a.endswith("n")):
    print "a starts with S and ends with n"
else : print "a does not starts with S and ends with n"

xx = 1
for x in range(0, len(a)):
    if a[x].islower():
        xx += 1
    else: xx -= 1
    if (xx % 2 == 0):
        print "Printing count only when it's even", xx