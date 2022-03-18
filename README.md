# EchoTrail API Examples

## Summary

The purpose of this script is to provide an example Python script to use for accessing the EchoTrail API. You can use it as a standalone commandline script or use the code to build an integration with your favorite SIEM or SOAR product.

## Usage

Create a virtualenv if needed and then run

`pip install -r requirements.txt`

To make a call to the API, run:

`python ./echotrail_api.py [filename or hash] [API Key]`

Alternatively, you can store your API key in an environment variable and run the script without the second argument.

`export ECHOTRAIL_API_KEY=<your_api_key>`

`python ./echotrail_api.py [filename or hash]`

You can get a free API Key by registering for a free account at [https://www.echotrail.io/register](https://www.echotrail.io/register)

## Examples

`python ./echotrail_api.py powershell.exe`

`python ./echotrail_api.py svchost.exe`

`python ./echotrail_api.py 09459f012f42eaed788f617c3c879d298077dca193b239b1172628a5e0c3ffaa`

## Pretty Print

To pretty print the JSON output, you can pipe the output to [json_pp](https://metacpan.org/dist/JSON-PP/view/bin/json_pp)

`python ./echotrail_api.py powershell.exe | json_pp`