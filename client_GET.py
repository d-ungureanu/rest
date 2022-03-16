import requests
import pprint

if __name__ == "__main__":
    response = requests.get("https://www.bbc.co.uk")
    print(type(response))
    print(response)
    print(response.status_code)
    pprint.pprint(response.headers)
    headers_data = pprint.pformat(response.headers, indent=4)
    # my_printer = pprint.PrettyPrinter()
    pprint.pprint(headers_data)
