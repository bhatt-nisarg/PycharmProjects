#declaration
s = set()

print(type(s))

#big set
l = [1, 2, 3, 4]
s_from_list = set(l)
# you can also write this set([1, 2, 3, 4,])
print((s_from_list))
print(type(s_from_list))


#add
s.add(1)
s.add(1)#set add unique value dont take same value second time

s.add(2)
s1 = s.union({1, 2, 3})
print(s)

s1 = s.intersection({1, 2, 3})
print(s1)
s.remove(2)
print(s, s1)

#function
print(max(s1))

s2 = {4, 5}
#disjoit means not a same number
print(s.isdisjoint(s2))