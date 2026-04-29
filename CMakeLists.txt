cmake_minimum_required(VERSION 3.13)
project(pico_keypad_leds C CXX ASM)

# Plantilla documental para Pico SDK.
# Mantiene el proyecto listo para integrar cuando exista una versión compatible de Keypad.

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Requiere exportar PICO_SDK_PATH en entorno real.
include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)
pico_sdk_init()

add_executable(pico_keypad_leds
  src/main.cpp
)

# Dependencias básicas (ajustar si se porta Keypad a SDK puro)
target_link_libraries(pico_keypad_leds pico_stdlib)

pico_add_extra_outputs(pico_keypad_leds)
