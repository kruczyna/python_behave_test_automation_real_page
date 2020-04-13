# Requirements- Linux (Chrome):
1. Python3
2. Chrome browser, may be headless
3. pip install -r requirements.txt
4. sh ./chromedriver_update.sh (this will install or update chromedriver to /usr/local/bin/)


# Configuration- behave.ini
1. main_url- main page url
3. login credentials 

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

