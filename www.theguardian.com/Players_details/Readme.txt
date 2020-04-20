Libraries Required:

Kindly install these libraries in your python compiler and then run the program.

* BeautifulSoup
* selenium
* csv
* json
* Chrome web browser

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Json format:

{Country:{ Defender,Forwards,etc:{ PlayerNumber:{playerDetails
						}
					}
			}
	}
}	

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Chrome driver:

For this program to work you have to change the chrome drivers path to your chromedriver.exe file path.

or remain in the same folder where code.py

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This code tested on both spyder and jupyter notebook with python 2.7 base

Run it on basic compiler by using python 

csv.__version__ '1.0'
selenium.__version__ '3.12.0'
bs4.__version__ '4.6.0'
json.__version__ '2.0.9'
