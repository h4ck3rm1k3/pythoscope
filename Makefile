# makefile for running python setups

run_setup_test:
	python setup.py test

lint:
	python setup.py lint

uinstall:
	python setup.py install --user
