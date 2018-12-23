# noize-warner
Monitors a noize level and triggers an event if the level is too high
Based on soundmeter and simple python script.

Setup:
install os packages requirements for soundmeter (https://pypi.org/project/soundmeter/)
pip install -r requirements.txt
pip install --upgrade setuptools (might be needed)

Place a config file at ~/.soundmeter/config
It should contain rms_as_trigger_arg = True - needed to pass rms value to out trigger script

How to launch in a ok way: from the repo dir, for instance:

Problem: soundmeter won't wait while the trigger ends and will continue to trigger and trigger and triger
So next loop will restart soundmeter.

while true; do soundmeter --profile main --trigger +4000 3 --action  exec-stop --exec ./make_a_warning.py; sleep 5; done

The voice messages are short so 5 sec is enough.

P.S.: If you have some free time, fix soundmeter behaviour ;)
