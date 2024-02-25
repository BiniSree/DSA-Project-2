from flask import Flask, render_template, request
import pickle
import sklearn
import pandas as pd
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction', methods = ['GET','POST'])
def prediction():
    print("INSIDE PREDICTION")
    if request.method == 'POST':
        category = request.form['category']
        style = request.form['style']
        month = request.form['month']
        print("VALUES COLLECTED FROM WEB:", category, style, month)
        df= pd.DataFrame()
        df['Category']= []
        df['Style']=[]
        df['month']= []
        print("MY DATAFRAME init : \n",df)
        #df['Category']= category
        #df['Style']= style
        #df['month']= month
        df.loc[0] = [category,style,month]
        #df= df.drop(df.index)
        print("MY DATAFRAME : \n",df)
        print("MY DATAFRAME : \n",df['Category'])
        print("CATEGORY BEFORE ENCODING :", category)
        encoder1= pickle.load(open('encoder1.pkl','rb'))
        print("AFTER PICKLE.LOAD", encoder1.classes_)
        category= encoder1.transform(df['Category'])
        print("The encoded category is : ", category)
        encoder2= pickle.load(open('encoder2.pkl','rb'))
        style= encoder2.transform(df['Style'])
        print("The encoded style is : ", style)
        encoder3= pickle.load(open('encoder3.pkl','rb'))
        month= encoder3.transform(df['month'])
        print("The encoded month is : ", month)
        #encoder= pickle.load(open('encoder.pkl','rb'))
        print("DATATYPE OF DF : ", type(df))
        print("To be transformed data : ", df)
        #encoded_category= encoder.fit_transform([df['Category']])
        #encoded_style= encoder.fit_transform(df['Style'])
        #encoded_month= encoder.fit_transform(df['month'])
        df.loc[0] = [category,style,month]
        
        print("The encoded df is : \n", df)
        model_mdata_rf = pickle.load(open('model_mdata_rf.pkl','rb'))
        sales_count = model_mdata_rf.predict(df)
        scaler1= pickle.load(open('scaler1.pkl','rb'))


    return render_template('prediction.html', sales_count = sales_count)


if __name__ == '__main__':
    app.debug = True
    app.run(port=15000)
    
