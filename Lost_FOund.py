print('Hello World')
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from datetime import datetime
responce = ""
responce2 = ""
responce3 = ""
responce4 = ""

@app.route('/home')
def my_page():
    global responce, responce2, responce3, responce4
    now = datetime.now()  # current date and time
    year = now.strftime("%Y")
    print("year:", year)
    month = now.strftime("%m")
    print("month:", month)
    day = now.strftime("%d")
    print("day:", day)
    time = now.strftime("%H:%M:%S")
    print("time:", time)
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    responce = request.args.get('user')
    responce2 =  request.args.get('email')
    responce3 = request.args.get('location')
    responce4 = request.args.get('image')
    checkbox=request.args.get('checkbox') 
   print("Found? %d (var1.get()))

Label(master, text="Status").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Found.", variable=var1).grid(row=1, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()

    return render_template('home.html', time= date_time)

@app.route('/blog')
def my_page2():
    global responce, responce2, responce3, responce4

    now = datetime.now()  # current date and time
    year = now.strftime("%Y")
    print("year:", year)
    month = now.strftime("%m")
    print("month:", month)
    day = now.strftime("%d")
    print("day:", day)
    time = now.strftime("%H:%M:%S")
    print("time:", time)

    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    return render_template('blog.html', time= date_time, user = responce, email = responce2, location = responce3, image= responce4)

@app.route('/')
def index():
    return redirect('/home')


@app.route('/double/<number>')
def double(number):

    responce = request.args.get('user')
    responce2 =  request.args.get('email')
    responce3 = request.args.get('location')
    responce4 = request.args.get('image')




app.run(debug=True)
link
rel = "stylesheet"
