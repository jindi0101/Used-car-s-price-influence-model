import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import kbb_extraction
import cars_extraction

def kbb_analysis():
    print('The relationship between mileage and price:')
    data=pd.read_csv('kbb_data.csv',header=0)#import kbb website data
    X1 = data['mileage'].values.reshape(-1,1)
    y1 = data['price'].values.reshape(-1,1)
    X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=0)
    #split data
    reg = LinearRegression() 
    # linear regression
    reg.fit(X1_train, y1_train) 
    print('coefficient:',reg.coef_,'intercept_:',reg.intercept_)
    #print coefficient and intercept
    y1_pred = reg.predict(X1_test)
    #predict y1
    plt.scatter(X1_test, y1_test, color='gray')
    plt.plot(X1_test, y1_pred, color='red', linewidth=2)
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.show()
    print('The relationship between year and price:')
    X2=data['year'].values.reshape(-1,1)
    y2 = data['price'].values.reshape(-1,1)
    X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=0)
    #split data
    reg.fit(X2_train, y2_train)
    y2_pred = reg.predict(X2_test)
    #predict y2
    print('coefficient:',reg.coef_,'intercept_:',reg.intercept_)
    #print coefficient and intercept
    plt.scatter(X2_test, y2_test,  color='gray')
    plt.plot(X2_test, y2_pred, color='red', linewidth=2)
    plt.xlabel("year")
    plt.ylabel("price")
    plt.show()
    print('The relationship between mileage, year and price:')
    X=data[['mileage','year']]
    y=data['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 
    #split data
    reg.fit(X_train, y_train) 
    y_pred = reg.predict(X_test)
    #predict y
    df = pd.DataFrame({'Actual price': y_test, 'Predicted price': y_pred})# predict price 
    print(df)
    df_25 = df.head(25)#get 25 data
    df_25.plot(kind='bar',figsize=(10,8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()
    model = LinearRegression().fit(X, y)
    model = sm.OLS(y, X)#linear regression
    results = model.fit()
    print(results.summary())#parameters of linear regression


def cars_analysis():
    print('The relationship between mileage and price:')
    data=pd.read_csv('cars_data.csv',header=0)
    X1 = data['mileage'].values.reshape(-1,1)
    y1 = data['price'].values.reshape(-1,1)
    X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=0)
    reg = LinearRegression() 
    reg.fit(X1_train, y1_train) 
    y1_pred = reg.predict(X1_test)
    print('coefficient:',reg.coef_,'intercept_:',reg.intercept_)
    plt.scatter(X1_test, y1_test,  color='gray')
    plt.plot(X1_test, y1_pred, color='red', linewidth=2)
    plt.xlabel("mileage")
    plt.ylabel("price")
    plt.show()

    print('The relationship between year and price:')
    X2=data['year'].values.reshape(-1,1)
    y2 = data['price'].values.reshape(-1,1)
    X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=0)
    reg.fit(X2_train, y2_train)
    y2_pred = reg.predict(X2_test)
    print('coefficient:',reg.coef_,'intercept_:',reg.intercept_)
    plt.scatter(X2_test, y2_test,  color='gray')
    plt.plot(X2_test, y2_pred, color='red', linewidth=2)
    plt.xlabel("year")
    plt.ylabel("price")
    plt.show()
    
    print('The relationship between mileage, year and price:')
    X=data[['mileage','year']]
    y=data['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)  
    reg.fit(X_train, y_train)
    coeff = pd.DataFrame(reg.coef_, X.columns, columns=['Coefficient'])  
    y_pred = reg.predict(X_test)
    df = pd.DataFrame({'Actual price': y_test, 'Predicted price': y_pred})
    print(df)
    df_25 = df.head(25)
    df_25.plot(kind='bar',figsize=(10,8))
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()
    model = LinearRegression().fit(X, y)
    model = sm.OLS(y, X)
    results = model.fit()
    print(results.summary())
    plt.hist(data['color'], bins=40, density=0, facecolor="blue", edgecolor="black", alpha=0.7)
    print(data.sort_values(by=['review'], ascending=False).head(25))
    print(data.sort_values(by=['review'], ascending=False).head(25).mean())
    
    
if __name__ == "__main__":
    kbb_extraction.extract()
    cars_extraction.get_data()
    kbb_analysis()
    cars_analysis()