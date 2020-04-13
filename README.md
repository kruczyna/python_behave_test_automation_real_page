# Requirements- Linux (Chrome):
1. Python3
2. Chrome browser, may be headless
3. pip install -r requirements.txt
4. sh ./chromedriver_update.sh (this will install or update chromedriver to /usr/local/bin/)

# Requirements- Windows:
1. Python 3
2. Edge browser
3. **run as administrator**: `pip install -r requirements.txt`
4. create a directory for webdriver executables and add it to path

# Configuration- behave.ini
1. main_url- main page url
3. login credentials 
4. implicit wait
5. browser- selects browser to be used in test. Valid choices are:
  * Chrome
  * Chrome_headless
  * Edge
  * Ie

# Running tests
execute always in `features` directory (same level as requirements.txt and chromedriver_update.sh are)
1. one feature:
  * behave -i [name].feature
2. all features, alphabetical order:
  * behave
3. all features, alphabetical order:
  * behave -n "[name]"

# Configuration: .feature files

  * all string enclosed in double quotes are step parameters and can be changed

