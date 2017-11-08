import time

from upm import pyupm_grove as grove
from upm import pyupm_buzzer as upmBuzzer
from upm import pyupm_ultrasonic as upmUltraSonic
from upm import pyupm_gp2y0a as upmGp2y0a
from upm import pyupm_hcsr04 as hcsr04

def buzzerFunction():

    buzzer = upmBuzzer.Buzzer(5)

    chords = [upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_RE, upmBuzzer.BUZZER_MI,
              upmBuzzer.BUZZER_FA, upmBuzzer.BUZZER_SOL, upmBuzzer.BUZZER_LA,
              upmBuzzer.BUZZER_SI];

    for chord_ind in range (0,1):
        # play each note for a half second
        print(buzzer.playSound(chords[chord_ind], 500000))
        time.sleep(0.1)

    print("exiting application")

    del buzzer

if __name__ == '__main__':

    ultrasonic = upmUltraSonic.UltraSonic(2)
    knob = grove.GroveRotary(3)
    myIRProximity = upmGp2y0a.GP2Y0A(2)
    hcsr04_sensor = hcsr04.HCSR04(6, 7);

    GP2Y0A_AREF = 5.0;
    SAMPLES_PER_QUERY = 20;

    while True:
        
        abs = knob.abs_value()
        absdeg = knob.abs_deg()
        distance = ultrasonic.getDistance()

        print("Knob Abs: %4d" % int(abs) , "Ultrasonic Distance %4d" % int(distance))
        print("Distance: {0}".format(hcsr04_sensor.getDistance(hcsr04.HCSR04_CM)))

        #if ( int(distance) <= int(abs) ):
        #    buzzerFunction()
    
        #print myIRProximity.value(GP2Y0A_AREF, SAMPLES_PER_QUERY)

        time.sleep(.1)

