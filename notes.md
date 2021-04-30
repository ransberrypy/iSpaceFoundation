Services:
iSPace has two ways of generating revenue
a. Space Rentals
b. Programs that we offer,when we take programs we offer, we want the following.

Activities:
Events: are sessions ispace have in relation to the program we have or offer


# Model Structure

- Programs
    - Event - fk_Program = event.Prgram
        -Participant -fk_to_Event

We have a list of <Programs>, and there are <events> that happen based on a <program>, then <participants> that attent a particular <event>


- Spaces
    - Booking -fk - Space
        - Spaceusers-fk_Booking 



----------------------------------------------
# QUERY SEARCH WITH FOREIGNKEY AS RELATIONSHIP
-----------------------------------------------
- #When using foreign key as relation there are two ways to get info
a. Reverse relation 
b. Straight relation.

# a.Using Reverse Relation: With reverse relation we import the model who has no foreign key and call our query with an _set.all on it.
Using Programs model to get events 

a. Getting Events from a single program
----------------------------------------
<!-- So we imported Program because event has a foreign key to it in its model and we called the _set.all on the model(event) we wanted -->
>>> from services.models import Program 
>>> program1 = Program.objects.get(id=1)
>>> program1.event_set.all()


>>> Program.objects.last().event_set.all()


b. Getting Participant from a single Event
---------------------------------------------
from events.models import Event
>>> Event.objects.all()
>>> Event.objects.last()
>>> Event.objects.last().participant_set.all()

>>> Event.objects.get(id=1).participant_set.all()


c. Getting Space user from a Single Booking
------------------------------------------------
>>> from bookings.models import Booking
>>> Booking.objects.all()
>>> Booking.objects.first()
>>> Booking.objects.first().spaceuser_set.all()
>>> 

# b. Using STRAIGHT RELATION: Using the striaght relation we call the model and filter the data we want 
GETTING EVENT THAT OCCURED UNDER A PARTICULAR PROGRAM
>>> from events.models import Event
>>> Event.objects.filter(program__id=1)
The above means:"Hey give me a list of events but filter them according to a program with the id of 1"

GETTING PARTICIPANT WHO ATTENDED A PARTICULAR EVENT
from customers.models import Participant
>>> Participant.objects.filter(event__id=1)
<QuerySet [<Participant: Adams Mohammed>]>

OTHER FORMS OF FILTER
Participant.objects.filter(event__name__iexact='Vault')




NB: Under Events, we should have internal events and external events

a. Pull data from event tp Google calendar.

1. Under participants who register for a program or event, allow ability to extract excel data to populate db.

2. Space users should have an is_active check box that when we check it, it leaves the frontend but stays in the db
and also ability to extract info out of excel sheet to populate.


3. Both the registered users and  actual attendants



thursday friday   saturday
800       800     800 = 2400

800 - 700 for more than 2  day program

More than 3hours - 45cedis per hour



FUTURE PROGRAMS AND FOLLOW
1. hAVE A FUNCTION THAT ALLOWS US TRACK LESSONS AND PARTICIPANTS  AND PROGRESS REPORT

- GROUP MESSAGING FUNCTIONALITY


2. TASK MANAGER AND TRACKING
 - PROJECTIONS ADDING
 - TRELLO APPROACH  FOR PROGRAM MANAGEMENT
