#to_weird_case('String') # => returns 'StRiNg'
#to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
#to_weird_case('This') # => returns 'ThIs'
#to_weird_case('is') # => returns 'Is'
#to_weird_case('This is a test') # => returns 'ThIs Is A TeSt'

to_weird_case = lambda s: ''.join([to_weird_casee(w) for w in s.split(' ')])
to_weird_casee = lambda s: ''.join([c.lower() if i%2 else c.upper() for i,c in enumerate(s)])
print(to_weird_case('String'))
print(to_weird_case('Weird string case'))
print(to_weird_case('This'))
print(to_weird_case('is'))
print(to_weird_case('This is a test'))