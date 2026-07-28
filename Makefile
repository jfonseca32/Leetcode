.PHONY: check install lint test

UV ?= uv
PYTEST ?= $(UV) run pytest
PREK ?= $(UV) run prek

install:
	$(UV) sync --dev

test:
	$(PYTEST)

lint:
	$(PREK) run --all-files

check: test lint
