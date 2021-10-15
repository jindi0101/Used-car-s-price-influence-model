from bs4 import BeautifulSoup
import urllib
import requests
import pandas as pd

def get_data():
    i=1
    data_list=[]
    while i<11:
        a=0
        list_price=[]
        list_mileage=[]
        list_color=[]
        list_model=[]
        list_review=[]
        list_year=[]
        website=requests.get('https://www.cars.com/for-sale/searchresults.action/?mdId=20444&mkId=20005&page='+str(i)+'&perPage=100&rd=99999&searchSource=PAGINATION&sort=relevance&stkTypId=28881&zc=90007')
        soup=BeautifulSoup(website.content,'html.parser') 
        tag1=soup('span')
        for tag in tag1:
            if tag.get('class',None):
                if tag.get('class',None)[0]=='listing-row__price':
                    list_price.append(float(tag.text.strip('\n ').lstrip('$').split(',')[0]+tag.text.strip('\n ').lstrip('$').split(',')[1]))
                if tag.get('class',None)[0]=='listing-row__mileage':
                    list_mileage.append(float(tag.text.strip('\n ').rstrip(' mi.').split(',')[0]+tag.text.strip('\n ').rstrip(' mi.').split(',')[1]))
                if tag.get('class',None)[0]=='listing-row__review-number':
                    list_review.append(int(tag.text.strip('\n ').strip('(').strip(')').rstrip(' reviews')))
        tag2=soup('h2')
        for tag in tag2:
            if tag.get('class',None):
                if tag.get('class',None)[0]=='listing-row__title':
                    year=tag.text.strip('\n ').split(' ')[0]
                    model=tag.text.strip('\n ').split(' ')[1]+tag.text.strip('\n ').split(' ')[2]+tag.text.strip('\n ').split(' ')[3]
                    list_year.append(int(year))
                    list_model.append(model)
        tag3=soup('ul')
        for tag in tag3:
            if tag.get('class',None):
                if tag.get('class',None)[0]=='listing-row__meta':
                    list_color.append(tag.text[55:62].strip('\n '))
        while a<80:
            data_list.append([list_year[a],list_model[a],list_mileage[a],list_review[a],list_color[a],list_price[a]])
            a=a+1
        i=i+1
    print(data_list)
    name=['year','model','mileage','review','color','price']
    file=pd.DataFrame(columns=name,data=data_list)
    file.to_csv('cars_data.csv',index=False,encoding="utf-8")
    
if __name__ == "__main__":
    get_data()