#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

WiFiClient client;
HTTPClient http;

// please change savedSize as you change the size of savedNetworks[] accordingly
int savedSize = 7;
String savedNetworks[] = {"STUDBME1", "STUDBME2", "iot", "YME", "Miran", "CMP_LAB4", "CMP_LAB2"};

void connect_wifi()
{
  delay(100);
  char * username = "STUDBME2";
  char * password = "BME2Stud";
  Serial.print("Connecting to Wifi: ");
  Serial.println(username);
  WiFi.begin(username, password);

  uint8_t i = 0;
  while (WiFi.status() != WL_CONNECTED && i < 20)
  {
    Serial.print(".");
    delay(500);
    i++;
  }
  if (i > 20) {
    Serial.println("Couldn't connect to wifi");
  } else {
    Serial.print("Connected to WiFi network with IP Address: ");
    Serial.println(WiFi.localIP());
  }
}

void setup() {
  Serial.begin(115200);
  Serial.println("Connecting");
  connect_wifi();

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");

  Serial.println("Timer set to 5 seconds (timerDelay variable), it will take 5 seconds before publishing the first reading.");
}


void loop() {

  String networkNames[savedSize];
  int networkStrength[savedSize];

  //Check WiFi connection status
  if (WiFi.status() == WL_CONNECTED) {

    int foundNetworks = WiFi.scanNetworks();
    Serial.print("Number of found networks: ");
    Serial.println(foundNetworks);

    for (int i = 0; i < savedSize; i++) {
      bool found = false;
      for (int j = 0; j < foundNetworks; j++) {
        if (savedNetworks[i] == WiFi.SSID(j)) {
          networkNames[i] = WiFi.SSID(j);
          networkStrength[i] = WiFi.RSSI(j) + 100;
          found = true;
          break;
        }
      }
      if (!found) {
        networkNames[i] = savedNetworks[i];
        networkStrength[i] = 0;
      }
    }

    String urlString = "http://192.168.1.18:8090/data?";
    for (int i = 0; i < savedSize; i++) {
      urlString += networkNames[i] + "=" + networkStrength[i] + "&";
    }

    Serial.print("Requesting: ");
    Serial.println(urlString);

    // url format:
    // "http://192.168.1.18:8090/data?STUDBME1=12&STUDBME2=10&iot=13&YME=9";

    http.begin(client, urlString.c_str());
    // Your Domain name with URL path or IP address with path
    int httpResponseCode = http.GET();
    String payload = http.getString();
    Serial.println(payload);
    // Free resources
    http.end();
  }
  else
  {
    Serial.println("WiFi Disconnected");
  }
  delay(5000);
}