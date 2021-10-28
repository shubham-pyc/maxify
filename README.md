# Maxify
Python CLI for cloning, updating, creatign code for maxymiser platform



## Prerequisite
1. Install [Python 2.7.x](https://www.python.org/downloads/release/python-2718/)
2. Install [Pip](https://pip.pypa.io/en/stable/installing/)
3. Set ENV variable OPTIMIZATION_HOME = path to web-optimization folder

## Installtion
Install Package

```shell 
    pip install "git+https://github.com/shubham-pyc/maxify"
```
## Usage

1. Below command is used to clone any campaign 

```shell
    maxify clone -n "QA - Some campaign"
```
2. Update file on maxymiser
    a. Goto source folder of the campaign
    b. open folder in vscode
    c. press clt + shift + p
    d. select push task and press enter 


## RoadMap
1. Packaging for easy installation
2. Write unit test cases for current code to achieve 80% code coverage
3. Create push all scripts functionality
4. When cloning the campaign if scripts are not empty on maxymiser inject the scripts with code present on maxymiser
5. Create a sync functionality. This will be used if new file is added to maxymiser
6. Take maxymiser password from user currently it is hard coded. Ask the password again if it is expired
7. Explore git integration
8. Enable campaign creation on maxymiser through maxify
9. Interate webpack bundler before pushing to maxymiser
10. Enable Saas to css convertor through webpack ( This would enable us to write less css )
11. Enable ES6 to ES5 converstion through babel ( This would enable us to write cross browser runnable code)
12. Explore how to add Redux to our campaigns
13. Enable campagin migration through maxify


Author © [Shubham Gupta](mailto:shubhamg2404@gmail.com)
