#include <Arduino.h>

// Controlador PI ilustrativo para o primeiro ensaio HIL.
// Protocolo de entrada:  MEAS,<sequencia>,<medicao>,<periodo_s>\n
// Protocolo de saida:    CTRL,<sequencia>,<controle>,<tempo_us>\n
constexpr float KP = 1.2f;
constexpr float KI = 8.0f;
constexpr float SETPOINT = 1.0f;
constexpr float U_MIN = 0.0f;
constexpr float U_MAX = 3.3f;

float integral = 0.0f;
String line;

void setup() {
  Serial.begin(921600);
  line.reserve(96);
  Serial.println("READY,ESP32_HIL_BASE,VARIABLE_DT");
}

void processMeasurement(const String &message) {
  unsigned long sequence = 0;
  float measurement = 0.0f;
  float sampleTimeS = 0.0f;
  if (sscanf(message.c_str(), "MEAS,%lu,%f,%f", &sequence, &measurement,
             &sampleTimeS) != 3) {
    Serial.println("ERR,FORMAT");
    return;
  }
  if (sampleTimeS < 0.0001f || sampleTimeS > 0.1f) {
    Serial.println("ERR,DT");
    return;
  }

  const float error = SETPOINT - measurement;
  integral += KI * sampleTimeS * error;
  integral = constrain(integral, U_MIN, U_MAX);
  const float control = constrain(KP * error + integral, U_MIN, U_MAX);

  Serial.printf("CTRL,%lu,%.6f,%lu\n", sequence, control, micros());
}

void loop() {
  while (Serial.available() > 0) {
    const char value = static_cast<char>(Serial.read());
    if (value == '\n') {
      line.trim();
      if (line.startsWith("MEAS,")) {
        processMeasurement(line);
      } else if (line == "PING") {
        Serial.printf("PONG,%lu\n", micros());
      } else if (line == "RESET") {
        integral = 0.0f;
        Serial.println("RESET,OK");
      } else if (!line.isEmpty()) {
        Serial.println("ERR,COMMAND");
      }
      line = "";
    } else if (value != '\r' && line.length() < 95) {
      line += value;
    }
  }
}

