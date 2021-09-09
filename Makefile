setup:
	python setup.py bdist_wheel
	pip install -e .

test:
	pytest --cov=PyDS tests

coverage:
	coverage run -m pytest
	coverage report -m
	coverage html
