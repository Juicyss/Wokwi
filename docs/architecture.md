# Arquitectura del firmware

## Objetivo funcional
Interpretar teclas de un keypad 4x4 y controlar 12 LEDs con reglas simples por tecla.

## Estructura del código
- `setup()`:
  - Configura 12 GPIO como salida.
  - Inicializa todos los LEDs en `LOW`.
- `loop()`:
  - Lee una tecla con `keypad.getKey()`.
  - Si hay tecla válida (`!= NO_KEY`), ejecuta un `switch`.
  - Cada caso enciende/apaga LED(s) específicos.
  - Espera `delay(10)` ms.

## Reglas de negocio (sin alterar lógica)
- Teclas `1..8`: encienden LED individual `ledPins[0..7]`.
- Tecla `9`: enciende bloque `ledPins[0..7]`.
- Tecla `0`: apaga bloque `ledPins[0..7]`.
- Teclas `A..D`: encienden `ledPins[8..11]` individualmente.
- Tecla `*`: enciende bloque `ledPins[8..11]`.
- Tecla `#`: apaga bloque `ledPins[8..11]`.

## Módulos/librerías
- `Keypad.h`: lectura de keypad matricial.
- API tipo Arduino: `pinMode`, `digitalWrite`, `delay`.

## Riesgos técnicos conocidos
- En Pico SDK puro, `Keypad.h` y funciones Arduino no están disponibles por defecto.
- Para hardware real se requiere:
  1) capa de compatibilidad Arduino para RP2040, o
  2) portar `Keypad` y GPIO a SDK nativo.

Este repositorio prioriza documentación y preservación del comportamiento original.
