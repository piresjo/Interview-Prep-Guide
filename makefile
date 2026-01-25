test_all: 
	pytest

requirements: requirements.txt 
	pip3 install -r requirements.txt

format:
	black *

clean:
	rm -rf __pycache__