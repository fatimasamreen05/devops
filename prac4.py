#4 Write a program to demonstrate working with tuples in python
tuple1 = (1,2,3,4,5)
print(f'original tuple{tuple1}')
#printing first & last element of tuple
print(f'the first element{tuple1[0]},the last element {tuple1[-1]}')
#slincing tuple
print(f'sliced tuple(from index 1-3) {tuple1[1:4]}')
#concatenate tuples
tup1 = (12,13,14)
tup2=(10,11)
concatinated_tuples = tup2+tup1
print("concatenated tuple",concatinated_tuples)
#length
length_tup = (len(tuple1))
print("length:",length_tup)
#nested tuple
nested_tuple = (1,(2,3),(4,5,6))
print("printing 2 element in 2 tuple",nested_tuple[2][2])
#unpacking a tuple
a,b,c,d,e = tuple1
print(f'unpacked values: {a},{b},{c},{d},{e}')
#checking item exists or not
num = int(input("enter number"))
if num in tuple1:
    print("available")
else:
    print("not available")



