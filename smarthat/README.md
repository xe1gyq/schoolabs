# SmartHat

Each SmartHat is a piece of headwear that is fitted with a sophisticated ultrasonic ranger sensor. It is a distance monitoring tool for invident people that provides real-time sounds alerts of distance.

Team Members

- Tbd
- Tbd

Components

- [Grove - Buzzer](http://wiki.seeed.cc/Grove-Buzzer/)
- [Grove - Ultrasonic Ranger](http://wiki.seeed.cc/Grove-Ultrasonic_Ranger/)
- [Grove - Rotary Angle Sensor “Potentiometer”](http://wiki.seeed.cc/Grove-Rotary_Angle_Sensor/)
- [Intel® Edison Kit for Arduino](https://www.seeedstudio.com/Intel%C2%AE-Edison-Kit-for-Arduino-p-2149.html)

## StartUp Service

```sh
root@edison:~# cat smarthat.sh
cd /home/root/schoolabs/smarthat
python main.py
```

## Source Code

```python
import time

from upm import pyupm_grove as grove
from upm import pyupm_buzzer as upmBuzzer
from upm import pyupm_ultrasonic as upmUltraSonic
from upm import pyupm_gp2y0a as upmGp2y0a

def buzzerFunction(long):

    buzzer = upmBuzzer.Buzzer(5)
    print long

    chords = [upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_RE, upmBuzzer.BUZZER_MI,
              upmBuzzer.BUZZER_FA, upmBuzzer.BUZZER_SOL, upmBuzzer.BUZZER_LA,
              upmBuzzer.BUZZER_SI];

    for chord_ind in range (0,1):
        # play each note for a half second
        print(buzzer.playSound(chords[chord_ind], long))
        time.sleep(0.1)

    del buzzer

if __name__ == '__main__':

    ultrasonic = upmUltraSonic.UltraSonic(8)
    knob = grove.GroveRotary(3)
    myIRProximity = upmGp2y0a.GP2Y0A(1)

    while True:
        
        abs = knob.abs_value()
        absdeg = knob.abs_deg()
        distance = ultrasonic.getDistance()

        print("Knob Abs: %4d" % int(abs) , "Ultrasonic Distance %4d" % int(distance))

        threshold = int(abs) * 2
        print threshold

        if int(distance) in xrange(0,1000):
            print 'One'
            buzzerFunction(threshold*50)
        elif int(distance) in xrange(1000, 2500):
            print 'Two'
            buzzerFunction(threshold*25)
        elif int(distance) in xrange(2500,4000):
            print 'Three'
            buzzerFunction(threshold)
        else:
            print 'Four'

        time.sleep(.1)
```
