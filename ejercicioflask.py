from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola, Flask está funcionando'

if __name__=='__main__':
    app.run(debug=True)
    