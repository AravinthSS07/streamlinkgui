from flask import *
from pyfladesk import *
import os

app = Flask(__name__)

app.secret_key = 'aravinthss_ar7'

def streamlink(streamurl, streamquality):
    os.system(f'streamlink {streamurl} {streamquality}')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'url' in request.form and 'quality' in request.form:
        url = request.form['url']
        quality = request.form.get('quality')
        streamlink(streamurl=url, streamquality=quality)
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=5000, debug=True)
    init_gui(app, port=5000, width=952, height=530, window_title='Streamlink GUI Client')