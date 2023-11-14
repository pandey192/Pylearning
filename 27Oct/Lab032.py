#multiple value asign possible in tuple

a,b = 23,24 #this is multiple value asign
q,w,e = (23,24,25)
print(q)
print(w)
print(e)

#nested tuple

hero1 = ("bruce wayne","iron man")
hero2 = ("batman","thor")

h = hero1 , hero2   # nested tupple can be genrate by ","
print(h)
print(h[0])
print(h[1])
print(h[0][1])

#Search in tuple - by in operator

cities = ("london","Delhi","mumbai","cicago","bangalore")
print("Delhi" in cities)    # result will be in Ture / false