# what are attributes?
# data attributes and methods are collectively known as attributes in python


class DragonBallFighter:

    def __init__(self, speed, damage):
        # these are data attributes
        self.speed = speed
        self.damage = damage

    # this is a method, which is a callable attribute
    def combo_attack(self, number_of_punches):
        return number_of_punches * self.speed * self.damage


# what are dynamic attributes?
# dynamic attributes are the same as data attributes but are computed on demand

class LiverpoolClub:

    def __init__(self, coach):
        self.coach = coach

    @property
    def current_goals_at_season(self):
        # here call some api that will give you the current goals which can
        # vary depending on the day so the result today can be different
        # than the result tomorrow.
        pass

# how do we implement dynamic attributes?
# multiple ways but we will cover for now the most basic ones.
# 1 - @property decorator.
# 2 - __getattr__ special method, these are normally referred to as virtual
# attributes, attributes that are not explicitly declared anywhere in the source
# code of the class and are not present in the instance __dict__, but are retrieved
# from somewhere else or computed on the fly.



