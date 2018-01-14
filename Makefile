.PHONY: publish clean

publish:
	@echo "Use 'tox -e release'"

clean:
	@echo "Cleaning up distutils and tox stuff"
	rm -rf build dist deb_dist
	rm -rf *.egg .eggs *.egg-info
	rm -rf .tox
	@echo "Cleaning up byte compiled python stuff"
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
