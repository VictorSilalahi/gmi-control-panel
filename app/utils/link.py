import requests

def check_link(link):
    try:
        resp = requests.get(link, timeout=5)
    # If the connection succeeds, you can check the status code here
        if resp.status_code == 200:
            return {"status": "good"}
        else:
            print(f"Server returned status code: {response.status_code}")

    except requests.exceptions.ConnectionError as e:
        # This block catches the 'Connection refused' error
        print(f"Error: Connection refused/network problem pada link: ", link)
        # You can access the underlying system error number (errno) if needed
        # print(e.args[0].reason.errno) 
        return {"status": "bad"}
        
    except requests.exceptions.Timeout as e:
        # Handle cases where the server is up but takes too long to respond
        print("Error: The request timed out")
        return {"status": "bad"}
        
    except requests.exceptions.RequestException as e:
        # This is a general exception that catches all of the above and more
        print(f"An unexpected error occurred: {e}")
        return {"status": "bad"}