# template for "Stopwatch: The Game"
import simplegui
# define global variables
setne = 0
stops = 0
wholestops = 0
on = True
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    t = int(t)
    a = t // 600
    b = t // 100
    c = (t // 10) % 10
    d = t % 10
    if b >= 6:
        b = 0    
    if c > 10:
        c = 0       
    if d > 10:
        d = 0
    if t > 699:
        b = (t // 100) // 10
    return "#%s:%s%s.%s" % (a,b,c,d)
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global on
    timer.start()
    on = True
def stop():
    global setne,stops,wholestops,on
    stops = int(stops)
    wholestops = int(wholestops)
    timer.stop()
    if on==True:
        stops += 1
        if setne % 10==0:
            wholestops += 1
    on = False
def reset():
    global setne, stops, wholestops
    setne = 0
    stops = 0
    wholestops = 0

# define event handler for timer with 0.1 sec interval
def time():
    global setne
    setne = int(setne)
    setne += 1
# define draw handler
def draw(canvas):
    global setne, stops, wholestops
    setne = str(setne)
    stops = str(stops)
    wholestops = str(wholestops)
    canvas.draw_text(format(setne), [100, 100], 20,  "Red")
    canvas.draw_text(wholestops + "/" + stops, [170, 20], 20,  "Red")
    
# create frame
frame=simplegui.create_frame("Stopwatch", 200, 200)
timer=simplegui.create_timer(100, time)
start=frame.add_button("Start", start, 50)
stop=frame.add_button("Stop", stop, 50)
reset=frame.add_button("Reset", reset, 50)
# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
# Please remember to review the grading rubric
