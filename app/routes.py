from flask import Flask, render_template , redirect , request, url_for
 
app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')  
 
@app.route('/calculate')
@app.route('/calculate/<int:num>')
def calculate(num=None):
    return render_template('calculate.html',num=num)

@app.route('/doit',methods=['POST'])
def doit(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('calculate',num=temp))


if __name__ == '__main__':
  app.run(debug=True)