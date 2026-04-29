#!/usr/bin/env bash
set -euo pipefail

# Script base para ejecutar un prototipo mínimo local.
# Adáptalo según el lenguaje elegido por el estudiante.

echo "[INFO] Iniciando script de ejecución local..."

if [[ -f "src/main.py" ]]; then
  echo "[INFO] Detectado: src/main.py"
  echo "[INFO] Ejecutando prototipo en Python..."
  python3 src/main.py
  exit 0
fi

if [[ -f "src/main.c" ]]; then
  echo "[INFO] Detectado: src/main.c"
  echo "[INFO] Compila y ejecuta manualmente, por ejemplo:"
  echo "       gcc -Wall -Wextra -O2 src/main.c -o main && ./main"
  exit 0
fi

if [[ -f "src/main.sh" ]]; then
  echo "[INFO] Detectado: src/main.sh"
  echo "[INFO] Ejecuta manualmente, por ejemplo:"
  echo "       bash src/main.sh"
  exit 0
fi

if [[ -f "src/main.s" ]] || [[ -f "src/main.S" ]]; then
  echo "[INFO] Detectado archivo Assembly en src/."
  echo "[INFO] Usa comandos de ensamblado/enlace según tu entorno ARM64."
  exit 0
fi

echo "[ERROR] No se encontró archivo principal en src/."
echo "[ERROR] Esperado: main.py, main.c, main.sh, main.s o main.S"
exit 1
