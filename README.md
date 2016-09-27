The files and folders contains the solutions of problems given by LOKTRA Team

1. File reverse_hash.py contains the solution of https://github.com/Loktra/software-engineer/blob/master/Hash.md (Reverse Hash problem)

2.Directory Shopping contains the solution of https://github.com/Loktra/software-engineer/blob/master/Web%20Crawler.md



Steps to install pip 

Ubuntu
Type Commands in terminal
	sudo apt-get update && sudo apt-get -y upgrade
	sudo apt-get install python-pip


Steps to install scrapy

Ubuntu

Type Commands in terminal
	pip install Scrapy

Check if its installed using
	scrapy version [-v]

Testing Task "Python Crawler"
	1. Open terminal and Type cd Loktra/Shopping/Shopping
	2. Scrapy Framework is used for making the Crawler 
	Use command 
	scrapy crawl shop -a keyword=[String Value]
	scrapy crawl shop -a keyword=[String Value] -a page=[Number]

	example scrapy crawl shop -a keyword='handbags-and-wallets' -a page='2'
               scrapy crawl shop -a keyword='handbags-and-wallets'
               scrapy crawl shop 


3 . uri.py is the program for https://github.com/Loktra/software-engineer/blob/master/Python%20Uri.md
	Run the program and enter the uri


