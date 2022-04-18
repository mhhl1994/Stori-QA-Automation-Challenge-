Tester: Mario Hernandez 
Date: 2022.04.17


Dependencies:
    * pytest
    * pytest-html 
    * selenium 

Please install by using pip 
    > pip install <dependencies>


To run all test suites run:
    > pytest

To run all test suites and generate reports run:
    > pytest --html=Reports/report.html --junitxml=Reports/report.xml


Custom parameters:
--browser <browser_name>    Default is chrome. Accepted browsers are firefox and chrome 