from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    try:
        with open('/app/rally-sync.html', 'r') as f:
            return f.read(), 200, {'Content-Type': 'text/html'}
    except Exception as e:
        return f"Error: {e}", 500

@app.route('/rally-sync.html')
def rally_page():
    try:
        with open('/app/rally-sync.html', 'r') as f:
            return f.read(), 200, {'Content-Type': 'text/html'}
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
