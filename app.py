from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
@app.route('/')
def hello():
    return render_template('index.html')
@app.route('/prediction', methods = ['GET','POST'])
def prediction():
    if request.method == 'POST':
        category = request.form['category']
        style = request.form['style']
        month = request.form['month']
        model_mdata_rf = pickle.load(open('model_mdata_rf.pkl','rb'))
        sales_count = model_mdata_rf.predict([['category','style','month']])
    return render_template('prediction.html', sales_count = sales_count)





if __name__ == '__main__':
    app.debug = True
    app.run(port=15000)
    
