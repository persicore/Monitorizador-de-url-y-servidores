import asyncio
import requests


websites = [
    'https://www.panama-jack.com',
    'https://www2.panama-jack.com',
    'https://api2.panama-jack.com',
    'https://api3.panama-jack.com',
    'https://api.panama-jack.com',
    'https://test.panama-jack.com',
    'https://vendor.panamajack.es',
    'https://vendortest.panamajack.es',
    #'https://test2.panama-jack.com',
]

async def check_website_status(url):
    
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.exceptions.RequestException as error:
        print(f"Error chequeando la siguiente URL: {url}: {error}")
        return None

async def monitor_websites():
    
    while True:
        tasks = [check_website_status(url) for url in websites]
        results = await asyncio.gather(*tasks)
        for url, status_code in zip(websites, results):
            if status_code is not None:
                print(f"{url} - Status: {status_code}")
        await asyncio.sleep(60) 

if __name__ == '__main__':
    asyncio.run(monitor_websites())