# Improving StochPy Performance with JIT

To see the greatest performance improve with the least amount of JIT compilation, we want to identify the most 
computationally expensive blocks of code. This is the SSA.Execute() method in the DirectMethod.py class.

The DirectMethod class inherits from the StochPySSA_Shared class. If it is necessary to make
the DirectMethod class into a JIT class, it will be necessary to make the StochPySSA_Shared class into a jit class.
The StochPySSA_Shared class is in StochPyTools.py. It is a decently large class with 11 functions.
It doesn't inherit any other classes. However, both DirectMethod and StochPySSA_Shared implement other classes.

## Using Numba

#### Numba documentation: https://numba.readthedocs.io/en/stable/
#### JIT Class documentation: https://numba.readthedocs.io/en/stable/user/jitclass.html

To declare a Jit Class, we want to use the @jitclass() decorator and pass in a tuple or list that maps the python
variables to numba types. e.g.

```py
spec = [
    ('value', int32),               # a simple scalar field
    ('array', float32[:]),          # an array field
]

@jitclass(spec)
class Bag(object):
    def __init__(self, value):
        self.value = value
        self.array = np.zeros(value, dtype=np.float32)

    @property
    def size(self):
        return self.array.size

    def increment(self, val):
        for i in range(self.size):
            self.array[i] += val
        return self.array

    @staticmethod
    def add(x, y):
        return x + y
```
Numba types:

| Type name(s)    | Shorthand |                               Comments |
|-----------------|:---------:|---------------------------------------:|
| boolean         |    b1     |                  represented as a byte |
| uint8, byte     |    u1     |                 8-bit unsigned integer |
| uint16          |    u2     |                16-bit unsigned integer |
| uint32          |    u4     |                32-bit unsigned integer |
| uin64           |    u8     |                64-bit unsigned integer |
| int8, char      |    i1     |                      8-bit signed byte |
| int16           |    i2     |                  16-bit signed integer |
| int32           |    i4     |                  32 bit signed integer |
| int64           |    i8     |                  64-bit signed integer |
| intc            |           |                    C int-sized integer |
| uintc           |           |           C int-sized unsigned integer |
| intp            |           |                  pointer-sized integer |
| uintp           |           |         pointer-sized unsigned integer |
| float32         |    f4     | single-precision floating-point number |
| float64, double |    f8     | double-precision floating-point number |
| complex64       |    c8     |        single-precision complex number |
| complex128      |    c16    |        double-precision complex number |

## Classes to JIT Compilation:

### DirectMethod

#### Inherits StochPySSA_Shared

#### Constructor:
```py
def __init__(self,model_file,model_dir,IsQuiet=False):    
    self.Parse(model_file,model_dir,IsQuiet=IsQuiet)
```