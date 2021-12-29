#!/bin/bash

# pytest --html=Report/report.html --self-contained-html
rm -r allure_results/
pytest --alluredir=$PWD/allure_results
allure generate $PWD/allure_results -o $PWD/Report --clean
allure open $PWD/Report
