import json
from bs4 import BeautifulSoup
import urllib
import requests
import pandas as pd
def get_cars_infomation(make,model):
    data_list=[]
    api_key='Z7sq4yf1s4IjVLgzZfVhWU2LiKdVHScy'#get api key
    j=2020
    while j>2019:# extrat 2020 data
        list_price=[]
        list_mileage=[]
        list_model=[]
        list_year=[]
        a=1
        url='http://marketcheck-prod.apigee.net/v2/search/car/active?api_key='+api_key+'&year='+str(j)+'&make='+make +'&model'+model
        resp=requests.get(url)#connect url
        js=resp.json()# covert json formal
        prettyjs=json.dumps(js, indent=4, sort_keys=True)
        for i in range(10):
            list_model.append(js['listings'][i]['build']['model'])#model data
            list_year.append(js['listings'][i]['build']['year'])#year data
            list_price.append(js['listings'][i]['price'])#price data
            list_mileage.append(js['listings'][i]['ref_miles'])#mileage data
        while a<9:
            data_list.append([list_year[a],list_model[a],list_mileage[a],list_price[a]])# total of data
            a=a+1
        j=j-1
    name=['year','model','mileage','price']
    return data_list

if __name__ == "__main__":
    get_cars_infomation('honda','accord')