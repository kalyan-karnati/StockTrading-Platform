# StoxTrade
![image](https://user-images.githubusercontent.com/59049329/194774702-6af1c810-5d60-4746-afbd-3df559d41d70.png)
<!-->
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Open Issues](https://img.shields.io/github/issues/kalyan-karnati/StockTrading-Platform)](https://github.com/kalyan-karnati/StockTrading-Platform/issues)
[![Stars](https://img.shields.io/github/forks/kalyan-karnati/StockTrading-Platform)](https://github.com/kalyan-karnati/StockTrading-Platform/network/members)
[![codecov](https://codecov.io/gh/kalyan-karnati/StockTrading-Platform/branch/dev/graph/badge.svg?token=SmiSDihWvE)](https://codecov.io/gh/kalyan-karnati/StockTrading-Platform)
![GitHub](https://img.shields.io/badge/Language-JavaScript-orange.svg)
![GitHub](https://img.shields.io/badge/Language-Python-green.svg)
![GitHub](https://img.shields.io/badge/Language-HTML-yellow.svg)
![GitHub contributors](https://img.shields.io/badge/Contributors-5-blue)
[![Build-And-Test](https://github.com/kalyan-karnati/StockTrading-Platform/actions/workflows/pipeline.yml/badge.svg)](https://github.com/kalyan-karnati/StockTrading-Platform/actions/workflows/pipeline.yml)
[![DOI](https://zenodo.org/badge/545725634.svg)](https://zenodo.org/badge/latestdoi/545725634)
[![GitHub Release](https://img.shields.io/github/v/release/kalyan-karnati/StockTrading-Platform.svg)](https://github.com/kalyan-karnati/StockTrading-Platform/releases)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/kalyan-karnati/StockTrading-Platform.svg)](https://img.shields.io/github/repo-size/kalyan-karnati/StockTrading-Platform.svg)
[![GitHub contributors](https://img.shields.io/github/contributors/kalyan-karnati/StockTrading-Platform)](https://github.com/kalyan-karnati/StockTrading-Platform/graphs/contributors)
[![Pull Requests](https://img.shields.io/github/issues-pr/kalyan-karnati/StockTrading-Platform)](https://github.com/kalyan-karnati/StockTrading-Platform/pulls)
![Supports Python](https://img.shields.io/pypi/pyversions/pytest)

## About StoxTrade

StoxTrade is an platform where Owner and Trader of stocks transactions takes place.Owner is admin whereas Trader is user:
 
 ### Role of Owner(Admin):
 - Sets the Market timings.
 - Sets the Market Holidays.
 - Creating the new stocks with price, volume.
 - Deleting the stocks.
 
 ### Role of Trader(Admin):
 - Buy/Sell the stock in the Market timings set by admin.
 
## DEMO


https://user-images.githubusercontent.com/59049329/194781197-eaf36d82-ec05-4bef-851b-d0098c6da319.mp4




## Installation guide

1. Install Python (3.8.0 Preffered)

2. Clone this repository to any folder

3. Open Terminal in the cloned folder

4. Linux and Mac OS Users might need to install a few dependecies before installing requirements. (Not needed for Windows Users)

      ```
        sudo apt install libpq-dev
      ```  
5. Install Requirements

```
pip install -r requirements.txt

```

In case, you have an issue installing the dependency psycopg2 in linux, replace the psycopg2==2.8.4 with psycopg2-binary==2.8.3 in the requirements file and try reinstalling all requirements.


6. Run the following:
```
  python wsgi.py
```
7. Go to http://127.0.0.1/ for the UI.



## Contributors:
<a href = "https://github.com/kalyan-karnati/StockTrading-Platform/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=kalyan-karnati/StockTrading-Platform"/>
</a>

## Team Members:
- Kalyan Karnati
- Mukunda Varma Pericherla
- Pranavi Sharma Sanganabhatla
- Saketh Vangala
- Srihitha Reddy Kaalam
