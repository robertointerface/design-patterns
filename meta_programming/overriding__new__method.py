"""
The __init__ method does not construct a class instance, it initializes it.
After all when __init__ is called it already receives 'self'.

The method that actually builds a class is __new__, this method can be overwritten
if required. By default classes use the __new__ method from objects.

"""
class SuperSayan:
    ALLOWED_FIGHTHERS = ['Goku', 'Vegeta']

    # __new__ is a class method but it does not need to have @classmethod
    # decorator because is super cool (just special way is treated by the
    # interpreter)
    # fighter_name here is passed to __init__ method.
    def __new__(cls, fighter_name):
        if fighter_name in cls.ALLOWED_FIGHTHERS:
            # here we just use super to call __new__ method all classes
            # inherit from object, this is object.__new__ which is implemented
            # in C in the deep guts of the interpreter
            return super().__new__(cls)
        raise TypeError(f'fighter {fighter_name} can not be a super sayan')

    def __init__(self, fighter_name):
        # note how the fighter name is passed even that don't pass it explicetely
        # on the __new__ method above, that is how special __new__ method
        # is.
        self.fighter_name = fighter_name

    def fight_bobo(self):
        print(f'{self.fighter_name} fighting with bo-bo')


if __name__ == "__main__":
    goku = SuperSayan('Goku')
    goku.fight_bobo()
    krillin = SuperSayan('Krillin')
