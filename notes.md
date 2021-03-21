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
Using Programs model to get events 

a. Getting Events from a single program
----------------------------------------
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