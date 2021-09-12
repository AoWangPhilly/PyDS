setup:
	python setup.py bdist_wheel
	pip install -e .

test:
	pytest --cov=PyDS tests

coverage:
	coverage run -m pytest
	coverage report -m
	coverage html

sphinx:
	cd docs && rm ./PyDS.rst ./PyDS.LinkedList.rst ./modules.rst
	cd docs && sphinx-apidoc -o . ../src/PyDS --ext-autodoc
	cd docs && make html
