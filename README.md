# amazon-automate-test-framework
Python UI test framework for amazon.com markerplace 

# Configuration
Install packages run **pip install  -r .\requirements.txt**

# How to use it

**Run all test cases**

"pytest -v -s"  
### Command samples for diffrence scopes of tests


**Run positive test cases**

"pytest -v -m  positive"


**Run negative test cases**

"pytest -v -m  negative"


**Run search test cases**

"pytest -v -m  search"


**Run filter test cases**

"pytest -v -m  filter"


**Run cart test cases**

"pytest -v -m  cart'"


**To generate and see report**

"pytest -v -s --alluredir reports"

"allure serve reports" - to view test running report
"allure generate reports" - to generate test running report

(Ensure that the Allure is installed)
