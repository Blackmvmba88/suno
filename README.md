# suno

Initial baseline commit created by automation

## Monitor de errores (ligero)

Se incluye un monitor simple en `scripts/monitor_errors.py`. Uso rápido:

- Instala dependencias: `python -m pip install -r backend/requirements.txt`
- Ejecuta: `ERROR_MONITOR_WEBHOOK=https://hooks.example.com/endpoint python scripts/monitor_errors.py`

El monitor:
- Comprueba `/api/health` y hace un POST con una imagen de prueba a `/api/ocr`.
- En caso de fallo, imprime un JSON con `issues` y, si `ERROR_MONITOR_WEBHOOK` está configurado, hace POST del payload a ese endpoint.

Nota: para producción use Sentry/Prometheus/Alertmanager en lugar de este script de ejemplo.
