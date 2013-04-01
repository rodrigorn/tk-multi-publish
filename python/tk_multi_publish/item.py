"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------
"""

class Item(object):
    """
    Encapsulate an item returned by the scan hook
    """
    def __init__(self, fields={}):
        self._raw_fields = fields
    
    @property
    def raw_fields(self):
        return self._raw_fields
        
    @property
    def name(self):
        return self._raw_fields["name"]
    
    @property
    def scene_item_type(self):
        return self._raw_fields["type"]

    @property
    def description(self):
        return self._raw_fields.get("description")
    
    def validate(self):
        required_keys = ["name", "type"]
        for rk in required_keys:
            if rk not in self._raw_fields.keys():
                raise Exception("Item does not contain required field '%s'" % rk)
    