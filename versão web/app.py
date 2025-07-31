from flask import Flask, render_template, jsonify
import speedtest
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-speedtest')
def run_speedtest():
    try:
        st = speedtest.Speedtest()
        
        # Atualização de progresso
        st.get_best_server()
        ping = st.results.ping
        
        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        
        return jsonify({
            'status': 'success',
            'ping': round(ping, 2),
            'download': round(download, 2),
            'upload': round(upload, 2)
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)