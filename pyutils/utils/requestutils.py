import requests
import time
import json


def request_get(url, query_params=None, bearer_token=None, is_response_json=True, raise_for_status=True, headers={}):
    """
    Send a GET request to the specified URL with optional query parameters and bearer token authorization.

    :param url: The URL to send the GET request to
    :param query_params: A dictionary of query parameters to include in the request
    :param bearer_token: A bearer token for authorization (optional)
    :return: The JSON response from the server
    """
    if not headers:
        headers = {}
    headers["Content-Type"] = "application/json"

    if bearer_token:
        headers["Authorization"] = "Bearer " + bearer_token

    start_time = time.time()  # Record the start time

    try:
        response = requests.get(url, headers=headers, params=query_params)
        if raise_for_status:
            response.raise_for_status()  # Check if the request was successful
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    finally:
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the total time taken
        print(f"Total time taken for the request: {elapsed_time:.2f} seconds")

    if is_response_json:
        try:
            response_data = response.json()  # Parse JSON response directly
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            return None
    else:
        response_data = {
            "status_code": response.status_code,
            "response": response.text
        }

    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response_data}")

    return response_data


def request_put(url, data=None, query_params=None, bearer_token=None, expect_json_response=True):
    """
    Send a PUT request to the specified URL with optional data, query parameters, and bearer token authorization.

    :param url: The URL to send the PUT request to
    :param data: A dictionary of data to include in the request
    :param query_params: A dictionary of query parameters to include in the request
    :param bearer_token: A bearer token for authorization (optional)
    :return: The JSON response from the server
    """
    headers = {
        "Content-Type": "application/json"
    }
    if bearer_token:
        headers["Authorization"] = "Bearer " + bearer_token

    start_time = time.time()  # Record the start time

    try:
        response = requests.put(url, headers=headers, json=data, params=query_params)
        response.raise_for_status()  # Check if the request was successful
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
    finally:
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the total time taken
        print(f"Total time taken for the request: {elapsed_time:.2f} seconds")

    print(f"Response status code: {response.status_code}")

    if not expect_json_response:
        return None

    try:
        response_data = response.json()  # Parse JSON response directly
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None

    print(f"Response content: {response_data}")

    return response_data


def request_post(url, payload, bearer_token=None, api_token=None):
    # Set the content type header to JSON
    headers = {
        "Content-Type": "application/json"
    }
    if bearer_token:
        headers["Authorization"] = "Bearer " + bearer_token

    if api_token:
      for api_key in api_token:
            headers[api_key] = api_token[api_key]

    # Send the POST request with the JSON payload in the request body
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    # Print the response status code and content
    print("Response status code:", response.status_code)
    print("Response content:", response.content)

    response_data = response.content
    response_data = response_data.decode("utf-8")

    response_json = json.loads(response_data)

    return response_json


def request_patch(url, payload=None, bearer_token=None):
    # Set the content type header to JSON
    headers = {
        "Content-Type": "application/json"
    }
    if bearer_token:
        headers["Authorization"] = "Bearer " + bearer_token

    requests_args = {
        "url": url,
        "headers": headers,
    }

    if payload:
        requests_args["data"] = json.dumps(payload)
        print("request body:")
        print(json.dumps(payload, indent=4))

    # Send the POST request with the JSON payload in the request body
    response = requests.patch(**requests_args)

    # Print the response status code and content
    print("Response status code:", response.status_code)
    print("Response content:", response.content)

    response_data = response.content

    if response_data:
        response_data = response_data.decode("utf-8")
        response_json = json.loads(response_data)
    else:
        response_json = None

    return response_json
