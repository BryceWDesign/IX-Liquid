.PHONY: test cost

test:
	PYTHONPATH=src python -m pytest -q

cost:
	PYTHONPATH=src python tools/cost_rollup.py
