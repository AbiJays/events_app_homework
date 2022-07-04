from models.events import *

event1 = Event("15/4/2022", "Becky & Luke", 300, False, 1, "Rebels and Luke are finally getting married a year later")
event2 = Event("16/5/2022", "Kirstin & Jon", 590, False, 2, "Kirstin and Jon in Scotland, an absolute treck to but so very very lovely")
event3 = Event("18/6/2022", "Neveen & Alice", 450, False, 3, "Two beautiful women getting married, it was so nice, there was a sweety stall")
event4 = Event("15/7/2022", "Ben & Kirsty", 120, False, 4, "TBC")
event5 = Event("20/8/2022", "Rania & Tom", 290, False, 5, "I'm a bridesmaid and I have to be fitted still ;_;")
events = [event1, event2, event3, event4, event5]

def add_new_event(event):
    events.append(event)

def delete_event(event_title):
    event_to_delete = None
    for event in events:
        if event.title == event_title:
            event_to_delete = event
            break
    events.remove(event_to_delete)