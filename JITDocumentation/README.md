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

#### Attributes of DirectMethod

DirectMethod does not have any unique attributes, however, mappings may have to be defined in inherited classes.
We can potentially avoid creating mappings for inherited classes, by giving DirectMethods numba attributes that
inherited non-numba attributes are cast too. However, I imagine this would not have ideal performance.

#### Classes used by DirectMethod

DirectMethod inherits StochPySSA_Shared

The constructor takes in model_file, model_dir, and IsQuiet=IsQuiet.
These maye have to be mapped and should match mappings in StochPySSA_Shared, as the Parse function is inherited from it.

```py
def Execute(self, settings, IsStatusBar=False):
```
type.

#### Inherited Attributes

IsStatusBar : numba boolean

settings : may need to be made into jit class

_IsInitial : numba boolean.

sim_t : unsure

X_matrix : numpy matrix

fixed_species_amount : unsure

timestep : numpy int

sim_output : numpy array

propensities_output : numpy array

V_output : numpy array

_IsTrackPropensities : will need to be defined in settings class

randoms_log : numpy array

randoms : numpy array

count : numpy int

sim_tau : numpy int

sim_r2 : numpy int

sim_a_mu : numpy array

N_matrix_transpose : numpy matrix

#### Functions

SpeciesSelection() | inherited from StochPySSA_Shared | several datatypes to be cast or mapped, many from settings

RateSelection() | inherited from StochPySSA_Shared | several datatypes to be cast or mapped, many from settings

SetEvents() | inherited from class CoreToPsc(object):

RunExactTimestep() | defined in DirectMethod.py itself

#TODO Finish analysis of functions