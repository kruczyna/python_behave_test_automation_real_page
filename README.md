# Requirements- Linux (Chrome):
1. Python3
2. Chrome browser, may be headless
3. pip install -r requirements.txt
4. sh ./chromedriver_update.sh (this will install or update chromedriver to /usr/local/bin/)

# Running tests
execute always in `features` directory (same level as requirements.txt and chromedriver_update.sh are)
* one feature:
  * behave -i [name].feature
* all features, alphabetical order:
  * behave
* all features, alphabetical order:
  * behave -n "[name]"

# Configuration: .feature files
  * all strings enclosed in double quotes are step parameters and can be changed

