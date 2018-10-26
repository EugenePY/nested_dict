# nested_dict
Deep Nested dict that easily updated value, easily get value, and picklble.


```python
from nested_dict import NestedDict
import pickle as pkl

nested_dict = NestedDict()
nested_dict.update_list_key(["2", "3", "4"], 1)
>>>  {'2': {'3': {'4': 1}}}
nested_dict.update_list_key(["2", "3"], 1)
>>>  {'2': {'3': 1}}
nested_dict.update_list_key(["2"], 1)
>>> {'2': 1}
nested_dict.update_list_key(["2", "3", "4"], 1)
m.update_list_key(["2", "3", "5"], 1)
m.update_list_key(["2", "5"], 1)
for k, v in nested_dict.iter_flatten_nested_item():
  print(k, v)
>>> ('2', '3', '4') 1
    ('2', '3', '5') 1
    ('2', '5') 1

with open("./test.pkl", "wb") as f:
  loaded_nested_dict = pkl.load(f)
    
```
