from flask import Flask, render_template, request
import payjp
import os

app = Flask(__name__)

SECRET_KEY = 'b'
PUBLIC_KEY = ''

payjp.api_key = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.js')
def index_js():
    return render_template('index.js')

@app.route('/payment', methods=['POST'])
def payment():
    print(request.json.get('token'))
    amount = 1000
    customer = payjp.Customer.create(
        card=request.json.get('token')
    )

    payjp.Charge.create(
        amount=amount,
        currency='jpy',
        customer=customer.id,
        description='flask example charge'
    )

    return "success"


if __name__ == '__main__':
    app.run(debug=True)