import requests
import time
import random
import click

from sense_hat import SenseHat
sense = SenseHat()

def get_joystick_direction():
    d_long = 0
    d_la = 0
    send_vel=False
    dir = ""
        
    for event in sense.stick.get_events():
            dir = event.direction
    if dir == 'up':
        click.echo('Up')
        send_vel = True
        d_long = 0
        d_la = 1      # Up arrow
    elif dir == 'down':
        send_vel = True
        d_long = 0
        d_la = -1     # Down arrow
    elif dir == 'left':
        send_vel = True
        d_long = -1
        d_la = 0
    elif dir == 'right':
        send_vel = True
        d_long = 1
        d_la = 0    
    elif dir =='':
        d_long = 0
        d_la = 0
        send_vel = False
    else :
        click.echo('Invalid input')
        d_long = 0
        d_la = 0
        send_vel = False
    return d_long, d_la, send_vel


if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"
    while True:
        d_long, d_la, send_vel = get_joystick_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
