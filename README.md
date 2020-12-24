There are two different options available to perform the testing using HEADLESS approach. 
1. Selenium
   This is very popular and have a package available in Python. We can simply use this with Pytest(Python package for writing test cases) and solves our purpose. 

2. Puppeteer
   Puppeteer is also a good option but we need to learn Jest framework which is written in javascript and need to have Nodejs experience. 

They both provide HEADLESS option, so that test cases can run without visiualing the browser GUI. So we decided to go with Selenium for automation.


I have added both Selenium and Puppeteer both to test the headless browser testing experience.

Steps to Run:
-------------
1. Create virtaul environment
2. Install requirements.txt
3. Run python suite.py


Troubleshooting:
----------------
Please install the correct drivers specific to your operating system:
For Centos:
$ wget https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip
$ unzip chromedriver_linux64.zip
$ chromedriver --version
ChromeDriver 2.40.565383

You also need to install Google Chrome on Centos:
https://intoli.com/blog/installing-google-chrome-on-centos/
I chose the 'The Hard Way' option in the above page.