from flask import Flask, render_template, jsonify
import speedtest
from ping3 import ping as cping
import time

# tem que mudar tudo aqui pra funcionar os que tão em branco
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run-speedtest")
def run_speedtest():
    try:
        st = speedtest.Speedtest()
        best_server = st.get_best_server()
        server_nome = f"{best_server['name']}, {best_server['country']}"

        # Atualização de progresso
        st.get_best_server()
        ping = st.results.ping

        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        ping_val = st.results.ping

        ##server = best_server['latency']

        host = "google.com"
        count = 10
        interval = 0.5
        pings = []

        for _ in range(count):
            result = cping(host, timeout=2)
            pings.append(result * 1000 if result else None)
            time.sleep(interval)

        valid = [p for p in pings if p is not None]
        jitter = 0
        avg_cping = 0
        if len(valid) >= 2:
            jitter_values = [abs(valid[i] - valid[i - 1]) for i in range(1, len(valid))]
            jitter = sum(jitter_values) / len(jitter_values)

            avg_cping = sum(valid) / len(valid) if valid else 0

        return jsonify(
            {
                "status": "success",
                "ping": round(ping_val, 2),
                "download": round(download, 2),
                "upload": round(upload, 2),
                "cping": round(avg_cping, 2),
                "jitter": round(jitter, 2),
                "server": server_nome,
            }
        )

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
