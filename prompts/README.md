# 🎵 Prompts Musicales

Este directorio contiene **prompts curados** para generación musical con IA.

## 📋 Estructura

```
prompts/
├── README.md           # Este archivo
├── templates/          # Plantillas reutilizables
├── genres/            # Prompts organizados por género
├── moods/             # Prompts organizados por mood/emoción
└── experiments/       # Prompts experimentales
```

## 🎯 Cómo usar un prompt

1. **Selecciona** un prompt base del directorio correspondiente
2. **Personaliza** los parámetros según tu necesidad
3. **Documenta** el resultado en `/experiments`
4. **Itera** y refina basándote en lo que funciona

## ✍️ Anatomía de un buen prompt

Un prompt musical efectivo incluye:

- **Género/Estilo**: Rock, Jazz, Electronic, etc.
- **Mood/Emoción**: Energético, melancólico, épico
- **Tempo/BPM**: Indicación de velocidad
- **Instrumentación**: Instrumentos específicos
- **Estructura**: Intro, verso, coro, bridge, etc.
- **Referencias**: Artistas o canciones como inspiración

## 📝 Formato recomendado

```yaml
# prompt-name.yaml
title: "Nombre del Prompt"
genre: "Electronic/Synthwave"
mood: "Nostálgico, atmosférico"
tempo: "100-110 BPM"
structure: "Intro → Verse → Chorus → Bridge → Outro"
instruments:
  - Synths analógicos
  - Pads atmosféricos
  - Drums electrónicos
description: >
  [Tu prompt detallado aquí]

notes: >
  Observaciones sobre qué funciona y qué no
```

## 🎨 Ejemplos rápidos

### Synthwave Nostálgico
```
Synthwave track, 105 BPM, nostalgic and atmospheric, analog synths,
warm pads, punchy electronic drums, driving bassline, 80s aesthetic,
cinematic feel
```

### Rock Energético
```
High-energy rock anthem, 140 BPM, powerful electric guitars,
driving drums, anthemic chorus, raw vocals, stadium rock vibes
```

### Ambient Relajante
```
Ambient soundscape, 60 BPM, ethereal pads, subtle textures,
gentle piano, natural reverb, peaceful and meditative, no drums
```

## 🧪 Experimentación

Prueba variaciones de:
- **Intensidad**: Subtle → Intense
- **Complejidad**: Simple → Layered
- **Influencias**: Mezcla géneros inesperados
- **Duración**: Short loop → Extended composition

## 📊 Tracking

Mantén un registro de tus experimentos en `/experiments` con:
- Prompt usado
- Resultados obtenidos
- Calificación (1-5)
- Aprendizajes

---

**Tip**: Los mejores prompts son específicos pero flexibles.
Demasiado rígido → poca variación. Demasiado vago → resultados inconsistentes.
