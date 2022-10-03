# Add your Python code here. E.g.
# Written by Muhamad Abdul Aziz
import microbit as m

def runChrono():
    currentTime = m.running_time() / 1000
    
    return currentTime

def stopChrono(start, duration):
    currentTime = m.running_time() / 1000
    duration += (currentTime - start)
    
    return currentTime, duration

def resetChrono():
    currentTime = 0
    duration = 0
    
    return currentTime, duration
    
state = 0
currentTime = 0
duration = 0

def launchChrono(state, currentTime, duration):
    while True: 
        if state == 0:
            if m.button_a.was_pressed():
                currentTime = runChrono()
                state = 1
            elif m.button_b.was_pressed():
                state = 0
                
        elif state == 1:
            if m.button_a.was_pressed():
                currentTime, duration = stopChrono(currentTime, duration)
                m.display.scroll(duration)
                state = 2
            elif m.button_b.was_pressed():
                state = 1
                m.display.scroll(duration + m.running_time() / 1000 - currentTime)
                
        elif state == 2:
            if m.button_b.was_pressed():
                currentTime, duration = resetChrono()
                state = 0
            elif m.button_a.was_pressed():
                currentTime = runChrono()
                state = 1
                
launchChrono(state, currentTime, duration)       