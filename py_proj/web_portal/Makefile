# http://stackoverflow.com/questions/18136918/how-to-get-current-relative-directory-of-your-makefile
mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))

setup:
	virtualenv --no-site-packages $(mkfile_path)/venv;
	source $(mkfile_path)/venv/bin/activate;
	install -r $(mkfile_path)/requirements.txt;
	deactivate;

run:
	source venv/bin/activate;
	python web_portal.py;
	deactivate;
