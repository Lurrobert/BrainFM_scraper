import brainfm
import requests
from fake_useragent import UserAgent
from fake_headers import Headers
import warnings
warnings.filterwarnings("ignore")

headers = Headers(os="mac", headers=True).generate()
client = brainfm.Connection(user_agent=UserAgent().ie)
client.login("your email", "your password)

token = client.get_token(302)  # token for the station

for i in range(20):
    if i % 5 == 0:
        print(f'--{i}--')
    url = client.make_stream_url(token)
    r = requests.get(url, allow_redirects=True, verify=False, headers=headers)
    open(f'Piano{i}.mp3', 'wb').write(r.content)
