# noize-warner

It will replace some funtionality of Anton K. =)

Monitors a noize level and triggers an event if the level is too high.
The solution is based on soundmeter + simple python script + appriate launch with bash :)

Setup:
1) Install os packages requirements for soundmeter (https://pypi.org/project/soundmeter/)
2.0) Might be needed: pip install --upgrade setuptools
2.1) For Ubuntu: sudo apt-get install python3-dev mpg123
3) pip install -r requirements.txt
4) Place a config file at ~/.soundmeter/config or make a symlink:
mkdir ~/.soundmeter && cp config ~/.soundmeter/config 
It should contain rms_as_trigger_arg = True - needed to pass rms value to out trigger script

It has some issues: soundmeter won't wait while the trigger ends and will continue to trigger and trigger and triger
How to launch in a operable way:

while true; do soundmeter --profile main --trigger +4000 5 --action  exec-stop --exec ./make_a_warning.py; sleep 5; done

+4000 - the enrance level. ./make_a_warning.py contains all logic for choosing what action to take next (depending on rms level)
if rms will be above 4000 5 timew in raw, it will trigger ./make_a_warning.py
So above loop will restart soundmeter. The voice messages are short so 5 sec is enough.

P.S.: If you have some free time, fix soundmeter behaviour ;)

JFI: 
Допустимые уровни шума http://www.acoustic.ua/directory/135
