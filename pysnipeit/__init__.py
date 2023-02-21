import logging
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import os
from .assets import Assets
from .categories import Categories
from .status_labels import StatusLabels


class SnipeIT(object):
    def __init__(self, base_url = None, token = None, 
        retries = 5 , backoff_factor=0.1, status_forcelist=(500,502,503,504)):

        self.base_url = base_url if base_url else os.getenv('SNIPE_URL')
        self._headers = self._build_headers(token=token)
        self._retries = retries
        self._backoff_factor = backoff_factor
        self._status_forcelist = status_forcelist

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
        return response.json() if format else response

    def _iter_api(self, uri, params=None, data=None):
        #TODO
        pass

    def _list(self, uri, limit=None, order='asc', offset=None):
        params = {'limit':limit,
            'order':order,
            'offset':offset}
        return self._iter_api(uri, params=params)


    @property
    def assets(self):
        return Assets(self)
    
    @property
    def categories(self):
        return Categories(self)
    
    @property
    def status_labels(self):
        return StatusLabels(self)