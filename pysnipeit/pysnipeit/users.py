

class Users(object):
    def __init__(self, apibase):
        self.apibase = apibase
        self.base_uri = '/api/v1/users'
    
    def list(self, limit=None, **kwargs):
        uri = self.base_uri        
        return self.apibase._list(uri, **kwargs)
    
    def details(self, id ):
        uri = f'{self.base_uri}/{id}'
        return self.apibase.invoke_api(uri)
    
    def update(self, data):
        uri = self.base_uri
        self.apibase._update(uri, data=data)


