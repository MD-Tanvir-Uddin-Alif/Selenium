from seleniumwire import webdriver
import time

def main():
    # simple options - adjust if needed
    driver = webdriver.Chrome()  # ensure chromedriver is on PATH and matches Chrome
    driver.get('https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_3_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=3d96f199-f32b-4519-8033-f6b5b959272e')

    time.sleep(5)  # wait for network requests to fire

    for req in driver.requests:
        if req.response:
            print(req.method, req.url, req.response.status_code)
    driver.quit()

if __name__ == "__main__":
    main()
