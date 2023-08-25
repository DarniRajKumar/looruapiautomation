# import requests
# from notes_api_tests import *

# #API Test for error handling of creating new Looru Note
# def send_post_request(url, headers, payload):
#     # try:
#         response = requests.post(url, headers=headers, json=payload)
#         response.raise_for_status()  # Raise HTTPError if response status is not 2xx
#         return response

# def test_post_main():
#     try:
#         response = send_post_request(url, headers, post_payload)
#         print("Response:", response.status_code, response.json())
#     except requests.exceptions.HTTPError as e:
#         print("HTTP Error:", str(e))
#     except requests.exceptions.RequestException as e:
#         print("Request error:", str(e))


# #API Test for error handling of updating new Looru Note


# base_url = "https://b2btesterscom.s1.my.looru.ai/api"
# note_id = "195fea3c-7a25-4e3d-be6f-4d511926697b"
# url = f"{base_url}/notes/{note_id}"

# def send_put_request(url, headers, payload):
#     # try:
#         response = requests.post(url, headers=headers, json=payload)
#         response.raise_for_status()  # Raise HTTPError if response status is not 2xx
#         return response

# def test_put_main():
#     try:
#         response = send_put_request(url, headers, put_payload)
#         print("Response:", response.status_code, response.json())
#     except requests.exceptions.HTTPError as e:
#         print("HTTP Error:", str(e))
#     except requests.exceptions.RequestException as e:
#         print("Request error:", str(e))


# #API Test for error handling of getting specific  Note

# # Define the URL and note_id
# note_id = "195fea3c-7a25-4e3d-be6f-4d511926697b"
# url = f"{base_url}/notes/{note_id}"
# api_params = {"type": "luru"}

# # Send the GET request
# response = requests.get(url,headers=headers)
# def test_get_notes_errorvalidation():
# # Check the response status code
#  if response.status_code == 200:
#     print("Request was successful!")
#     print("Response:", response.json())
#  elif response.status_code == 404:
#     print(f"Note with ID '{note_id}' was not found.")
#     print("Response:", response.text)
#  else:
#     print(f"An error occurred. Status Code: {response.status_code}")
#     print("Response:", response.text)


# if __name__ == "__main__":
#     test_get_notes_errorvalidation()
