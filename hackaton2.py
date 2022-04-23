'''
#problem 1
a = input('введите слово: ')
b = input('введите слово: ')
c = input('введите слово: ')
d = []
d.extend([a, b, c])

if len(a + b + c) > 20:
	print(d)
else:
	print('not long enough')
if len(a) > len(b) and len(a) > len(c):
	d.remove(a)
	print(a.upper())
elif len(b) > len(a) and len(b) > len(c):
	d.remove(b)
	print(b.upper())
else:
	d.remove(c)
	print(c.upper())
print(d)

'''
'''
#problem2
a = input('зарегистрируйтесь с помощью почты: ')
if a.endswith('@gmail.com') or a.endswith('@mail.ru'):
	print('123456')
else:
	print('не удалось определить почту')

b = int(input('подтвердите 6 значное число: '))
if b == 123456:
	print('вход успешен')
else:
	print('не удалось подтвердить почту')
a = 2897607
b = a // 3
c = a % 3
d = b * b
if c == 0:
        print(d)
        print(len(str(d)))
if len(str(d)) > 10:
        print(str(d).replace('3', '0'))
        print(str(d).replace('3', '0')[0:6])
'''
'''
#problem3
a = 2897607
b = a // 3
c = a % 3
d = b * b
if c == 0:
        print(d)
        print(len(str(d)))
if len(str(d)) > 10:
        print(str(d).replace('3', '0'))
        print(str(d).replace('3', '0')[0:6])


'''

'''
#problem4
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = (11, 12, 13, 14, 15, 16, 17)
c = list(b)

print(c)
a.extend(c)
print(a)
print(a[0], len(a)//2, a[-1])
'''


