import tkinter as tk
import requests
import json

root = tk.Tk()
root.title("Postman Clone")

# Input frame
input_frame = tk.Frame(root)
input_frame.pack()

# URL
url_label = tk.Label(root, text="Enter URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.config(width=100)
url_entry.pack()

# Header
header_label = tk.Label(root, text="Header:")
header_label.pack()

header_text = tk.Text(root)
header_text.config(height=10)
header_text.pack()

# Request Body
request_body_label = tk.Label(root, text="Request Body:")
request_body_label.pack()

request_body_text = tk.Text(root)
request_body_text.config(height=10)
request_body_text.pack()


# Helper functions
def jsonify_response(response):
    json_data = json.loads(response.text)
    json_str = json.dumps(json_data, indent=4)
    return json_str


# API request functions
def get_request():
    url = url_entry.get()
    response = requests.get(url)
    display_response(response)


def post_request():
    url = url_entry.get()
    request_body = request_body_text.get("1.0", tk.END)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=request_body, headers=headers)
    display_response(response)


def put_request():
    url = url_entry.get()
    request_body = request_body_text.get("1.0", tk.END)
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, data=request_body, headers=headers)
    display_response(response)


def delete_request():
    url = url_entry.get()
    response = requests.delete(url)
    display_response(response)


# Display response
def display_response(response):
    json_str = jsonify_response(response)
    response_text.delete("1.0", tk.END)
    response_text.insert(tk.END, json_str)
    status_code_label.config(text=f"Status Code: {response.status_code} {response.reason}")

# Buttons
button_frame = tk.Frame(root)
button_frame.pack()

get_button = tk.Button(button_frame, text="GET", command=get_request)
post_button = tk.Button(button_frame, text="POST", command=post_request)
put_button = tk.Button(button_frame, text="PUT", command=put_request)
delete_button = tk.Button(button_frame, text="DELETE", command=delete_request)

get_button.grid(row=0, column=0)
post_button.grid(row=0, column=1)
put_button.grid(row=0, column=2)
delete_button.grid(row=0, column=3)

# Output frame
output_frame = tk.Frame(root)
output_frame.pack()

response_label = tk.Label(output_frame, text="Response:")
response_label.pack()

status_code_label = tk.Label(output_frame, text="Status Code:")
status_code_label.pack()

response_text = tk.Text(output_frame)
response_text.config(height=10)
response_text.pack(fill="both", expand=True)

root.mainloop()