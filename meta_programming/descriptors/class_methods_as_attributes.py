"""Methods in a class are treated specially
"""



obj = Managed()
print(f'obj.spam {obj.spam}')
print(f'Managed.spam {Managed.spam}')
obj.spam = 7
print(f'obj.spam after overriding {obj.spam}')
print(f'Managed.spam after overriding {Managed.spam}')
