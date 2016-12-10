# http://stackoverflow.com/questions/18136918/how-to-get-current-relative-directory-of-your-makefile
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
root_dir := $(dir $(mkfile_path))

init:
	echo $(mkfile_path)
	echo $(root_dir)

setup:
	virtualenv --no-site-packages $(root_dir)venv; \
	. $(root_dir)venv/bin/activate; \
	pip install -r $(root_dir)requirements.txt; \
	deactivate;

run:
	. $(root_dir)venv/bin/activate; \
	$(root_dir)venv/bin/python web_portal.py; 
