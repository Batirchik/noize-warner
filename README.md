# noize-warner
Monitors a noize level and triggers an event if the level is too high.
The solution is based on soundmeter + simple python script + appriate launch with bash :D

Setup:
1) Install os packages requirements for soundmeter (https://pypi.org/project/soundmeter/)
2.0) Might be needed: pip install --upgrade setuptools 
3) pip install -r requirements.txt
4) Place a config file at ~/.soundmeter/config or make a symlink
It should contain rms_as_trigger_arg = True - needed to pass rms value to out trigger script

It has some issues: soundmeter won't wait while the trigger ends and will continue to trigger and trigger and triger
How to launch in a operable way: 
while true; do soundmeter --profile main --trigger +4000 3 --action  exec-stop --exec ./make_a_warning.py; sleep 5; done

So next loop will restart soundmeter. The voice messages are short so 5 sec is enough.

P.S.: If you have some free time, fix soundmeter behaviour ;)

JFI: 
Допустимые уровни шума http://www.acoustic.ua/directory/135
