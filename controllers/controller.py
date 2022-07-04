from flask import render_template, request, redirect
from app import app
from models.event_list import events, add_new_event, delete_event # get a hold of all the tasks
from models.events import * #File should actually be event.py not events 

# change the template to display all events

@app.route('/events')
def index():
    # print(events) if you write this then refresh the web browser page it prints in terinal. same with breakpoint()
    return render_template("index.html", title="Abi", all_events = events) # pass the tasks down to the template
    # events in line 4 and events in line 11 must be the same. all_events must be how it is refered to as such in template.

# POST ACTION
@app.route('/events', methods=['POST'])
def add_event():
    eventDate = request.form['date'] # must match the class outlne 'title' === self.title = title 
    eventTitle = request.form['title']
    eventGuest = request.form['guest_number']
    eventRoom = request.form['room']
    eventDesc = request.form['description']
    recurring = True if 'recurring' in request.form else False
    newEvent = Event(date=eventDate, title=eventTitle, recurring=recurring, guest_number=eventGuest, room=eventRoom, description=eventDesc)
    add_new_event(newEvent)
    
    return redirect('/events')

@app.route('/events/delete/<title>', methods=['POST'])
def delete(title):
    delete_event(title)
    return redirect('/events')