from app import create_app
import webbrowser
import threading
import time


app = create_app()

def open_browser():
    time.sleep(1.5)
    webbrowser.open_new("http://localhost:5000")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(debug=True, host='localhost', port=5000)
