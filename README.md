# Umbrella_APIUsage

This Python script displays the Umbrella API Usage Endpoint responses.


## Installation:

1. **Download Files**: 
   Download all the files from this repository.

2. **Install Dependencies**: 
   Ensure you have the `requests` package installed. You can install it using pip:

   ```sh
   pip install requests
   ```

   Please update these variables in the script according to your Umbrella API:
   - umb_key = "XXX"    
   - umb_sec = "YYY"

   
##  Usage:  


   ```sh
   python3 Umb_APIUsage.py
   ```

For example:


   ```sh
  Access Token received.
  Requests: {
    "from": "2024-10-10",
    "to": "2024-10-11",
    "count": 6,
    "items": [
        {
            "userAgent": "Cisco XDR - Umbrella Integration",
            "count": 4,
            "requests": [
                {
                    "path": "/auth/v2/oauth2/token",
                    "verb": "POST",
                    "count": 4
                }
            ]
        },

    ...
   ```

More information:

https://developer.cisco.com/docs/cloud-security/api-reference-reports-api-usage-overview/

