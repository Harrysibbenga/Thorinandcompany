import os
import json
from flask import Flask, render_template

'''
runs the server by importing the os through cloud9. 

imports the Flask object inside the flask module.
'''



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', page_title='Home')
    
@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template('about.html', page_title='About', company_data=data)
    
@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj['url'] == member_name:
                member = obj
                
    return render_template('member.html', member=member)


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact Us')
    
@app.route('/careers')
def careers():
    return render_template('careers.html', page_title='Come Work With Us')
    
if __name__ == '__main__':
    
    '''
    allows us to get the ip address
    
    tells flask which ip address we want to run this on.
    
    debug mode is true so we can debug the code as we are developing the application
    if debug is false then we wont be able to vie the changes live.
    '''
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)