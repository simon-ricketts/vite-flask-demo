venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3.6 -m venv venv
	venv/bin/python -m pip install pip==21.* setuptools==46.*
	venv/bin/python -m pip install -r $< --progress-bar off
	touch $@

requirements.txt: | requirements.in
	python3.6 -m piptools compile --no-header --output-file $@
	chmod +r $@
