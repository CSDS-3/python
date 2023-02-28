

class Fields(object):
    def __init__(self, apibase):
        self.apibase = apibase
        self.base_uri = '/api/v1/fields'
    
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

    def associate(self, field_id, fieldset_id):
        uri = f'{self.base_uri}/{field_id}/associate'
        data = {'fieldset_id': fieldset_id}
        return self.apibase.invoke_api(uri, method='post', data=data)
    
    def unassociate(self, field_id, fieldset_id):
        uri = f'{self.base_uri}/{field_id}/associate'
        data = {'fieldset_id': fieldset_id}
        return self.apibase.invoke_api(uri, method='post', data=data)
