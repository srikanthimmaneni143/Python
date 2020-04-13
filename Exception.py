
a=5
b=0


try:
    c=a/b
except Exception as reason:
    print('ERROR: ',reason)
finally:
    print('Have a gud day')
