# FMTL: a Field-Mappable Tuple List

## Requirements:

- TQDM

## Install:
via pip: `pip install -e git+https://github.com/cedias/FMTL.git`

## Usage

Let's say you have a tuple list `tl`:
```python
from fmtl import FMTL

tl = [("id0",1,44),("id0",5,75),("id1",3,44)] #raw tuple list
fmtl = FMTL(tl,{0:"id",1:"type",2:"num"}) #create the FMTL

```
You can directly create a dictionnary of all your field's values and use it as a map.
```python
map = fmtl.get_field_dict("id") #Creates mapping on id field
fmtl.set_mapping("id",)  sets it
```
Mapping is done as iteration time
```python
list(fmtl) ==> [(0, 1, 44), (0, 5, 75), (1, 3, 44)] 
list(fmtl.tuplelist) =>[('id0', 1, 44), ('id0', 5, 75), ('id1', 3, 44)]
```
Unless you decide it should be persistant.
```python
#persist mapping explicitely.
builded = fmtl.prebuild()
list(builded) => [(0, 1, 44), (0, 5, 75), (1, 3, 44)] 
list(builded.tuplelist) => [(0, 1, 44), (0, 5, 75), (1, 3, 44)] 
```
