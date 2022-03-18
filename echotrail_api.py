import os
import requests
import sys

ECHOTRAIL_API_URL = 'https://api.echotrail.io/v1/private/insights/'

if len(sys.argv) < 2:
    print('Please provide a filename or hash argument')
    sys.exit(1)
else:
    filename = sys.argv[1]

if len(sys.argv) == 3:
    key = sys.argv[2]
else:
    key = os.environ.get('ECHOTRAIL_API_KEY')

if not key:
    print('\nPlease store your API key in the ECHOTRAIL_API_KEY environment variable')
    print('e.g. export ECHOTRAIL_API_KEY=<your_api_key>\n')
    print('- or -\n')
    print('Provide your key as the second argument\n')
    print('Free API keys are available by registering for a free account at https://www.echotrail.io\n')
    sys.exit(1)

headers = {
    'X-Api-key': key,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
    }
r = requests.get(ECHOTRAIL_API_URL + filename, headers=headers)

if r.status_code != 200:
    print('Error contacting API', r.status_code)
else:
    print(r.text)
