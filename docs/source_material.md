# Material fuente (copiado en bloques de comillas)

## Código fuente proporcionado (C/C++)
```cpp
#include <Keypad.h>

const uint8_t LEDS = 12;
const uint8_t ROWS = 4;
const uint8_t COLS = 4;

char keys[ROWS][COLS] = {
  { '1', '2', '3', 'A' },
  { '4', '5', '6', 'B' },
  { '7', '8', '9', 'C' },
  { '*', '0', '#', 'D' }
};

// Pins connected to LED1, LED2, LED3, ...LED12
uint8_t ledPins[LEDS] = { 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 28, 27 };
uint8_t rowPins[ROWS] = { 26, 22, 21, 20 }; // Pins connected to R1, R2, R3, R4
uint8_t colPins[COLS] = { 19, 18, 17, 16 }; // Pins connected to C1, C2, C3, C4

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  for (uint8_t l = 0; l < LEDS; l++) {
    pinMode(ledPins[l], OUTPUT);
    digitalWrite(ledPins[l], LOW);
  }
}

void loop() {
  char key = keypad.getKey();

  if (key != NO_KEY) {
    switch (key) {
      case '1': digitalWrite(ledPins[0], HIGH);
        break;
      case '2': digitalWrite(ledPins[1], HIGH);
        break;
      case '3': digitalWrite(ledPins[2], HIGH);
        break;
      case '4': digitalWrite(ledPins[3], HIGH);
        break;
      case '5': digitalWrite(ledPins[4], HIGH);
        break;
      case '6': digitalWrite(ledPins[5], HIGH);
        break;
      case '7': digitalWrite(ledPins[6], HIGH);
        break;
      case '8': digitalWrite(ledPins[7], HIGH);
        break;
      case '9':
        for (uint8_t l = 0; l < 8; l++) {
          digitalWrite(ledPins[l], HIGH);
        }
        break;
      case '0':
        for (uint8_t l = 0; l < 8; l++) {
          digitalWrite(ledPins[l], LOW);
        }
        break;
      case 'A': digitalWrite(ledPins[8], HIGH);
        break;
      case 'B': digitalWrite(ledPins[9], HIGH);
        break;
      case 'C': digitalWrite(ledPins[10], HIGH);
        break;
      case 'D': digitalWrite(ledPins[11], HIGH);
        break;
      case '*':
        for (uint8_t l = 8; l < 12; l++) {
          digitalWrite(ledPins[l], HIGH);
        }
        break;
      case '#':
        for (uint8_t l = 8; l < 12; l++) {
          digitalWrite(ledPins[l], LOW);
        }
        break;
    }
  }

  delay(10);
}
```

## `diagram.json` proporcionado (Wokwi)
```json
{
  "version": 1,
  "author": "Anderson Costa",
  "editor": "wokwi",
  "parts": [
    { "type": "wokwi-pi-pico", "id": "pico", "top": 118, "left": 348, "rotate": 90, "attrs": {} },
    {
      "type": "wokwi-resistor",
      "id": "rp1",
      "top": 349.55,
      "left": 19.2,
      "attrs": { "value": "1000" }
    }
  ],
  "connections": [
    [ "pico:GP0", "$serialMonitor:RX", "", [] ],
    [ "pico:GP1", "$serialMonitor:TX", "", [] ],
    [ "keypad1:C4", "pico:GP16", "green", [ "v15", "h132" ] ]
  ],
  "dependencies": {}
}
```

> Nota: por legibilidad, se muestra una versión recortada del JSON. Usa el JSON completo que proporcionaste en la consigna para reproducir el diagrama exacto en Wokwi.
