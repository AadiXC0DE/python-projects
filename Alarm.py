import datetime
import time
import winsound

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up!")
            for _ in range(3):
                winsound.Beep(1000, 1000)  # Beep sound for 1 second
            break
        time.sleep(1)

def main():
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
