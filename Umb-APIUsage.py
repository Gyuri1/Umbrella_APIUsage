#!/usr/bin/env python
"""
UMBRULLA APIUSAGE test
more info:
https://developer.cisco.com/docs/cloud-security/api-reference-reports-api-usage-overview/
"""
import requests
import json
from requests.auth import HTTPBasicAuth


umb_url= "api.umbrella.com/auth/v2/token"
umb_key= "XXX"
umb_sec= "YYY"


from_date="2024-10-10" 
to_date="2024-10-11"

# URL to obtain the access token
TOKEN_URL = 'https://api.umbrella.com/auth/v2/token'

def get_access_token(client_id, client_secret):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'client_credentials'
    }

    try:
        response = requests.post(TOKEN_URL, headers=headers, data=data, auth=HTTPBasicAuth(client_id, client_secret))
        response.raise_for_status()  # Raise an HTTPError for bad responses
        token_data = response.json()
        return token_data['access_token']
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while obtaining the access token: {e}")
        return None



def get_dns_activity(access_token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = "https://api.umbrella.com/reports/v2/activity/dns?to="+to_date +"&from="+from_date+"&limit=10"
    response = requests.request('GET', url, headers=headers)
    print(response.text.encode('utf8'))

def get_api_requests(access_token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = "https://api.umbrella.com/reports/v2/apiUsage/requests?to="+to_date +"&from="+from_date
    response = requests.request('GET', url, headers=headers)
    return response
    

def get_api_responses(access_token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = "https://api.umbrella.com/reports/v2/apiUsage/responses?to="+to_date +"&from="+from_date
    response = requests.request('GET', url, headers=headers)
    return response


def get_api_keys(access_token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = "https://api.umbrella.com/reports/v2/apiUsage/keys?to="+to_date +"&from="+from_date
    response = requests.request('GET', url, headers=headers)
    return response



def get_api_summary(access_token, from_date, to_date):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    url = "https://api.umbrella.com/reports/v2/apiUsage/summary?to="+to_date +"&from="+from_date
    response = requests.request('GET', url, headers=headers)
    return response



if __name__ == "__main__":
    access_token = get_access_token(umb_key, umb_sec)
    if access_token:
        print(f"Access Token received.")
    """    
    response = get_dns_activity(access_token, from_date="-1days", to_date= "now")
    if response:
        print(response.text.encode('utf8'))
	"""
    response = get_api_requests(access_token, from_date=from_date, to_date=to_date)
    if response:
	    print("Requests:",json.dumps(response.json(), indent=4)) 
    
    response = get_api_responses(access_token, from_date=from_date, to_date=to_date)
    if response:
    	print("Responses:",json.dumps(response.json(), indent=4))

    response = get_api_keys(access_token, from_date=from_date, to_date=to_date)
    if response:
    	print("Responses:",json.dumps(response.json(), indent=4))	

    response = get_api_summary(access_token, from_date=from_date, to_date=to_date)
    if response:
        print("Summary:",json.dumps(response.json(), indent=4)) 	
