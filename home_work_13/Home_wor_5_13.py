# Write a Python program to add two given lists using map and
# lambda.(map-y kara function-ic heto mekic avel hajordakanutyun
# ynduni, orinak erku list)
a = [2,4,8]
b = [1,2,3]
c = map(lambda x,y:x+y,a,b)
print(list(c))