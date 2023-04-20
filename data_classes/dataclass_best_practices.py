# Do not declare default values with mutable types, depending on your IDE
# if you try to declare a default value with a mutable type, the IDE would
# produce a warning or even highlight an error

from dataclasses import dataclass, field
@dataclass
class ClubMember:
    name: str
    guest: list = [] # most likely this will show as syntax error on IDE

# use default_factory
@dataclass
class ClubMember:
    name: str
    guest: list = field(default_factory=list)
# the field function can accept arguments, default, default_factory,
# init, repr, compare, hash, metadata.



# Like everything in life, use but not abuse, data classes are very handy but
# is not good to overuse them or use them for the wrong purpose.
# It is very tempting to just use data classes as data holders and implement the
# data class behaviour all around on multiple files, this will give us code
# with low cohesion where related functionality is on multiple files and this
# makes the code hard to read (because you have to be jumping files constantly)
# and hard to maintain as is hard to keep track where functionality is (if
# you have all the behaviour (like login functionality) on one file is easy to
# maintain as you know all the code is on that file).
# It can be code smell if you see a data class that is only holding data but
# the data is being manipulated/interpreted on multiple places and not inside
# the data class itself.
# If you are using data classes as object-oriented programming keep in mind that object-oriented
# programming is the art of placing behaviour and data together, so the data
# class must hold data but also hold behaviour/functionality with it's own methods.


# so when is good idea to use data class.
# 1 - Data class on scaffolding:
#   The data class is an initial and simplistic implementation of a class to
#   quickly start a new module. With time the data class should use its own
#   methods and not rely on other classes methods or scatter functions to operate.

# 2 - Quick experimentation.
#   Yes this one goes for you 'Research Engineers', if you are just doing quick
#   experimentation then is ok to just leave a data class just holding data
#   and the data is being manipulated/interpreted outside the class.

# 3 - Data class as intermediate Representation.
#   This is the main reason why we use data classes at Darkroom, use a data class
#   to just build records that will just be exported to JSON or saved in file.
#   For example we use data class to hold mongodb data that will be exported
#   to JSON and returned by 'Strawberry'. In our case there is not much functionaly
#   apart from just exporting the data.
