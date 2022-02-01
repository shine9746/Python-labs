a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

toseta = set(a)      #converted list to set
tosetb = set(b)

common = toseta & tosetb  #condition applied

tolist = list(common)   #converted back to list 

print(tolist)

print(type(tolist))

