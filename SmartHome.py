import time

try:
    import adafruit_dht
    import psutil
    import RPi.GPIO as GPIO
except:
    import mock.adafruit_dht as adafruit_dht
    import mock.GPIO as GPIO
    import mock.psutil as psutil


class SmartHome:
    AIR_QUALITY_PIN = 5
    SERVO_PIN = 6
    BUZZER_PIN = 16
    DHT_PIN1 = 23
    DHT_PIN2 = 24
    INFRARED_PIN = 25
    LIGHT_PIN = 26
    PHOTO_PIN = 27  # Photoresistor pin

    def __init__(self):
        """
        Constructor
        """
        # Ignore this loop. It is required for the hardware deployment
        for proc in psutil.process_iter():
            if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
                proc.kill()

        # GPIO pin setup
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.AIR_QUALITY_PIN, GPIO.IN)
        GPIO.setup(self.INFRARED_PIN, GPIO.IN)
        GPIO.setup(self.PHOTO_PIN, GPIO.IN)
        GPIO.setup(self.LIGHT_PIN, GPIO.OUT)
        GPIO.setup(self.BUZZER_PIN, GPIO.OUT)
        GPIO.setup(self.SERVO_PIN, GPIO.OUT)

        self.dht_indoor = adafruit_dht.DHT11(self.DHT_PIN1)
        self.dht_outdoor = adafruit_dht.DHT11(self.DHT_PIN2)
        self.servo = GPIO.PWM(self.SERVO_PIN, 50)
        self.servo.start(0)
        self.servo.ChangeDutyCycle(2)

        self.light_on = False
        self.blinds_open = False
        self.buzzer_on = False

        GPIO.output(self.LIGHT_PIN, GPIO.LOW)
        GPIO.output(self.BUZZER_PIN, GPIO.LOW)
        time.sleep(2)

    def check_room_occupancy(self) -> bool:
        """
        Checks whether the infrared distance sensor on the ceiling detects something in front of it.
        :return: True if the infrared sensor detects something, False otherwise.
        """
        pass

    def manage_light_level(self) -> None:
        """
        User story 2:
        When the user leaves the room the smart home system turns off the smart light bulb.
        When the user goes back into the room, the system turns on the smart light bulb.

        User story 3:
        When the user comes back inside the room, before turning on the smart light bulb,
        the system checks how much light is inside the room (by querying the photoresistor).
        If the measured light level inside the room is above the threshold of 500 lux,
        the smart home system does not turn on the smart light bulb even if the person is in the room;
        on the other hand, if the actual light level is below the threshold of 500 lux
        the system regulates the smart light bulb as usual.
        """
        pass

    def manage_blinds(self) -> None:
        """
        Two temperature sensors, one inside and one outside the room are used to trigger the servo motor
        to manage the blinds.
        Whenever the internal temperature is lower than the  outside temperature minus two degrees,
        the system opens the blinds by using the servo motor;
        on the other hand, when the inside temperature is greater than the outside temperature
        plus two degrees, the system closes the blinds by using the servo motor.
        """
        try:
            # Your code goes here
            # Remove the pass
            pass
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2)
            return
        except Exception as error:
            self.dht_indoor.exit()
            self.dht_outdoor.exit()
            raise error

    def monitor_air_quality(self):
        """
        The air quality sensor is configured in a way such that if the amount of gas particles detected
        is below 500 PPM, the sensor returns a constant reading of 1.
        As soon as the gas measurement goes to 500 PPM or above, the sensor switches state and
        starts returning readings of 0.

        To notify the user of any gas leak an active buzzer is employed;
        if the amount of detected gas is greater than or equal to 500 PPM,
        the system turns on the buzzer until the smoke level goes below the threshold of 500 PPM.
        """
        pass
