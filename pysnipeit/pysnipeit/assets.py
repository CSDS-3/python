

class Assets(object):
    def __init__(self, apibase):
        self.apibase = apibase
        self.base_uri = '/api/v1/hardware'
    
    def list(self, **kwargs):
        uri = self.base_uri        
        return self.apibase._list(uri, **kwargs)
    
    def details(self, id ):
        uri = f'{self.base_uri}/{id}'
        return self.apibase.invoke_api(uri)
    
    def update(self, data):
        uri = self.base_uri
        return self.apibase._update(uri, data=data)
    
    def delete(self, id):
        uri = f'{self.base_uri}/{id}'
        return self.apibase.invoke_api(uri, method='delete')
    
    def get_by_tag(self, tag):
        uri = f'{self.base_uri}/bytag/{tag}'
        return self.apibase.invoke_api(uri)
    
    def get_by_serial(self, serial_number):
        uri = f'{self.base_uri}/byserial/{serial_number}'
        return self.apibase.invoke_api(uri)
    
    def restore(self, id):
        uri = f'{self.base_uri}/{id}'
        return self.apibase.invoke_api(uri, method='post')




