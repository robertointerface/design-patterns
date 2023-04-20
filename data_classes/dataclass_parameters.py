# when initializing a dataclass as a decorator the decorator accepts several
# keywords arguments
# @dataclass(*, init=True, repr=True, eq=True, order=False,
#              unsafe_hash=False, frozen=False)
# init : means that will automatically generate the __init__ (default True),
#   if the __init__ is implemented by the user it is ignored
# repr: automatically generates __repr__ method (default True), ignored if __repr__ is
#   implemented by user.
# eq: automatically generates __eq__ method (default True), ignored if __repr__ is
# #   implemented by user.
# order: generaters __lt__, __le__, __gt__, __ge__ methods (default False),
# these methods are used when sorting instances, either by using operator
# overloading like < > or sorting methods
#
# unsafe_hash: generates __hash__ (default False)
# frozen: makes it immutable (default False)
