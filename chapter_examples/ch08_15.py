### Example 8-15: Access to outer scope from inner functions

class Value:
    """Hold a value, demonstrating some aspects of nested scope"""
    def __init__(self, v=None):
        self.val = v

    def get(self):
        return self.val

    def set(self, v):
        self.val = v

    def setter(self):
        """Return a function that can be called to change the value
        held by the instance"""
        return lambda newval: self.set(newval)

    def __str__(self):
        return str(self.get())

    def __repr__(self):
        return 'value({})'.format(self.get())

print()
v = Value()
print(v.get())
v.set(0)
print(v.get())
print()
print('__str__(v) ==', v)
print('__repr__(v) ==', repr(v))
fn = v.setter()
fn(9)
print()
print('__str__(v) ==', v)
print('__repr__(v) ==', repr(v))
