#!/bin/bash

# pytest --html=Report/report.html --self-contained-html
rm -r allure_results/
pytest --alluredir=/home/we2am/Documents/GitHub/plotX/allure_results
allure generate /home/we2am/Documents/GitHub/plotX/allure_results -o /home/we2am/Documents/GitHub/plotX/Report --clean
allure open /home/we2am/Documents/GitHub/plotX/Report
