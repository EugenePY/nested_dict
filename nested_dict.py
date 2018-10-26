class NestedDict(dict):
    def __init__(self, *arg, **kwargs):
        super(NestedDict, self).__init__(*arg, **kwargs)
   
    def update_list_key(self, key, value):
        return NestedDict._update_list_key(self, key, value)
    
    def iter_flatten_nested_item(self):
        return NestedDict._flatten_nested_items(self)
    
    @staticmethod
    def _flatten_nested_items(dict_):
        keys = dict_.keys
        for key in keys():
            value = dict_[key]
            if isinstance(value, dict):
                for keykey, value in NestedDict._flatten_nested_items(value):
                    yield (key,) + keykey, value
            else:
                yield (key,), value
    
    @staticmethod
    def _update_list_key(nested_dict, key, value):
        if len(key) == 1:
            last_key = key.pop(0)
            nested_dict.update({last_key: value})
            return nested_dict
        else:
            k = key.pop(0)
            nested_dict.update(
                    {k: NestedDict._update_list_key(
                            nested_dict.get(k, {}) 
                            if isinstance(nested_dict.get(k, {}), dict) \
                                else {}, # if get value is not a dict thats means this is a one layer dict
                                key, value)}
                              )
            return nested_dict
