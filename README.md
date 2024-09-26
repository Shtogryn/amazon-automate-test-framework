# amazon-automate-test-framework
Python UI test framework for amazon.com markerplace 

# Configuration
Install packages run **pip install  -r .\requirements.txt**

# How to use it

**Run all test cases**

"pytest -v -s"  
### Command samples for Address model


**Run positive test cases**

"pytest -v -m  positive

**Run negative test cases**

"pytest -v -m  negative

**To generate and see report**

"pytest -v -m addresses --alluredir reports"

"allure serve reports"
(Ensure that the Allure is installed)

