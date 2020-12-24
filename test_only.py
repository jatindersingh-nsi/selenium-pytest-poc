"""
`params['project_url']` will be returned after deploying the application in docker container. So this will be
available in the params parameter in every function and class methods. For E2E testing, Chrome browser driver path is
available in `params['driver_path']`. See below, are examples to write test cases.

1. Method based
def test_add_to_cart(params):
    project_url = params['project_url']
    driver_path = params['driver_path']
    # ...
    # Your code goes here
    # ...


2. Class based
class Test:
    def test_add_to_cart(self, params):
        project_url = params['project_url']
        driver_path = params['driver_path']
        # ...
        # Your code goes here
        # ...


todo: Only headless option
todo: Create webapp class for browser driver
todo: need to check this on server
"""
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

HEADLESS = True


def test_get_article(params):
    """
    Test RESTful API endpoint to check Get post data
    """
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    except requests.ConnectionError:
        assert False
    assert response.status_code == 200


def test_github_login(params):
    """
    Test github login success
    """
    project_url = params['project_url']
    driver_path = params['driver_path']
    options = Options()
    options.headless = HEADLESS
    driver = webdriver.Chrome(driver_path, options=options)
    driver.get(project_url)
    driver.find_element_by_id('login_field').send_keys('Jatindersingh-nsi')
    driver.find_element_by_id('password').send_keys('jatinder@netsolutions')
    driver.find_element_by_name('commit').click()
    assert "Two-factor authentication" in driver.page_source


def test_add_to_cart(params):
    project_url = params['project_url']
    driver_path = params['driver_path']
    # ...
    # Your code goes here
    # ...
    assert True


def test_place_order_failed(params):
    """
    Place order goes Failed
    """
    project_url = params['project_url']
    driver_path = params['driver_path']
    # ...
    # Your code goes here
    # ...
    assert False
