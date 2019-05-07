show:
	@echo "dist : make package for project"
	@echo "upload : upload project to pypi"
	@echo "clean : remove dist files"

dist:
	python setup.py sdist bdist_wheel --universal

upload: dist
	twine upload dist/*

clean:
	rm -rf dist
	rm -rf musicsa.egg-info
	rm -rf build
