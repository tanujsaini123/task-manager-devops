from flask import Flask, send_from_directory
import random
import os

app = Flask(__name__)

quotes = [
    {"quote": "Push yourself, because no one else is going to do it for you.", "author": "Unknown"},
    {"quote": "Great things never come from comfort zones.", "author": "Anonymous"},
    {"quote": "Dream it. Wish it. Do it.", "author": "Unknown"}
]

@app.route('/')
def home():
    images = os.listdir('static/images')
    image = random.choice(images)
    selected = random.choice(quotes)

    html = f'''
    <html>
    <head><title>Inspiration Gallery</title></head>
    <body style="text-align:center; font-family:sans-serif;">
        <h1>🌟 {selected['quote']}</h1>
        <h3>— {selected['author']}</h3>
        <img src="/images/{image}" width="600" />
        <p><a href="/">🔁 Refresh</a></p>
    </body>
    </html>
    '''
    return html

@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
