from flask import render_template

from app import app
from models.event_list import events # get a hold of all the tasks

# change the template to display all events

@app.route('/events')
def index():
    # print(events) if you write this then refresh the web browser page it prints in terinal. same with breakpoint()
    return render_template("index.html", title="Abi", all_events = events) # pass the tasks down to the template
    # events in line 4 and events in line 11 must be the same. all_events must be how it is refered to as such in template.

# POST ACTION