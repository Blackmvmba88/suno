# 🛠️ Tools

Herramientas de Python para gestión y validación del repositorio.

## 📋 Herramientas disponibles

### validate_metadata.py

Valida archivos YAML de metadata contra el schema definido.

**Uso**:
```bash
# Validar un archivo
python tools/validate_metadata.py metadata/tracks/mi-track.yaml

# Validar todos los archivos en un directorio
python tools/validate_metadata.py metadata/tracks/

# Validar todo el directorio metadata
python tools/validate_metadata.py metadata/
```

**Qué valida**:
- ✅ Campos requeridos presentes
- ✅ Tipos de datos correctos
- ✅ Rangos válidos (BPM 20-300, ratings 1-10)
- ⚠️ Campos recomendados faltantes (warnings)

**Output**:
```
✅ example-track.yaml: VALID
   ⚠️  Recommended field missing: mood.energy_level

❌ bad-track.yaml: INVALID
   ❌ Missing required field: track_id
   ❌ Field musical.bpm has incorrect type. Expected int, got str
```

### generate_index.py

Genera un índice JSON de todos los tracks para búsqueda rápida.

**Uso**:
```bash
# Generar índice en ubicación por defecto
python tools/generate_index.py

# Especificar output
python tools/generate_index.py --output metadata/index.json

# Especificar directorio de metadata
python tools/generate_index.py --metadata-dir metadata/ --output index.json
```

**Output**: Archivo JSON con:
- Lista de todos los tracks con campos clave
- Listas agregadas de géneros, moods, artistas
- Total de tracks indexados

### search_metadata.py

Busca tracks por diferentes criterios.

**Uso**:
```bash
# Buscar por género
python tools/search_metadata.py --genre synthwave

# Buscar por BPM exacto (±5 de tolerancia)
python tools/search_metadata.py --bpm 110

# Buscar por rango de BPM
python tools/search_metadata.py --bpm 110-120

# Buscar por mood
python tools/search_metadata.py --mood nostalgic

# Buscar por artista
python tools/search_metadata.py --artist "Suno Lab"

# Buscar por tag
python tools/search_metadata.py --tag retro

# Combinar filtros
python tools/search_metadata.py --genre electronic --bpm 110-120 --mood energetic

# Limitar resultados
python tools/search_metadata.py --genre rock --limit 5
```

**Output**:
```
🎵 Neon Dreams - Suno Lab
   Genre: Electronic | BPM: 110 | Key: C Minor | Mood: Nostálgico
   📁 metadata/tracks/example-track.yaml
```

## 🔧 Instalación

```bash
# Crear entorno virtual
python3 -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## 🚀 Integración con CI/CD

Ver `.github/workflows/validate.yml` para validación automática en cada push/PR.

## 💡 Futuras herramientas

Ideas para expansión:
- [ ] **export_playlist.py**: Exportar a formato M3U/PLS
- [ ] **analyze_patterns.py**: Análisis estadístico de metadata
- [ ] **suggest_similar.py**: Recomendar tracks similares
- [ ] **bulk_edit.py**: Edición masiva de metadata
- [ ] **audio_analyzer.py**: Extraer BPM/key automáticamente
- [ ] **prompt_optimizer.py**: Analizar qué prompts funcionan mejor
- [ ] **experiment_tracker.py**: Dashboard de experimentos

## 📝 Añadir nueva herramienta

1. Crea el script en `tools/`
2. Incluye docstring y `--help`
3. Maneja errores gracefully
4. Actualiza `requirements.txt` si es necesario
5. Documenta en este README
6. Haz executable: `chmod +x tools/nueva-herramienta.py`

## 🤝 Contribuir

¿Tienes idea para una herramienta útil? ¡Crea un PR!

Ver `CONTRIBUTING.md` para más detalles.
