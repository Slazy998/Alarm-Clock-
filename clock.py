import time
import datetime
import pygame

def set_alarm(alarm_time):
    is_running = True
    music= 'Python/real-love.mp3'
    print(f'Alarm set on {alarm_time}')
    while is_running:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f'Time: {current_time}')

        if current_time == alarm_time:
            print(f"Wakkeyy Wakkeyy it's {alarm_time}")
            pygame.mixer.init()
            try:
                pygame.mixer.music.load(music)
                pygame.mixer.music.play()
            except pygame.error:
                print("Failed to located the mp3 file ")
            while pygame.mixer.music.get_busy():
                shut=input('Shut the alarm press Q: ').lower()
                if shut == 'q':
                    pygame.mixer.music.stop()
                time.sleep(1)
            is_running = False
        
        time.sleep(1) 
     

if __name__ == "__main__":
    alarm_time = input("Set the alarm in Hours: Minutes: Seconds format: ")

    try:
        alarm_time = datetime.datetime.strptime(alarm_time, '%H:%M:%S').strftime('%H:%M:%S')
        set_alarm(alarm_time)

    except ValueError:
        print("Invalid time format. Please enter in H:M:S format (e.g., 12:34:56).")
