# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a Suno Experiments & Music AI Lab!

## 🎯 Filosofía del proyecto

Este es un **laboratorio experimental**, no un producto terminado. Valoramos:

- 🧪 **Experimentación** sobre perfección
- 📝 **Documentación** sobre código
- 🎨 **Creatividad** sobre convención
- 🔄 **Iteración** sobre planificación exhaustiva

## 📋 Cómo contribuir

### 1. Agregar un nuevo prompt

```bash
# Crea archivo basado en template
cp prompts/templates/prompt-template.yaml prompts/mi-nuevo-prompt.yaml

# Edita con tus detalles
# Commit y PR
```

**Checklist**:
- [ ] Incluye descripción clara del género/mood
- [ ] Especifica BPM y tempo aproximado
- [ ] Lista instrumentación clave
- [ ] Documenta para qué funciona mejor
- [ ] Incluye al menos un ejemplo de uso

### 2. Agregar letras

```bash
# Crea en el directorio apropiado
# generated/ - Generadas por IA
# hybrid/ - IA + edición humana
# original/ - Completamente humanas
```

**Formato**:
- Usa Markdown con metadata en header (YAML front matter)
- Marca claramente las secciones [Verse], [Chorus], etc.
- Indica idioma y autor/fuente

### 3. Agregar metadata de un track

```bash
# Usa el template
cp metadata/tracks/example-track.yaml metadata/tracks/mi-track.yaml

# Completa todos los campos relevantes
python tools/validate_metadata.py metadata/tracks/mi-track.yaml
```

**Importante**:
- Todos los campos requeridos deben estar completos
- BPM y key deben ser precisos
- Tags deben ser descriptivos y consistentes
- Valida antes de hacer commit

### 4. Documentar un experimento

```bash
# Crea directorio para tu experimento
mkdir experiments/mi-experimento

# Copia template
cp experiments/templates/experiment-template.md experiments/mi-experimento/README.md

# Documenta proceso, resultados y aprendizajes
```

**Incluye**:
- Hipótesis clara
- Método replicable
- Resultados con evidencia (archivos, links)
- Aprendizajes específicos
- Próximos pasos

### 5. Agregar herramientas

Si desarrollas un script útil:

```bash
# Agrega a tools/
tools/mi-herramienta.py

# Incluye:
# - Docstring claro
# - Help/usage
# - Manejo de errores
# - Actualiza requirements.txt si necesario
```

## 🎨 Estilo y convenciones

### Nombres de archivos
- Usa kebab-case: `mi-archivo-nombre.yaml`
- Se descriptivo pero conciso
- Incluye fecha si relevante: `2024-12-experimento.md`

### Commits
```
feat: Add synthwave prompt template
fix: Correct BPM in track metadata
docs: Update README with new workflow
experiment: Jazz fusion with electronic elements
```

Prefijos sugeridos:
- `feat`: Nueva funcionalidad
- `fix`: Corrección
- `docs`: Documentación
- `experiment`: Nuevo experimento
- `tool`: Nueva herramienta
- `refactor`: Reorganización

### Branches
- `main`: Rama principal estable
- `experiment/<nombre>`: Para experimentación activa
- `feat/<feature>`: Para nuevas funcionalidades
- `docs/<topic>`: Para documentación

## 📊 Calidad

### Para prompts
- [ ] Testeado al menos 2 veces
- [ ] Produce resultados consistentes
- [ ] Documentado con ejemplos
- [ ] Incluye notas sobre variaciones

### Para metadata
- [ ] Pasa validación (`validate_metadata.py`)
- [ ] Campos requeridos completos
- [ ] Tags apropiados y consistentes
- [ ] Vinculado a archivos relacionados

### Para experimentos
- [ ] Hipótesis clara y testeable
- [ ] Método replicable
- [ ] Resultados documentados
- [ ] Aprendizajes extraídos
- [ ] Próximos pasos definidos

### Para herramientas
- [ ] Código limpio y comentado
- [ ] Maneja errores gracefully
- [ ] Incluye help/usage
- [ ] No rompe herramientas existentes

## 🔄 Workflow típico

1. **Fork** el repo (o crea branch si tienes acceso)
2. **Crea** tu contenido/cambios
3. **Valida** con herramientas (`validate_metadata.py`, etc.)
4. **Documenta** en README o archivos apropiados
5. **Commit** con mensaje descriptivo
6. **Push** y crea Pull Request
7. **Describe** en el PR qué agrega y por qué es útil

## 🚫 Qué NO hacer

- ❌ No commitear archivos de audio grandes (usa `.gitignore`)
- ❌ No incluir API keys o secrets
- ❌ No romper estructura existente sin discutir
- ❌ No commitear sin validar metadata
- ❌ No agregar dependencias pesadas sin justificación
- ❌ No usar términos ofensivos o inapropiados

## 💡 Ideas de contribución

Si no sabes por dónde empezar:

- 📝 Crear templates para géneros populares
- 🎵 Documentar prompts que funcionan bien
- 🔧 Mejorar herramientas de validación
- 📊 Agregar análisis de patrones exitosos
- 🌍 Traducir documentación
- 🎨 Crear visualizaciones de metadata
- 🤖 Desarrollar scripts de automatización
- 📚 Expandir ejemplos y tutoriales

## 🎓 Recursos útiles

### Para aprender sobre prompts musicales
- Experimenta con diferentes niveles de detalle
- Prueba referencias a artistas específicos
- Combina géneros inesperados
- Documenta TODO, incluso fracasos

### Para metadata
- Usa herramientas de análisis de audio (librosa, essentia)
- Mantén consistencia en términos
- Más metadata = más fácil buscar después

### Para experimentación
- Define hipótesis antes de empezar
- Cambia una variable a la vez
- Documenta resultados inmediatamente
- Comparte aprendizajes

## ❓ ¿Preguntas?

Si tienes dudas o sugerencias:
- Abre un Issue para discusión
- Revisa Issues existentes por duplicados
- Sé específico y constructivo

## 📜 Código de conducta

- ✅ Sé respetuoso y constructivo
- ✅ Da crédito donde corresponde
- ✅ Ayuda a otros a aprender
- ✅ Acepta feedback con apertura
- ✅ Enfócate en el aprendizaje y la creatividad

---

**Recuerda**: Este es un espacio de experimentación y aprendizaje.
No hay contribución "mala", solo oportunidades de mejorar. 🚀
