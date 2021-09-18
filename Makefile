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
	cd sphinx_docs && rm ./PyDS.rst ./PyDS.LinkedList.rst ./modules.rst
	cd sphinx_docs && sphinx-apidoc -o . ../src/PyDS --ext-autodoc
	cd sphinx_docs && make html

create_docs:
	rm -rf docs && mkdir docs
	cp -rf sphinx_docs/_build/html/. docs
	cd docs && touch .nojekyll
