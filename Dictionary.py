
#=============================================================================
#Dictionaries
Family= {"Key1":1991,"Key2":1994,"Key3":[1966,1991,1994,(2022,22,[23,34])],"Key4":1954}

print(Family["Key3"])

del(Family["Key1"])
print(type(Family))
print(Family)
#print(Family.values())

Family["Key6"]="Suhail"
print(Family)


#Lists
List1=["suhail", 'Soha', 12,1991,[45,"suhail",(23,34),[34,56,"kk"]]]
print(List1)



List1[4]=12

List1= List1+[23,34]
print(List1)
List1.extend([45,56,[3,4]])
print(List1)
List1.append([67,45])
print(List1)
del(List1[0])
print(List1)

# =============================================================================
Cool="Hi Suhail , How are you doing today Suhail ? ".split()

print(Cool)
Cool2 = set(Cool)
print(Cool2)
Cool2.add("todays")
print(Cool2)
Cool2.remove('today')
print(Cool2)
# =============================================================================
List= [1,2,3,4,5,6,7,8,9,10,1,2,3,0]
print(List)


#=============================================================================
Set=set(List)
print(Set)
Set2={2,3,4,5,10.34}
Set2.add(44)
Set.remove(4)
print(4 in Set)
print(Set2)
Combined_Set= Set.union(Set2)
print(Combined_Set)
print(Set,Set2)
#=============================================================================

# =============================================================================



#Touples
# =============================================================================
Tuple1= (8,7,[2,3,4],("ss,ff","ff"))
Tuple2=Tuple1+(99,90)

Tuple2= Tuple2+(0,(98,988))

Tuple1=(99,(99,32,230),"Silk")

print(Tuple1)
print(Tuple2)
print(type(Tuple1))
print(List1[2])

print((Tuple2[-1][1]))

print(Tuple2[0:4])


print(Family)

print(Family.keys())
print(Family.values())

say_what= ('say', 'what', 'you','will')

print(type(say_what[1]))

print(type(say_what))

Family2={"Key1":(1,2,3),'Key2':"hello", "Key3":345, "Marvel":'Swati'}
print(Family2.keys())
print(type(Family["Key3"]))
# 
# =============================================================================

