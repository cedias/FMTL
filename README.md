# FMTL: a Field-Mappable Tuple List

## Requirements:

- TQDM

## Install:
via pip: `pip install -e git+https://github.com/cedias/FMTL.git`

## Usage

Let's say you have a tuple list `tl` and that you want to make some transformations:

- Transform the `str` "id" field to a unique `int` identifier
- Multiply each "num" by 2

First create the FMTL object:

```python
from fmtl import FMTL

tl = [("id0",1,44),("id0",5,75),("id1",3,44)] #raw tuple list
fmtl = FMTL(tl,{0:"id",1:"type",2:"num"}) #create the FMTL

```
Then you can easily add functional mappings to fields with the `set_mapping(...)` method:

```python
#Multiply all "num" values by 2
fmtl.set_mapping("num",lambda x:x*2)
```

You can provide dictionnaries as mapping an the `__get_item__()` function will be automatically used.
The `get_field_dict(...)` method can be used to get such mapping. 
```python
map = fmtl.get_field_dict("id") # Creates mapping on id field (returns dict())
fmtl.set_mapping("id", map)  #sets it
```
Mapping is done as iteration time in the object's `__get_item__()` method.

```python
list(fmtl) ==> [(0, 1, 44), (0, 5, 75), (1, 3, 44)] 
list(fmtl.tuplelist) =>[('id0', 1, 44), ('id0', 5, 75), ('id1', 3, 44)]
```
You can prebuild it explicitely.
```python
#persist mapping explicitely.
builded = fmtl.prebuild()
list(builded) => [(0, 1, 44), (0, 5, 75), (1, 3, 44)] 
list(builded.tuplelist) => [(0, 1, 44), (0, 5, 75), (1, 3, 44)] 
```
