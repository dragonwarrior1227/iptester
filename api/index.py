from flask import Flask, render_template,jsonify, request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random 
import socket 
from webdriver_manager.chrome import ChromeDriverManager
import os,sys, stat
import subprocess

app = Flask(__name__)


# # print(subprocess.Popen("npm install chromium-version@77",shell=True,stdout=subprocess.PIPE).communicate()[0])
chrome_path=r"{}/node_modules/chromium-version/lib/chromium/chrome-linux/chrome".format(os.getcwd())
os.environ['CHROME_PATH']=chrome_path
binary_path=os.environ.get('CHROME_PATH')

path=r'tmp/chrome/chromedriver'
# os.chmod(path, 0o777)

options = Options()

# options.binary_location =binary_path
options.add_argument('--headless')
options.add_argument('--no-sandbox')
# options.add_argument("--proxy-server={}".format(py))
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
# options.add_argument("--incognito")
# options.add_extension('vpn.crx')


@app.route('/')
def hello():
    try:
        driver = webdriver.Chrome(executable_path=path,chrome_options=options)
    except Exception as e:
        print(e)
        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
    print("Your Computer Name2 is:" + hostname)    
    print("Your Computer IP Address2 is:" + IPAddr)
    print(os.listdir(os.getcwd()))
    url = 'https://www.youtube.com/watch?v=ku3HSNT0I-g'
    driver.get(url)
    time.sleep(2)
    driver.quit()


    return 'Hello, world'


@app.route('/test')
def test():
    return 'Test'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

@app.route('/ipt')
def get_tasks():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:

        return jsonify({'ip': request.environ['REMOTE_ADDR']}), 200
    else:
        return jsonify({'ip': request.environ['HTTP_X_FORWARDED_FOR']}), 200

