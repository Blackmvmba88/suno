# 📊 Metadata Musical

Información estructurada sobre composiciones: BPM, tonalidad, mood, tags y metadatos técnicos.

## 🎯 Propósito

La metadata bien organizada permite:
- **Búsqueda** eficiente de composiciones
- **Filtrado** por características musicales
- **Análisis** de patrones y tendencias
- **Organización** sistemática del catálogo
- **Integración** con herramientas de producción

## 📁 Estructura

```
metadata/
├── README.md          # Este archivo
├── schema.yaml        # Schema de metadatos
├── tracks/            # Metadata por track
└── collections/       # Metadata de álbumes/playlists
```

## 📋 Schema estándar

```yaml
# metadata/tracks/example-track.yaml
track_id: "track-001"
title: "Nombre de la Canción"
artist: "Artista/Proyecto"
creation_date: "2024-12-24"

# Información musical
musical:
  genre: "Electronic/Synthwave"
  subgenre: "Dreamwave"
  bpm: 110
  key: "C Minor"
  time_signature: "4/4"
  duration_seconds: 180

# Mood y energía
mood:
  primary: "Nostálgico"
  secondary: "Atmosférico"
  energy_level: 6  # 1-10
  danceability: 7  # 1-10
  emotional_valence: 5  # 1-10 (triste-feliz)

# Composición
composition:
  structure: ["Intro", "Verse", "Chorus", "Verse", "Chorus", "Bridge", "Outro"]
  has_vocals: true
  vocal_type: "Synthetic/AI"
  language: "es"

# Producción
production:
  instruments:
    - "Analog Synths"
    - "Electric Bass"
    - "Electronic Drums"
    - "Atmospheric Pads"
  effects:
    - "Reverb"
    - "Delay"
    - "Chorus"
  mixing_style: "Spacious, warm"

# Generación
generation:
  method: "AI-assisted"  # AI-full, AI-assisted, Human
  ai_model: "Suno v3"
  prompt_version: "v1.2"
  seed: 42
  iterations: 3

# Tags y clasificación
tags:
  - "synthwave"
  - "nostalgic"
  - "retro"
  - "80s"
  - "cinematic"

# Uso y derechos
usage:
  license: "Personal/Commercial"
  copyright: "© 2024 [Owner]"
  can_remix: true
  can_distribute: true

# Referencias y similares
references:
  inspired_by:
    - "Kavinsky - Nightcall"
    - "The Midnight - Sunset"
  similar_tracks:
    - "track-002"
    - "track-005"

# Notas
notes: >
  Notas adicionales sobre el proceso creativo,
  decisiones de producción, o cualquier observación relevante.

# Archivos relacionados
files:
  audio: "audio/track-001.mp3"
  lyrics: "lyrics/generated/track-001.md"
  prompt: "prompts/synthwave/nostalgic-drive.yaml"
  cover_art: "assets/covers/track-001.png"
```

## 🔧 Herramientas

### Validación de schema
```bash
python tools/validate_metadata.py metadata/tracks/mi-track.yaml
```

### Generación de índice
```bash
python tools/generate_index.py --output metadata/index.json
```

### Búsqueda
```bash
# Buscar tracks por BPM
python tools/search_metadata.py --bpm 110-120

# Buscar por mood
python tools/search_metadata.py --mood nostalgic

# Buscar por género
python tools/search_metadata.py --genre synthwave
```

## 📊 Categorías de clasificación

### Género (genre)
- Electronic, Rock, Pop, Jazz, Hip-Hop, Classical, Ambient, etc.

### Subgénero (subgenre)
- Más específico: Synthwave, Shoegaze, Lo-fi, etc.

### Mood (estado emocional)
- Energético, Melancólico, Épico, Relajante, Oscuro, Luminoso, etc.

### Energy Level (1-10)
- 1-3: Muy calmado, ambiente
- 4-6: Moderado
- 7-9: Alto, energético
- 10: Intenso, frenético

### Danceability (1-10)
- 1-3: No bailable
- 4-6: Algo bailable
- 7-9: Muy bailable
- 10: Orientado a danza

### Emotional Valence (1-10)
- 1-3: Muy triste/oscuro
- 4-6: Neutral/mixto
- 7-9: Positivo/luminoso
- 10: Muy alegre/eufórico

## 🎨 Casos de uso

### Playlist automática
Agrupar tracks con metadata similar para crear playlists cohesivas.

### Análisis de patrones
Identificar qué combinaciones de BPM + mood + género funcionan mejor.

### Recomendaciones
Sugerir tracks similares basados en metadata.

### Productividad
Filtrar música por contexto de uso (focus, workout, chill, etc.).

## 🔄 Workflow

1. **Crear track** (generado o grabado)
2. **Analizar** características musicales
3. **Completar metadata** usando el template
4. **Validar** con herramienta de validación
5. **Indexar** para búsqueda
6. **Actualizar** si es necesario

## 📝 Best practices

- **Consistencia**: Usa los mismos términos para categorías similares
- **Precisión**: BPM y key deben ser exactos
- **Completitud**: Llena todos los campos relevantes
- **Actualización**: Mantén sincronizado con cambios en el track
- **Versionado**: Trackea cambios en metadata importante

## 🤖 Extracción automática

Para audio existente, puedes extraer automáticamente:
- **BPM**: Con librosa o essentia
- **Key**: Con algoritmos de detección de tonalidad
- **Estructura**: Con análisis de segmentación
- **Features**: Con modelos de MIR (Music Information Retrieval)

---

**Pro tip**: La metadata es tan importante como la música misma.
Invertir tiempo en documentarla bien paga dividendos a largo plazo.
