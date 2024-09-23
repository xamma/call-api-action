import requests
from models import AppSettings
import json

"""
This class will do a customizable RestAPI call.  
The response needs to be in JSON format.  
"""

class ApiCaller():
    def __init__(self) -> None:
        self.settings = AppSettings()
        self.response_data = None
        self.request_body = self.parse_reqbody_to_json()
        self.headers = self.parse_headers_to_json()
        self.query_params = self.parse_query_to_json()
        self.make_api_request()

    def parse_reqbody_to_json(self):
        request_body_str = self.settings.request_body
        if request_body_str:
            return json.loads(request_body_str)
        return {}
    
    def parse_headers_to_json(self):
        headers_str = self.settings.headers
        if headers_str:
            return json.loads(headers_str)
        return {}
    
    def parse_query_to_json(self):
        query_str = self.settings.query_params
        if query_str:
            return json.loads(query_str)
        return {}

    def make_api_request(self):
        if self.settings.http_method == "GET":
            try:
                r = requests.get(self.settings.api_url, headers=self.headers, params=self.query_params)
                self.response_data = r.json()
                return self.response_data
            except Exception as e:
                print(f"error: Error getting data from API: {e}")
        elif self.settings.http_method == "POST":
            try:
                r = requests.post(self.settings.api_url, data=self.request_body, headers=self.headers, params=self.query_params)
                self.response_data = r.json()
                return self.response_data
            except Exception as e:
                print(f"error: Error posting data to API: {e}")
        elif self.settings.http_method == "PUT":
            try:
                r = requests.put(self.settings.api_url, data=self.request_body, headers=self.headers, params=self.query_params)
                return self.response_data
            except Exception as e:
                print(f"error: Error putting data to API: {e}")
        elif self.settings.http_method == "PATCH":
            try:
                r = requests.patch(self.settings.api_url, data=self.request_body, headers=self.headers, params=self.query_params)
                return self.response_data
            except Exception as e:
                print(f"error: Error patching data to API: {e}")
        elif self.settings.http_method == "DELETE":
            try:
                r = requests.delete(self.settings.api_url, data=self.request_body, headers=self.headers, params=self.query_params)
                return self.response_data
            except Exception as e:
                print(f"error: Error deleting data from API: {e}")
        else:
            print("error: Kaputt...")
