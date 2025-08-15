from flask import Flask, render_template, jsonify, request
import speedtest
from ping3 import ping as cping
import requests
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ADDITIONAL_SERVERS = [
    {"id": "14993", "host": "barespeedtest.claro.com.br:8080", "sponsor": "Claro", "name": "Claro SP", "country": "BR"},
    {"id": "17145", "host": "sp-speedtest.claro.com.br:8080", "sponsor": "Claro", "name": "Claro RJ", "country": "BR"},
    {"id": "10390", "host": "speedtest.vivo.com.br:8080", "sponsor": "Vivo", "name": "Vivo SP", "country": "BR"},
    {"id": "10776", "host": "speedtest2.vivo.com.br:8080", "sponsor": "Vivo", "name": "Vivo RJ", "country": "BR"},
    {"id": "10775", "host": "speedtest.tim.com.br:8080", "sponsor": "TIM", "name": "TIM SP", "country": "BR"},
    {"id": "16472", "host": "speedtest.oi.com.br:8080", "sponsor": "Oi", "name": "Oi RJ", "country": "BR"},
    {"id": "16473", "host": "speedtest.algartelecom.com.br:8080", "sponsor": "Algar", "name": "Algar Telecom", "country": "BR"},
    {"id": "17777", "host": "speedtest.sercomtel.com.br:8080", "sponsor": "Sercomtel", "name": "Sercomtel PR", "country": "BR"},
    {"id": "18575", "host": "speedtest2.algartelecom.com.br:8080", "sponsor": "Algar", "name": "Algar Telecom 2", "country": "BR"},
    {"id": "28910", "host": "speedtest1.movistar.com.pe:8080", "sponsor": "Movistar", "name": "Lima", "country": "PE"},
    {"id": "37235", "host": "speedtest.entelchile.net:8080", "sponsor": "Entel", "name": "Santiago", "country": "CL"},
    {"id": "48826", "host": "speedtest.telecom.com.ar:8080", "sponsor": "Telecom", "name": "Buenos Aires", "country": "AR"},
    {"id": "30852", "host": "nyc.speedtest.t-mobile.com:8080", "sponsor": "T-Mobile", "name": "New York", "country": "US"},
    {"id": "10392", "host": "la.speedtest.t-mobile.com:8080", "sponsor": "T-Mobile", "name": "Los Angeles", "country": "US"},
    {"id": "17754", "host": "speedtest.shaw.ca:8080", "sponsor": "Shaw", "name": "Vancouver", "country": "CA"},
    {"id": "4246", "host": "speedtest.fdcservers.net:8080", "sponsor": "FDC", "name": "Frankfurt", "country": "DE"},
    {"id": "14623", "host": "speedtest.serverius.net:8080", "sponsor": "Serverius", "name": "Amsterdam", "country": "NL"},
    {"id": "26478", "host": "speedtest.uk.barracuda.com:8080", "sponsor": "Barracuda", "name": "London", "country": "GB"},
    {"id": "3633", "host": "speedtest.tokyo.linode.com:8080", "sponsor": "Linode", "name": "Tokyo", "country": "JP"},
    {"id": "17205", "host": "speedtest.singapore.linode.com:8080", "sponsor": "Linode", "name": "Singapore", "country": "SG"},
    {"id": "5135", "host": "speedtest.hk.leaseweb.com:8080", "sponsor": "Leaseweb", "name": "Hong Kong", "country": "HK"},
    {"id": "16176", "host": "speedtest.syd1.linode.com:8080", "sponsor": "Linode", "name": "Sydney", "country": "AU"},
    {"id": "12204", "host": "speedtest.xtra.co.nz:8080", "sponsor": "Spark", "name": "Auckland", "country": "NZ"},
    {"id": "37213", "host": "speedtest.joburg.liquidtelecom.com:8080", "sponsor": "Liquid", "name": "Johannesburg", "country": "ZA"},
    {"id": "37657", "host": "speedtest.nairobi.liquidtelecom.com:8080", "sponsor": "Liquid", "name": "Nairobi", "country": "KE"},
    {"id": "7311", "host": "speedtest.wdc01.softlayer.com:8080", "sponsor": "IBM Cloud", "name": "Washington DC", "country": "US"},
    {"id": "5396", "host": "speedtest.dal05.softlayer.com:8080", "sponsor": "IBM Cloud", "name": "Dallas", "country": "US"},
    {"id": "27377", "host": "speedtest.fra02.softlayer.com:8080", "sponsor": "IBM Cloud", "name": "Frankfurt", "country": "DE"},
    {"id": "7557", "host": "speedtest.sng01.softlayer.com:8080", "sponsor": "IBM Cloud", "name": "Singapore", "country": "SG"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run-speedtest")
def run_speedtest():
    try:
        st = speedtest.Speedtest()
        st.timeout = 15
        
        server_id = request.args.get('server_id', '0')
        if server_id != '0':
            try:
                additional_server = next((s for s in ADDITIONAL_SERVERS if s['id'] == server_id), None)
                if additional_server:
                    st.get_servers([{
                        'id': server_id,
                        'host': additional_server['host'],
                        'sponsor': additional_server['sponsor'],
                        'name': additional_server['name'],
                        'country': additional_server['country']
                    }])
                    logger.info(f"Usando servidor customizado: {additional_server['sponsor']}")
            except Exception as e:
                logger.error(f"Erro ao configurar servidor: {e}")

        best_server = st.get_best_server()
        logger.info(f"Servidor selecionado: {best_server['sponsor']} ({best_server['name']})")

        download = st.download(threads=4) / 1_000_000
        upload = st.upload(pre_allocate=False, threads=4) / 1_000_000
        ping_val = st.results.ping

        hosts = ["google.com", "cloudflare.com", "facebook.com"]
        pings = []
        
        for host in hosts:
            try:
                p = cping(host, timeout=2)
                if p is not None:
                    pings.append(p * 1000)
            except:
                continue

        if len(pings) >= 2:
            jitter = sum(abs(pings[i]-pings[i-1]) for i in range(1, len(pings))) / (len(pings)-1)
            avg_cping = sum(pings)/len(pings)
        else:
            jitter = 0
            avg_cping = pings[0] if pings else 0

        return jsonify({
            "status": "success",
            "server": f"{best_server['sponsor']} ({best_server['name']}, {best_server['country']})",
            "download": round(download, 2),
            "upload": round(upload, 2),
            "ping": round(ping_val, 2),
            "cping": round(avg_cping, 2),
            "jitter": round(jitter, 2)
        })

    except Exception as e:
        logger.error(f"Erro no speedtest: {e}")
        return jsonify({
            "status": "error",
            "message": str(e),
            "solution": "Tente novamente ou selecione outro servidor"
        }), 500

@app.route("/list-servers")
def list_servers():
    try:
        servers_list = ADDITIONAL_SERVERS.copy()
        
        try:
            st = speedtest.Speedtest()
            servers = st.get_servers()
            
            for country, server_list in servers.items():
                for server in server_list:
                    servers_list.append({
                        "id": str(server["id"]),
                        "name": server["name"],
                        "country": country,
                        "sponsor": server["sponsor"],
                        "host": server["host"]
                    })
        except Exception as e:
            logger.warning(f"Não foi possível obter servidores públicos: {e}")

        unique_servers = {v['id']:v for v in servers_list}.values()
        sorted_servers = sorted(unique_servers, key=lambda x: (
            0 if x['country'] == 'BR' else 1,
            x['country'],
            x['name']
        ))
        
        return jsonify(list(sorted_servers))
        
    except Exception as e:
        logger.error(f"Erro ao listar servidores: {e}")
        return jsonify(ADDITIONAL_SERVERS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)