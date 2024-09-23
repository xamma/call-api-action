from api_caller import ApiCaller
import os

# os.environ["REQUEST_BODY"] = '{"data": "test", "name": "mxa", "age": 31, "access": ["allow", "deny"]}'
# os.environ["HEADERS"] = '{"Authorization": "Bearer ej231974zoasdnoashd789235r981hrijworhja8z90ur2q0hroq", "Content-Type": "application/json"}'
os.environ["QUERY_PARAMS"] = '{"limit": "10", "offset": "0"}'
os.environ["HTTP_METHOD"] = "GET"
os.environ["API_URL"] = "https://pokeapi.co/api/v2/pokemon"

api_caller = ApiCaller()
# result = api_caller.make_api_request()
print(api_caller.response_data)

# print(api_caller.request_body["data"])
# print(api_caller.headers)
# print(api_caller.settings.http_method)

# test_data_str=os.getenv("REQUEST_BODY")
# test_data = json.loads(test_data_str)
# print(test_data["access"][1])

# query_params = {
#     "sort": "ASC",
#     "page": "2"
# }

# if query_params:
#     print("true")
# else:
#     print("false")