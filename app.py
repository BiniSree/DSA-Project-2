from flask import Flask, render_template, request
import pickle
import sklearn
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/prediction', methods = ['GET','POST'])
def prediction():
    if request.method == 'POST':
        category = request.form['category']
        encoder1= pickle.load(open('encoder1.pkl','rb'))
        category= encoder1.transform(category)
        encder
        style = request.form['style']
        month = request.form['month']
        model_mdata_rf = pickle.load(open('model_mdata_rf.pkl','rb'))
        sales_count = model_mdata_rf.predict([['category','style','month']])
    return render_template('prediction.html', sales_count = sales_count)


if __name__ == '__main__':
    app.debug = True
    app.run(port=15000)
    
