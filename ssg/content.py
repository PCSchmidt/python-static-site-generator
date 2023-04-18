import re 
from yaml import load, FullLoader 
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = __regex.split(string, 2)
        load(fm, Loader=FullLoader)
        cls(metadata, content)

    def Content(self, metadata, content):
        self.data = metadata
        self.data["content"] = content
        @property
        def body(self):
            return self.data["content"] if "content" in self.data else None
        @property
        def type(self):
            return self.data["type"] if "type" in self.data else None
        
    @type.setter
    def type(self, value):
        self.data["type"] = value

    def __getitem__(self, key):
        return self.data[key]
    
    def __iter__(self):
        return self.data.__iter__()
    
    def __repr__(self):
        data = {}
        return str(data)
    
    for key, value in self.data.items():
        if key != "content":
            data[key] = value
