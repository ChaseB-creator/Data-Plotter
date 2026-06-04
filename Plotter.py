from flask import Flask
import webbrowser
import threading
import time

app = Flask(__name__, static_folder='.', static_url_path='')


def open_browser():
    """Open the browser after a short delay to ensure Flask is running."""
    time.sleep(1)
    webbrowser.open('http://127.0.0.1:5000/Tester.html')


@app.route('/')
def index():
    return app.send_static_file('Tester.html')


@app.route('/Tester.html')
def tester():
    return app.send_static_file('Tester.html')


if __name__ == '__main__':
    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    app.run(debug=False)

