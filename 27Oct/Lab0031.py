#list
my_list = [1,2,3,4]
print(my_list)
my_list[1] = 20
print(my_list)

#tupple  -  it is immutable in a nature (it content  not chage) denoted by ()
car = ("ford GT","nexon","crusoor")
print(type(car))
print(len(car))


#List can be converted on tupple

list1 = [1,2,3,4,5]
print(tuple(list1))

#tuple can be crasted in two ways
tuple1 = ()
tuple2 = (1,2,3,4) #1st way
tuple3 = tuple([1,2,3,4]) #2nd way

#merging of tuple
hero1 = ("bruce wayne","iron man")
hero2 = ("batman","thor")

h = hero1 + hero2
print(h)

#tuple to list conersion

print(list(h))