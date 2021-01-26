# from selenium.common.exceptions import InvalidArgumentException
from selenium import webdriver
from typing import List
import urllib, sys                                                      

def get_links(url: str):
    """Find all links on page at the given url.
       Returns:
          a list of all unique hyperlinks on the page,
          without page fragments or query parameters.
    """
    all_links = []
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        url = driver.find_elements_by_css_selector('a')
        for each_url in url:
            finalise_url =  each_url.get_attribute('href')
            if '#' in finalise_url :
                pass
            elif '?' in finalise_url:
                pass
            else:
                all_links.append(finalise_url)
    except InvalidArgumentException:
        print('Invalid argument')
        sys.exit(1)

    driver.quit()
    return all_links

def is_valid_url(url: str):
    """ Check that if a url is reachable (valid) or not .
    
        Returns:
            True if the url is ok, False otherwise.
    
    """
    try : 
        connection = urllib.request.urlopen(url)
        if connection.status == 200:
            return True
    except:
        return False

def invalid_urls(urllist: List):
    """ Validate the urls in urllist and return a new list containing the invalid or unreachable urls.
    
        Returns:
            a list of all bad link 
    """

    invalid_link = []
    for each_link in urllist:
        print(each_link)
        if is_valid_url(each_link):
            pass
        else:
            invalid_link.append(each_link)
    print()
    if len(invalid_link) == 0:
        print("No Bad Link")
    else:
        print("Bad Links: ")
        for link in invalid_link:
            print(link)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage:  python3 link_scan.py url\n")
        print("Test all hyperlinks on the given url.")
    else:
        print(sys.argv[1])
        print()
        link = get_links(sys.argv[1])
        invalid_urls(link)