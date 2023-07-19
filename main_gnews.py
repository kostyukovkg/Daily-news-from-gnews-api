import requests
from datetime import datetime

# Getting the current date and time
dt = datetime.now()

# convert datetime to string a required format for email subject
str_date_subject = dt.strftime("%d %B, %Y")

# get a day before for API request
#convert dt to tuple
tt = dt.timetuple() # time.struct_time(tm_year=2023, tm_mon=5, tm_mday=17,
                    # tm_hour=10, tm_min=33, tm_sec=53, tm_wday=2, tm_yday=137,
                    # tm_isdst=-1)
#insert tuple into string data format
str_date_url = dt.strftime(f"%Y-%m-%{tt[2]-1}")

# working with API
topics = 'china'
sources = ("Investing.com", "The Guardian", 'Yahoo News', 'Reuters',
           "The New York Times", 'CNN', 'Business Insider',
           'The Washington Post', 'The Economist', 'Bloomberg', "Financial Times")
api_key = '63e48a77bd1c95fdd8d33aae96c8161a'
url = 'https://gnews.io/api/v4/search?' \
      f'q={topics}&' \
      'in=title,description&' \
      'sortby=relevance&' \
      'lang=en&' \
      f'from={str_date_url}T04:00:00Z&' \
      f'apikey={api_key}'


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()  # dict type

body = f"Subject: CNY news {str_date_subject} " + '\n'
i = 1
for article in content['articles']:
    if article['source']['name'] in sources:
        body = body + f'{str(i)}. ' + \
               article["description"] + '\n' + \
               article['url'] + \
               2 * '\n'
        i += 1

print(body)
body = body.encode('utf-8')

# send multiple emails based on the list of emails
#receivers = ()
#for receiver in receivers:
#    send_multiple_email(message=body, receiver=receiver)
