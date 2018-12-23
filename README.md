# noize-warner
Monitors a noize level and triggers an event if the level is too high
Based on soundmeter and simple python script.

Setup:
install os packages requirements for soundmeter (https://pypi.org/project/soundmeter/)
pip install -r requirements.txt
pip install --upgrade setuptools (might be needed)

Place a config file at ~/.soundmeter/config
It should contain rms_as_trigger_arg = True - needed to pass rms value to out trigger script

Launch from the repo dir, for instance:
soundmeter --profile main --trigger +4000 3 --action exec --exec ./make_a_warning.py