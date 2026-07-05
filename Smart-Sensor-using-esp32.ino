#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11

const char* ssid = "ESP";        //that one your pc wi-fi name
const char* password = "darkking";   //that one your wi-fi password

const char* mqtt_server   = "a4a03546a8184ee38c68c7e42a5d9302.s1.eu.hivemq.cloud";
const int   mqtt_port     = 8883;
const char* mqtt_username = "esp32";      // that one you created
const char* mqtt_password = "Manohar18@"; // that one you created

WiFiClientSecure espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");

  espClient.setInsecure(); // skips certificate validation (fine for student projects)
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32Client", mqtt_username, mqtt_password)) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.println(client.state());
      delay(2000);
      return;
    }
  }
  client.loop();

  float temp = dht.readTemperature();
  float hum  = dht.readHumidity();

  String payload = "{\"temp\":" + String(temp) + ",\"hum\":" + String(hum) + "}";
  client.publish("iot/sensor/data", payload.c_str());
  Serial.println(payload);

  delay(3000);
}
