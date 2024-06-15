Trek Tracer app developed by Cameron Baker and Aizen Yamashita for CS340

Citations:
Citation for app.py: (
Date: 05/22/2024
Copied from /OR/ Adapted from /OR/ Based on
the format of this code is based on the source below, but is hand authored by the Trek Tracer team.
Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app
)

Source for background.jpg: (
Date: 6/1/24
Free use image by Andrei Tanase
Source URL: https://www.pexels.com/photo/man-standing-on-a-rock-1271619/
)

Source for style.css: (
Date: 6/1/24
Based on and then adapted from a previously developed CSS file by Cameron Baker, a member of the Trek Tracer team.
)

Project Summary

Our project, Trek Tracer, creates a database for an organization to track hikers, trails, and manage events. It allows
hikers to stay connected, discover new trails, and join in on hiking events. The primary goal is to create a symbiotic
database between hikers and an organization, Trek Tracer. Events can be submitted by users and contain details such as
the difficulty, weather and details about the event. This database will also serve as a tool for hikers to track their
events and hikes through the use of HikerLogs. Hikerlogs will contain information related to hikers, such as which
trails and events are more popular among hikers. This allows for the organization to analyze the database for trends,
which can be used by the hikers to get more data about an area they are curious about. Examples of this is seeing how
often trails get used, which can be important for things like maintenance, and how popular a certain location is, which
can be used to schedule events. This database is designed to support a total of 3000 EventRegistrations and 10000
HikerLogs. Along with 100 trails and 250 events, there are plenty of options for Hikers to choose from.



Database Outline

Hikers: Records the details of hikers
hikerID: int, auto_increment, unique, not NULL, PK
email: varchar, not NULL
userName: varchar(15), unique, not NULL
biography: varchar(255)
Relationship: A M:M relationship with Events, where Event Registrations acts as an intersection table.
A 1:M relationship between Hikers and EventRegistrations using hikerID as FK inside EventRegistrations.
Another 1:M relationship between Hikers and HikerLogs using hikerID as FK inside HikerLogs

Trails: Hiking trail information stored in the system
trailID: int, auto_increment, unique, not NULL, PK
trailName: varchar, not NULL
length: varchar(50)
difficulty: enum “easy”, “medium”, “hard”, “expert”
trailInfo: varchar(255)
Relationship: a 1:M relationship between Trails and HikerLogs using trailID as FK inside HikerLogs

Events: Information about hiking events
eventID: int, auto_increment, unique, not NULL, PK
eventName: varchar, not NULL
eventDate: datetime
weather: varchar(50)
eventInfo: varchar(255)
Relationship: A M:M relationship with Hikers, where EventRegistrations acts as an intersection table.
A 1:M relationship between Events and EventRegistrations using eventID inside Event Registration.
Another 1:M relationship between Events and HikerLogs using eventID as FK inside HikerLogs

EventRegistrations: Registration details for events, intersection table between Hikers and Events
registrationID: int, auto_increment, unique, not NULL, PK
eventID: int, FK to Events
hikerID: int, FK to Hikers
registrationTime: datetime
Relationship: A M:M relationship between Hikers and Events is served through this intersection table, containing
both FK hikerID and eventID. A M:1 relationship between EventRegistrations and Hikers using hikerID inside
EventRegistrations. Another M:1 relationship is between EventRegistrations and Events using the eventID
shared between them.

HikerLogs: History of trails and events a hiker participated in
logID: int, auto_increment, unique, not NULL, PK
hikerID: int, FK to Hikers
trailID: int, FK to Trails
eventID: int, FK to Events
logTime: datetime
difficulty: enum “easy”, “medium”, “hard”, “expert”
Relationship: a M:1 relationship between HikerLogs and hikerID using hikerID, eventID being shared between
HikerLogs and Event and finally trailID that is being shared between HikerLogs and Trails
