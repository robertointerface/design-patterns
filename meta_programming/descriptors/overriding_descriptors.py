def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return f'<class {obj.__name__}>'
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return f'<{cls_name(obj)} object>'



def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print(f'-> {cls_name(args[0])}.__{name}__({pseudo_args})')


class Overriding:
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class OverridingNoGet:

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOverriding:

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print(f'-> Managed.spam({display(self)})')

obj = Managed()
print(f'obj.spam {obj.spam}')
print(f'Managed.spam {Managed.spam}')
obj.spam = 7
print(f'obj.spam after overriding {obj.spam}')
print(f'Managed.spam after overriding {Managed.spam}')

