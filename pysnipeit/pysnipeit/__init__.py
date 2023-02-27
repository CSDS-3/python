import logging
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import os
from .assets import Assets
from .categories import Categories
from .status_labels import StatusLabels
from .users import Users
from .models import Models
from .manufacturers import Manufacturers
from .fieldsets import Fieldsets
from .fields import Fields

class SnipeIT(object):
    def __init__(self, base_url = None, token = None, 
        retries = 5 , backoff_factor=0.1, status_forcelist=(500,502,503,504)):

        self.base_url = base_url if base_url else os.getenv('SNIPE_URL')
        self._headers = self._build_headers(token=token)
        self._retries = retries
        self._backoff_factor = backoff_factor
        self._status_forcelist = status_forcelist
        self.log = logging.getLogger(__name__)
        self.log.addHandler(logging.NullHandler())
        self._build_session()

    def _build_headers(self, token):
        tok = token if token else os.getenv('SNIPE_TOK')
        headers = {'accept':'application/json', 
            'Authorization': f'Bearer {tok}'}
        return headers

    def _build_session(self):
        'Handles retries/backoffs, etc'
        self._session = requests.Session()
        retry = Retry(
            total = self._retries,
            read = self._retries,
            connect = self._retries,
            backoff_factor = self._backoff_factor,
            status_forcelist = self._status_forcelist

        )
        adapter = HTTPAdapter(max_retries=retry)
        self._session.mount('htts://', adapter)
        self._session.verify = False

    def invoke_api(self, uri, method='get', params=None, data=None, format=True, **kwargs):
        url = self.base_url + uri
        if api_call := getattr(self._session, method):
            response = api_call(url, headers=self._headers, params=params, data=data, **kwargs)
            response.raise_for_status()
        else:
            raise KeyError(f'Wrong Method specified {url} {method}')
        return self._response_handler(response.json()) if format else response

    def _iter_api(self, uri, params=None, data=None):
        while True:
            response = self.invoke_api(uri=uri, params=params, data=data)
            if results := response.get('rows'):
                params['offset'] += len(results)
                for item in results:
                    yield item
            else:
                break


    def _list(self, uri, limit=None, order='asc', offset=0, iter=False, **kwargs):
        params = {'limit':limit,
            'order':order,
            'offset':offset}
        for k,v in kwargs.items():
            params.update({k:v})
        if not iter:
            return [i for i in self._iter_api(uri, params=params)]
        return self._iter_api(uri, params=params)

    def _response_handler(self, response):
        if response.get('rows'):
            # paging
            return response
        elif response.get('status'):
            if response['status'] != 'success':
                self.log.error(f'Failed Update {response["status"]=} {response["messages"]=}')
                raise Exception
            else: 
                return response['payload']
        return response

    @property
    def assets(self):
        return Assets(self)
    
    @property
    def categories(self):
        return Categories(self)
    
    @property
    def status_labels(self):
        return StatusLabels(self)
    
    @property
    def users(self):
        return Users(self)

    @property
    def manufacturers(self):
        return Manufacturers(self)
    
    @property
    def models(self):
        return Models(self)
    
    @property
    def fieldsets(self):
        return Fieldsets(self)
    
    @property
    def fields(self):
        return Fields(self)