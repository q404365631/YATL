check:
	poetry run ruff check . --fix

format:
	poetry run ruff format .

run_server:
	poetry run python src/yatl/server.py

run_tests:
	poetry run python src/yatl/run.py