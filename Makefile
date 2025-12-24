# Makefile for Suno Music AI Lab
# Comandos útiles para desarrollo y gestión del repositorio

.PHONY: help setup validate index search clean test

# Variables
PYTHON := python3
METADATA_DIR := metadata
TOOLS_DIR := tools

help: ## Mostrar esta ayuda
	@echo "Comandos disponibles:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

setup: ## Instalar dependencias de Python
	$(PYTHON) -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt
	@echo "✅ Entorno configurado. Activa con: source .venv/bin/activate"

validate: ## Validar todos los archivos de metadata
	$(PYTHON) $(TOOLS_DIR)/validate_metadata.py $(METADATA_DIR)/

validate-track: ## Validar un track específico (uso: make validate-track TRACK=path/to/track.yaml)
	@if [ -z "$(TRACK)" ]; then \
		echo "Error: Especifica TRACK=path/to/track.yaml"; \
		exit 1; \
	fi
	$(PYTHON) $(TOOLS_DIR)/validate_metadata.py $(TRACK)

index: ## Generar índice de búsqueda
	$(PYTHON) $(TOOLS_DIR)/generate_index.py --output $(METADATA_DIR)/index.json
	@echo "✅ Índice generado en $(METADATA_DIR)/index.json"

search-genre: ## Buscar por género (uso: make search-genre GENRE=synthwave)
	@if [ -z "$(GENRE)" ]; then \
		echo "Error: Especifica GENRE=nombre"; \
		exit 1; \
	fi
	$(PYTHON) $(TOOLS_DIR)/search_metadata.py --genre $(GENRE)

search-bpm: ## Buscar por BPM (uso: make search-bpm BPM=110-120)
	@if [ -z "$(BPM)" ]; then \
		echo "Error: Especifica BPM=valor o BPM=min-max"; \
		exit 1; \
	fi
	$(PYTHON) $(TOOLS_DIR)/search_metadata.py --bpm $(BPM)

search-mood: ## Buscar por mood (uso: make search-mood MOOD=nostalgic)
	@if [ -z "$(MOOD)" ]; then \
		echo "Error: Especifica MOOD=nombre"; \
		exit 1; \
	fi
	$(PYTHON) $(TOOLS_DIR)/search_metadata.py --mood $(MOOD)

list-prompts: ## Listar todos los prompts disponibles
	@echo "Prompts disponibles:"
	@find prompts/ -name "*.yaml" -type f | sort

list-experiments: ## Listar todos los experimentos
	@echo "Experimentos documentados:"
	@find experiments/ -name "*.md" -type f | grep -v templates | sort

stats: ## Mostrar estadísticas del repositorio
	@echo "📊 Estadísticas del repositorio:"
	@echo "  Prompts: $$(find prompts/ -name "*.yaml" -type f | wc -l)"
	@echo "  Tracks metadata: $$(find metadata/tracks/ -name "*.yaml" -type f | wc -l)"
	@echo "  Letras: $$(find lyrics/ -name "*.md" -type f | grep -v README | wc -l)"
	@echo "  Experimentos: $$(find experiments/ -name "*.md" -type f | grep -v templates | grep -v README | wc -l)"

clean: ## Limpiar archivos temporales
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*~" -delete
	find . -type f -name "*.tmp" -delete
	@echo "✅ Archivos temporales eliminados"

check: validate ## Alias para validate
	@echo "✅ Todas las validaciones pasaron"

new-prompt: ## Crear nuevo prompt desde template (uso: make new-prompt NAME=mi-prompt)
	@if [ -z "$(NAME)" ]; then \
		echo "Error: Especifica NAME=nombre-del-prompt"; \
		exit 1; \
	fi
	cp prompts/templates/prompt-template.yaml prompts/$(NAME).yaml
	@echo "✅ Prompt creado en prompts/$(NAME).yaml"
	@echo "   Edita el archivo y luego: git add prompts/$(NAME).yaml"

new-track: ## Crear nueva metadata de track desde template (uso: make new-track NAME=mi-track)
	@if [ -z "$(NAME)" ]; then \
		echo "Error: Especifica NAME=nombre-del-track"; \
		exit 1; \
	fi
	cp metadata/tracks/example-track.yaml metadata/tracks/$(NAME).yaml
	@echo "✅ Metadata creada en metadata/tracks/$(NAME).yaml"
	@echo "   Edita el archivo, valida con: make validate-track TRACK=metadata/tracks/$(NAME).yaml"

new-experiment: ## Crear nuevo experimento desde template (uso: make new-experiment NAME=mi-experimento)
	@if [ -z "$(NAME)" ]; then \
		echo "Error: Especifica NAME=nombre-del-experimento"; \
		exit 1; \
	fi
	mkdir -p experiments/$(NAME)
	cp experiments/templates/experiment-template.md experiments/$(NAME)/README.md
	@echo "✅ Experimento creado en experiments/$(NAME)/"
	@echo "   Edita experiments/$(NAME)/README.md con tus resultados"

test: validate ## Ejecutar todas las validaciones y tests
	@echo "🧪 Ejecutando validaciones..."
	@$(PYTHON) $(TOOLS_DIR)/validate_metadata.py $(METADATA_DIR)/ && echo "✅ Metadata validada"
	@$(PYTHON) $(TOOLS_DIR)/generate_index.py --output /tmp/test-index.json && echo "✅ Generación de índice funciona"
	@echo "✅ Todos los tests pasaron"

git-status: ## Ver estado de git con formato bonito
	@echo "📝 Estado del repositorio:"
	@git status -s

# Default target
.DEFAULT_GOAL := help
