
class StatusLabels(object):
    def __init__(self, apibase):
        self.apibase = apibase
        self.base_uri = '/api/v1/statuslabels'
    
    def list(self, iter=False, **kwargs):
        uri = self.base_uri        
        return self.apibase._list(uri, **kwargs)
    
    def update(self, data):
        uri = self.base_uri
        return self.apibase.invoke_api(uri, method='post', data=data)
    
    def delete(self, id):
        uri = f'{self.base_uri}/{id}'
        return self.apibase.invoke_api(uri, method='delete')