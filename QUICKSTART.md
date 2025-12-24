# 🎵 Quick Reference - Suno Music AI Lab

Guía rápida para contribuyentes y usuarios del repositorio.

## 🚀 Inicio rápido

```bash
# Clonar repo
git clone https://github.com/Blackmvmba88/suno.git
cd suno

# Setup (opcional, solo si usas tools)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Explorar
ls prompts/examples/     # Ver prompts de ejemplo
ls lyrics/examples/      # Ver letras de ejemplo
ls experiments/          # Ver experimentos documentados
```

## 📁 Estructura rápida

```
prompts/       → Prompts para generación musical
lyrics/        → Letras de canciones
metadata/      → Info estructurada (BPM, mood, etc)
experiments/   → Documentación de experimentos
tools/         → Scripts Python para validación
```

## 🎯 Tareas comunes

### Agregar un prompt nuevo

```bash
# Copiar template
cp prompts/templates/prompt-template.yaml prompts/mi-prompt.yaml

# Editar y completar campos
# Commit
git add prompts/mi-prompt.yaml
git commit -m "feat: Add [nombre] prompt"
```

### Agregar metadata de track

```bash
# Copiar ejemplo
cp metadata/tracks/example-track.yaml metadata/tracks/mi-track.yaml

# Editar campos requeridos
# Validar
python tools/validate_metadata.py metadata/tracks/mi-track.yaml

# Si válido, commit
git add metadata/tracks/mi-track.yaml
git commit -m "feat: Add metadata for [track]"
```

### Documentar experimento

```bash
# Crear directorio
mkdir experiments/mi-experimento

# Copiar template
cp experiments/templates/experiment-template.md \
   experiments/mi-experimento/README.md

# Documentar proceso y resultados
# Commit
git add experiments/mi-experimento/
git commit -m "experiment: [nombre del experimento]"
```

### Buscar tracks

```bash
# Por género
python tools/search_metadata.py --genre synthwave

# Por BPM
python tools/search_metadata.py --bpm 110-120

# Por mood
python tools/search_metadata.py --mood nostalgic

# Combinado
python tools/search_metadata.py --genre electronic --bpm 100-115
```

## 🎨 Guías de estilo

### Nombres de archivos
- `kebab-case-nombre.yaml` ✅
- `CamelCaseNombre.yaml` ❌
- Descriptivo pero conciso
- Fecha si relevante: `2024-12-experimento.md`

### Commits
```
feat: Add nueva funcionalidad
fix: Corregir algo
docs: Actualizar documentación
experiment: Nuevo experimento
```

### Metadata requerida
```yaml
track_id: "unique-id"
title: "Título"
creation_date: "YYYY-MM-DD"
musical:
  genre: "Genre"
  bpm: 120
```

## 🔧 Herramientas

```bash
# Validar metadata
python tools/validate_metadata.py metadata/

# Generar índice
python tools/generate_index.py

# Buscar tracks
python tools/search_metadata.py --genre [genre]
```

## 📚 Templates

- **Prompt**: `prompts/templates/prompt-template.yaml`
- **Metadata**: `metadata/tracks/example-track.yaml`
- **Experimento**: `experiments/templates/experiment-template.md`
- **Lyrics**: Ver `lyrics/examples/neon-dreams.md`

## 💡 Tips

### Para prompts efectivos
- Sé específico con BPM y genre
- Menciona instrumentación clave
- Incluye referencias de artistas/tracks
- Documenta qué funciona y qué no

### Para metadata completa
- Completa todos los campos requeridos
- Valida antes de commit
- Sé consistente con términos
- Usa tags descriptivos

### Para experimentos útiles
- Define hipótesis clara
- Documenta método replicable
- Incluye resultados con evidencia
- Extrae aprendizajes específicos

## ⚠️ NO commitear

- ❌ Archivos de audio (`.mp3`, `.wav`, etc)
- ❌ API keys o secrets
- ❌ Archivos temporales
- ❌ Dependencias (`node_modules/`, `.venv/`)
- ✅ Usar `.gitignore`

## 🆘 Problemas comunes

### "Metadata validation failed"
→ Revisar campos requeridos en `metadata/schema.yaml`
→ Verificar tipos de datos (int vs string)
→ Validar rangos (BPM 20-300, ratings 1-10)

### "YAML parsing error"
→ Verificar indentación (spaces, no tabs)
→ Verificar sintaxis YAML válida
→ Usar editor con syntax highlighting

### "Permission denied" en tools
→ `chmod +x tools/*.py`

## 📖 Más información

- **README.md**: Visión general del proyecto
- **CONTRIBUTING.md**: Guía completa de contribución
- **[directorio]/README.md**: Docs específicas por área

## 🤝 Ayuda

¿Preguntas? ¿Ideas?
→ Abrir Issue en GitHub
→ Consultar documentación en cada directorio
→ Ver ejemplos existentes

---

**Pro tip**: Empieza explorando `prompts/examples/` y `experiments/`
para entender el estilo y formato antes de contribuir. 🎵
