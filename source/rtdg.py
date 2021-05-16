# import Faker
from faker import Faker

# initializing a pseudo-random number generator
Faker.seed(20)

fake = Faker()

# dictionaries containing faker functions
address = {'address': fake.address,'city':fake.city,'country':fake.country,'postcode':fake.postcode}
creditcard = {'card_no':fake.credit_card_number,'expire_date':fake.credit_card_expire,'security code':fake.credit_card_security_code}
automotive = {'license_plate':fake.license_plate}
bank = {'country':fake.bank_country,'swift11':fake.swift11,'iban':fake.iban}
date_time={'am_pm':fake.am_pm,'date':fake.date,'month':fake.month}
file = {'file_extension':fake.file_extension,'file_name':fake.file_name,'file_path':fake.file_path}
geo = {'coordinate':fake.coordinate,'latitude':fake.latitude,'location_on_land':fake.location_on_land,'longitude':fake.longitude}
color = {'color_name':fake.color_name,'hex_color':fake.hex_color,'rgb_css_color':fake.rgb_css_color}
internet={'ascii_email':fake.ascii_email,'ascii_free_email':fake.ascii_free_email,'ascii_safe_email':fake.ascii_safe_email,'company_email':fake.company_email,'dga':fake.dga,'domain_name':fake.domain_name}
isbn={'isbn10':fake.isbn10,'isbn13':fake.isbn13}
job={'job':fake.job}
lorem={'paragraph':fake.paragraph,'paragraphs':fake.paragraphs,'sentence':fake.sentence,'sentences':fake.sentences,'text':fake.text,'texts':fake.texts,'word':fake.word,'words':fake.words}
misc={'binary':fake.binary,'boolean':fake.boolean,'csv':fake.csv,'dsv':fake.dsv,'fixed_width':fake.fixed_width,'json':fake.json,'md5':fake.md5,'null_boolean':fake.null_boolean,'password':fake.password}
person={'first_name':fake.first_name,'first_name_female':fake.first_name_female,'first_name_male':fake.first_name_male,'language_name':fake.language_name,'last_name':fake.last_name,'name':fake.name}
phone_number={'phone_number':fake.phone_number,'msisdn':fake.msisdn}
profile={'simple_profile':fake.simple_profile}
python1={'pybool':fake.pybool,'pydecimal':fake.pydecimal,'pydict':fake.pydict,'pyint':fake.pyint,'pyiterable':fake.pyiterable}
ssn={'ssn':fake.ssn}
user_agent={'chrome':fake.chrome,'android_platform_token':fake.android_platform_token,'firefox':fake.firefox,'linux_processor':fake.linux_processor}


# dictionary containing all  the groups
all_func = {'address':address,'creditcard':creditcard,'automotive':automotive,'bank':bank,'date_time':date_time,'file':file,'geo':geo,'color':color,'internet':internet,'isbn':isbn,'job':job,'lorem':lorem,'misc':misc,'phone_number':phone_number,'person':person,'python':python1,'ssn':ssn,'profile':profile,'user_agent':user_agent}



