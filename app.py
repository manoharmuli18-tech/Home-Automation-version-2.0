try:
    from flask import Flask, render_template  # type: ignore[import]
except ImportError as exc:
    raise ImportError(
        "Missing dependency 'flask'. Install with 'pip install flask'"
    ) from exc
try:
    from flask_socketio import SocketIO  # type: ignore[import]
except ImportError as exc:
    raise ImportError(
        "Missing dependency 'flask_socketio'. Install with 'pip install flask-socketio'"
    ) from exc
try:
    import paho.mqtt.client as mqtt  # type: ignore[import]
except ImportError as exc:
    raise ImportError(
        "Missing dependency 'paho-mqtt'. Install with 'pip install paho-mqtt'"
    ) from exc
import json
import ssl

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

BROKER   = "a4a03546a8184ee38c68c7e42a5d9302.s1.eu.hivemq.cloud"
PORT     = 8883
TOPIC    = "iot/sensor/data"
USERNAME = "esp32"          # same credential you created
PASSWORD = "Manohar18@"   # same one used in ESP32 code

def on_connect(client, userdata, flags, rc):
    print("Connected to HiveMQ with result code", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received:", data)
    socketio.emit("sensor_data", data)  # push to browser

def start_mqtt():
    client = mqtt.Client()
    client.username_pw_set(USERNAME, PASSWORD)
    client.tls_set(cert_reqs=ssl.CERT_NONE)  # matches setInsecure() on ESP32 side
    client.tls_insecure_set(True)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT)
    client.loop_start()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    start_mqtt()
    socketio.run(app, debug=True)