from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_geek():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Flask Deployment Success</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f7f8;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                background-color: #ffffff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
            }
            h1 {
                color: #4CAF50;
                margin-bottom: 20px;
            }
            p {
                font-size: 18px;
                color: #333333;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background-color: #4CAF50;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            a:hover {
                background-color: #45a049;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Deployment Successful!</h1>
            <p>Successfully deployed Python application through Jenkins! Webhook added.</p>
            <a href="/hi">Say Hi!</a>
        </div>
    </body>
    </html>
    """

@app.route('/hi')
def hell():
    return '<h1>Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii from Flask & Docker</h1>'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
