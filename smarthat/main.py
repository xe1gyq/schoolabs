from upm import pyupm_buzzer as upmBuzzer
from upm import pyupm_ultrasonic as upmUltraSonic

def buzzerFunction():

    buzzer = upmBuzzer.Buzzer(5)

    chords = [upmBuzzer.BUZZER_DO, upmBuzzer.BUZZER_RE, upmBuzzer.BUZZER_MI,
              upmBuzzer.BUZZER_FA, upmBuzzer.BUZZER_SOL, upmBuzzer.BUZZER_LA,
              upmBuzzer.BUZZER_SI];

    for chord_ind in range (0,7):
        # play each note for a half second
        print(buzzer.playSound(chords[chord_ind], 500000))
        time.sleep(0.1)

    print("exiting application")

    del buzzer

def main():

    buzzerFunction()

if __name__ == '__main__':
    main()
