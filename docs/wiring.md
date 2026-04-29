# Cableado y uso de GPIO (Pico W)

## Descripción breve del diagrama
El diagrama muestra un **Raspberry Pi Pico/Pico W** conectado a un **keypad de membrana 4x4** y **12 LEDs**. Cada LED tiene su resistencia serie de 220 Ω hacia un GPIO del Pico, y todos los cátodos regresan a GND. Las filas del keypad tienen resistencias de 1 kΩ hacia 3V3 como pull-up.

## Tabla de mapeo GPIO

### Teclado 4x4
| Señal keypad | GPIO Pico |
|---|---|
| C4 | GP16 |
| C3 | GP17 |
| C2 | GP18 |
| C1 | GP19 |
| R4 | GP20 |
| R3 | GP21 |
| R2 | GP22 |
| R1 | GP26 |

### LEDs
| LED lógico | GPIO |
|---|---|
| ledPins[0]  | GP11 |
| ledPins[1]  | GP10 |
| ledPins[2]  | GP9  |
| ledPins[3]  | GP8  |
| ledPins[4]  | GP7  |
| ledPins[5]  | GP6  |
| ledPins[6]  | GP5  |
| ledPins[7]  | GP4  |
| ledPins[8]  | GP3  |
| ledPins[9]  | GP2  |
| ledPins[10] | GP28 |
| ledPins[11] | GP27 |

## Notas eléctricas
- Resistencias de LED: 220 Ω.
- Pull-up de filas keypad: 1 kΩ a 3V3 (según diagrama proporcionado).
- GND común entre todos los componentes.

## Suposiciones documentadas
- El diagrama usa `wokwi-pi-pico`; el objetivo académico es Pico W (RP2040). El mapeo GPIO es equivalente para esta práctica.
