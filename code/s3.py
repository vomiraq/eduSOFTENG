import datetime
import time

def display_time():

    counter = 0
    while counter < 5:
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        print(f"Текущее время: {formatted_time}")
        
        counter += 1
        if counter < 5:
            time.sleep(1)

if __name__ == "__main__":
    display_time()