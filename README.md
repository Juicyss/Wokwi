# Pico W + Teclado 4x4 + 12 LEDs (Wokwi)

Proyecto de documentación y organización de firmware para **Raspberry Pi Pico W (RP2040)** basado en un ejemplo de Wokwi.

## Resumen
Este repositorio conserva la lógica original del programa (sin cambios de comportamiento):
- Lee un teclado matricial 4x4.
- Enciende/apaga 12 LEDs según la tecla presionada.
- Mapea teclas numéricas (`0-9`) y especiales (`A-D`, `*`, `#`) a salidas GPIO.

## Estructura propuesta (C/C++ Pico SDK)
```text
.
├── CMakeLists.txt
├── src/
│   └── main.cpp
├── include/
├── docs/
│   ├── architecture.md
│   ├── wiring.md
│   └── source_material.md
└── README.md
```

## Componentes (derivados de `diagram.json`)
- 1x Raspberry Pi Pico / Pico W (en Wokwi aparece `wokwi-pi-pico`)
- 1x Teclado de membrana 4x4
- 12x LED (8 azules + 4 rojos)
- 12x Resistencias de 220 Ω (serie de LEDs)
- 4x Resistencias de 1 kΩ (pull-up para filas del teclado)
- Cableado a GND y 3V3

## Mapa de GPIO principal
- **Teclado columnas:** GP16, GP17, GP18, GP19
- **Teclado filas:** GP26, GP22, GP21, GP20
- **LEDs (12):** GP11, GP10, GP9, GP8, GP7, GP6, GP5, GP4, GP3, GP2, GP28, GP27

Detalle completo en `docs/wiring.md`.

## Ejecutar en Wokwi
1. Crea un proyecto nuevo de Raspberry Pi Pico/Pico W.
2. Copia `src/main.cpp` en el archivo de código del proyecto.
3. Copia el JSON de `docs/source_material.md` (bloque `diagram.json`) al diagrama del proyecto.
4. Inicia simulación y prueba teclas del keypad.

## Ejecutar en hardware real (Pico W)
> Nota: el código original usa `Keypad.h` estilo Arduino. Para hardware real con Pico SDK puro se requiere portar la librería o adaptar escaneo de matriz manual. Este repo **documenta** y conserva la lógica original sin alterarla.

Flujo sugerido:
1. Implementar/portar capa `Keypad` compatible con RP2040.
2. Compilar con toolchain ARM y Pico SDK.
3. Flashear UF2 al Pico W por USB BOOTSEL.

## Wi-Fi y credenciales
Este proyecto no usa Wi-Fi en la lógica actual. Si se agrega conectividad después:
- No subir SSID/contraseñas al repo.
- Usar archivo local ignorado por git (`secrets.h` o similar).
- Documentar solo variables y formato, no valores reales.
