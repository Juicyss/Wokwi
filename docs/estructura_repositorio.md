# Guía de Estructura del Repositorio

## Árbol de directorios recomendado

```text
nombre-del-proyecto/
├── README.md
├── docs/
│   ├── propuesta.md
│   ├── caso_de_uso.md
│   ├── estructura_repositorio.md
│   └── plan_de_pruebas.md
├── src/
│   └── main.<ext>
├── scripts/
│   └── run.sh
└── tests/
    └── test_plan.md
```

## Explicación de cada carpeta
- `docs/`: documentación principal (propuesta, caso de uso, estructura y plan de pruebas).
- `src/`: código fuente principal del prototipo mínimo.
- `scripts/`: scripts de apoyo para ejecución local.
- `tests/`: evidencia y checklist de pruebas manuales.

## Explicación de cada archivo
- `README.md`: instrucciones generales de la actividad y criterios de evaluación.
- `docs/propuesta.md`: definición del problema, alcance y criterios de éxito.
- `docs/caso_de_uso.md`: descripción detallada del flujo de uso.
- `docs/estructura_repositorio.md`: guía de organización del proyecto.
- `docs/plan_de_pruebas.md`: diseño de casos de prueba.
- `src/main.<ext>`: punto de entrada del prototipo.
- `scripts/run.sh`: script para ejecutar o guiar la ejecución.
- `tests/test_plan.md`: checklist final de validación.

## Reglas para nombrar archivos
1. Usa minúsculas.
2. Usa guion bajo para separar palabras (`caso_de_uso.md`).
3. Evita espacios y caracteres especiales.
4. Mantén nombres cortos y descriptivos.

## Reglas para evitar desorden
1. No mezclar documentación con código dentro de `src/`.
2. No crear carpetas extras sin justificación.
3. Mantener un solo archivo principal en `src/` para esta práctica.
4. Eliminar archivos temporales antes de entregar.
5. Registrar cambios de alcance en la documentación.

## Nota de tamaño y complejidad
Mantén pocos archivos y funciones pequeñas. Esta práctica evalúa planeación y claridad técnica, no volumen de código.
