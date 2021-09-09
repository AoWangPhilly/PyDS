setup:
	python setup.py bdist_wheel
	pip install -e .

test:
	pytest --cov=PyDS tests
