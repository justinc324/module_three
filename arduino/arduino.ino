#include <WiFi.h>
#include <WebServer.h>
#include <WiFiUdp.h>
// #include <OSCMessage.h>


/* Put your SSID & Password */
const char* ssid = "ESP32_jcong";  // Enter SSID here
const char* password = "spookyseason";  //Enter Password here


/* Put IP Address details */
IPAddress local_ip(192,168,1,1);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

WebServer server(80);

WiFiUDP udp;

// light stuff
#define flexSensor 34
#define Switch 17
int lightInit;  // initial value
int lightVal;   // light reading
const char* message = "DEFAULT";
int flex;
char* modes[] = {"ONE", "TWO", "THREE"};

void setup() {
  pinMode(flexSensor, INPUT);
  pinMode(Switch, INPUT_PULLUP);

  WiFi.softAP(ssid, password);
  WiFi.softAPConfig(local_ip, gateway, subnet);
  
    server.begin();

}

int switch_state;

int mode = 0;
int prev_state = digitalRead(Switch);

void loop(){
  
  switch_state = digitalRead(Switch);
  flex = analogRead(flexSensor);
  
  if (switch_state == LOW && switch_state != prev_state) {
    
    mode = (mode + 1) % 3;
    udp.beginPacket("192.168.1.2",57222);
    udp.printf("%i", mode);
    udp.endPacket();
 
    prev_state = LOW;
  }

  else if (switch_state == HIGH && switch_state != prev_state) {
    
    mode = (mode + 1) % 3;
    udp.beginPacket("192.168.1.2",57222);
    udp.printf("%i", mode);
    udp.endPacket();
    
    prev_state = HIGH;
  }

  int message = -1;
  
  // low case (excluding 0)
  if ((flex < 1000) && (flex > 0)) {
    message = -2;
  }

   // med case
  else if ((flex > 1000) && (flex < 2000)) {
    message = -3;
  }

  else if ((flex > 2000) && (flex < 3000)) {
    message = -4;
  }

   // 3000 - 3300
   else if ((flex > 3000) && (flex < 3300)) {
      message = -5;
    }

    // 3300+
   else if (flex > 3300) {
      message = -6;
    }
   
    

   udp.beginPacket("192.168.1.2",57222);
   udp.printf("%i", message);
   udp.endPacket();
  
  //Wait for .75 second
  delay(750);
  
}
