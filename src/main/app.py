from api_caller import ApiCaller
import os
import json

"""
Runner file for docker.
Also converts dictionary to JSON string.  
"""

if __name__ == "__main__":
    api_caller = ApiCaller()

    # Debuggubg
    # print(f"Original response_data: {api_caller.response_data} (Type: {type(api_caller.response_data)})")

    # check if response is a dict before dumping
    if isinstance(api_caller.response_data, str):
        # convert  string to dict
        try:
            response_data_dict = json.loads(api_caller.response_data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            response_data_dict = {}
    elif isinstance(api_caller.response_data, dict):
        response_data_dict = api_caller.response_data
    else:
        print("Unexpected type for response_data. Must be str or dict.")
        response_data_dict = {}

    # py dict to JSON string
    response_data_json = json.dumps(response_data_dict)

    # debugg
    # print(f"Response Data JSON: {response_data_json}")

    # Write to GITHUB_OUTPUT, and escape double quotes for Shell
    escaped_json = response_data_json.replace('"', '\\"')
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"response_data={escaped_json}\n")

    print("Response data written to GITHUB_OUTPUT.")
