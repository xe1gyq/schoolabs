# SmartHat

Each SmartHat is a piece of headwear that is fitted with a sophisticated ultrasonic ranger sensor. It is a distance monitoring tool for invident people that provides real-time sounds alerts of distance.

Team Members

- Angela A
- Ana Paula P
- Leah Linares
- Hillary

Components

- [Intel® Edison Kit for Arduino](https://www.seeedstudio.com/Intel%C2%AE-Edison-Kit-for-Arduino-p-2149.html)
- [Grove - Buzzer](http://wiki.seeed.cc/Grove-Buzzer/)
  - Connected to Digital Output D5
- [Grove - Ultrasonic Ranger](http://wiki.seeed.cc/Grove-Ultrasonic_Ranger/)
  - Connected to Digital Input D8
- [Grove - Rotary Angle Sensor “Potentiometer”](http://wiki.seeed.cc/Grove-Rotary_Angle_Sensor/)
  - Connected to Analog Input A3

## StartUp SmartHat Service

```sh
root@edison:~# cat smarthat.sh
cd /home/root/schoolabs/smarthat
python main.py
```

## Source Code

```python
#!/usr/bin/python

import time

from upm import pyupm_grove as grove
from upm import pyupm_buzzer as upmBuzzer
from upm import pyupm_ultrasonic as upmUltraSonic
from upm import pyupm_gp2y0a as upmGp2y0a

def buzzerFunction(long):

    buzzer = upmBuzzer.Buzzer(5)

    chords = [upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_RE, upmBuzzer.BUZZER_MI,
              upmBuzzer.BUZZER_FA, upmBuzzer.BUZZER_SOL, upmBuzzer.BUZZER_LA,
              upmBuzzer.BUZZER_SI];

    for chord_ind in range (0,1):
        # play each note for a half second
        buzzer.playSound(chords[chord_ind], long)
        time.sleep(0.1)

    del buzzer

if __name__ == '__main__':

    ultrasonic = upmUltraSonic.UltraSonic(8)
    knob = grove.GroveRotary(3)

    while True:
        
        abs = knob.abs_value()
        absdeg = knob.abs_deg()
        distance = ultrasonic.getDistance()

        print("Knob Abs: %4d" % int(abs) , "Ultrasonic Distance %4d" % int(distance))

        threshold = int(abs)

        if int(distance) in xrange(0,1):
            print 'Zero'
            buzzerFunction(100)
        elif int(distance) in xrange(1,500):
            print 'One'
            buzzerFunction(threshold*900)
        elif int(distance) in xrange(500,99):
            print 'Two'
            buzzerFunction(threshold*400)
        elif int(distance) in xrange(1000, 2500):
            print 'Three'
            buzzerFunction(threshold*100)
        elif int(distance) in xrange(2500,4000):
            print 'Four'
            buzzerFunction(threshold)
        else:
            print 'Five'

        time.sleep(.1)
```
