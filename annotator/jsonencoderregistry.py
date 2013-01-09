import json 

'''
'''

class JSONEncoderRegistry (json.JSONEncoder):
    serializers = {}
    
    @classmethod
    def register_json_serializer(cls, obj, method):
        cls.serializers[obj] = method
                
    @classmethod
    def deregiser_serializer(cls, obj):
        if obj in cls.serializers:
            del cls.serializers[obj]
        
    def default(self, obj):
        for cls, method in self.serializers.iteritems() :
            if isinstance(obj, cls) :
                return method(obj)
            
        return super(JSONEncoderRegistry, self).default(obj)
