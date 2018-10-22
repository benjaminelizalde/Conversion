from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
@app.route("/response1")
def render_response1():
    Pounds = float(request.args['Pounds'])
    Stones = Pounds * 0.0714286
    return render_template('response.html', response = Stones)
    
@app.route("/response2")
def render_response2():
    Stones = float(request.args['Stones'])
    Pounds = Stones / 0.0714286
    return render_template('response.html', response = Pounds)
    

@app.route("/response3")
def render_response3():
    Ounces = float(request.args['Ounces'])
    Money = Ounces * 1227.35
    return render_template('response.html', response = Money)
    
    
 
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
