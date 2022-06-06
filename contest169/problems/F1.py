import requests
from requests_html import HTMLSession

sum = 0
for page in range(1, 21):
    print(page)
    url = f'http://cpython.uz/users/?page={page}'

    try:
        print(f'Page: {page}')
        session = HTMLSession()
        response = session.get(url)
        for xd in response.html.find('#rating tbody tr td.text-center span'):
            print(xd.text)
            sum += int(xd.text)
    except requests.exceptions.RequestException as e:
        print(e)

print(sum)
