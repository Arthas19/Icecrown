
# Don't Fear the Reaper // nebojte se ripera
print ("Hello World")

# skup
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}

for i in a:
    print (i ** 2)

str = 'Cao cao treniras'

# list
arr = ['cao', 'cao3', 'treniras']

print (str[0:9])
print (arr[1])
print (arr[-1])

# recnik(mapa)
dic = {'name':'milan', 'age':19, 'the':'heist'}

print (dic)

print (dic['age'])
print (dic.keys())
print (dic.values())
print (dic.get(19))

#z = raw_input("upisite nesto: ")
squares = [1, 4, 9, 16, 25]
squares = squares + [36, 49, 64, 81]

print (squares)

if len(squares) < 5:
    print ('Still Dree')
else:
    print ('Back in the game')

for i in range(7, 10) :
    print (i)
