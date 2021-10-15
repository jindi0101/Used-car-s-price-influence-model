from bs4 import BeautifulSoup
import urllib
import requests
import pandas as pd

def extract(): 
    i=0
    data_list=[]
    while i<1000:
        a=1
        list_price=[]
        list_mileage=[]
        list_color=[]
        list_model=[]
        list_year=[]
        url='https://www.kbb.com/cars-for-sale/used/honda/accord/los-angeles-ca-90001?makeCodeList=HONDA&searchRadius=500&modelCodeList=ACCORD&zip=90001&marketExtension=include&listingTypes=USED&isNewSearch=true&sortBy=relevance&numRecords=25&firstRecord='+str(i)
        website=requests.get(url)
        soup=BeautifulSoup(website.content,'html.parser')
        tag1=soup('div')
        for tag in tag1:
            if tag.get('class',None):
                if tag.get('class',None)[0]=='text-gray-base':
                    if 'MSRP' in tag.text.split(',')[1] and '$' not in tag.text.split(',')[1]:
                        list_price.append(float(tag.text.split(',')[0]+tag.text.split(',')[1].rstrip('MSRP')))
                    elif '$' in tag.text.split(',')[1]:
                        list_price.append(float(tag.text.split(',')[0]+tag.text.split(',')[1].split(' ')[0].rstrip('MSRP')))
                    else:
                        list_price.append(float(tag.text.split(',')[0]+tag.text.split(',')[1]))
                if tag.get('class',None)[0]=='text-bold':
                    if 'miles' in tag.text: 
                        if len(tag.text.split(' ')[0].lstrip('('))<5:
                            list_mileage.append(float(tag.text.split(' ')[0].lstrip('(')))
                        else:
                            list_mileage.append(float(tag.text.split(' ')[0].split(',')[0]+tag.text.split(' ')[0].split(',')[1]))
                if tag.get('class',None)[0]=='display-flex':
                    if 'Accord' in tag.text:
                        list_year.append(int(tag.text.split(' ')[1]))
                        list_model.append(tag.text.split(' ')[3])
                if tag.get('class',None)[0]=='item-card-specifications':
                    list_color.append(tag.text.split(':')[1])
        while a<28:
            data_list.append([list_year[a],list_model[a],list_mileage[a-1],list_price[a],list_color[a]])
            a=a+1
        i=i+25
    print(data_list)
    name=['year','model','mileage','price','color']
    file=pd.DataFrame(columns=name,data=data_list)
    file.to_csv('kbb_data.csv',index=False,encoding="utf-8")

if __name__ == "__main__":
    extract()
