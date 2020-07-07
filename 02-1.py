# Print() Play

# Separator
print('T', 'E', sep='')
print('2020', '07', '02', sep='-')
print('niceman', 'google.com', sep='@')

# end
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

# format [], {}, ()
print('{} and {}' .format('You', 'Me'))
print('{0} and {1} and {0}' .format('You', 'Me'))
print('{a} and {b}' .format(a='You', b='Me'))

# %s, %d, %f
print("%s is string, %d is int, %f is float" % ("jun", 123, 0.1123))

print("Test1: {0: 5d}, Price{1: 4.2f}". format(123, 1234.123))
print("Test1: {a: 5d}, Price{b: 4.2f}". format(a=123, b=1234.123))