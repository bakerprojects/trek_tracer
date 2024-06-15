-- These are some Database Manipulation queries for the Trek Tracer project
-- using the Trek Tracer database.
-- Your submission should contain ALL the queries required to implement ALL the
-- functionalities listed in the Project Specs.

-- get all trails and their details for the List Trails page
SELECT trailID, trailName, length, difficulty, trailInfo FROM Trails

-- get a single trail's data for the Update Trail form
SELECT trailID, trailName, length, difficulty, trailInfo FROM Trails WHERE trailID = :trailID_selected_from_trail_page

-- get all events and their details for the List Events page
SELECT eventID, eventName, eventDate, weather, eventInfo FROM Events

-- get a single event's data for the Update Event form
SELECT eventID, eventName, eventDate, weather, eventInfo FROM Events WHERE eventID = :eventID_selected_from_event_page

-- get all hikers and their details for the List Hikers page
SELECT hikerID, email, userName, biography FROM Hikers

-- get a single hiker's data for the Update Hiker form
SELECT hikerID, email, userName, biography FROM Hikers WHERE hikerID = :hikerID_selected_from_hiker_page

-- get all event registrations for a specific hiker
SELECT registrationID, eventID, registrationTime FROM EventRegistrations WHERE hikerID = :hikerID_selected_from_hiker_page

-- get all hiker logs for a specific hiker
SELECT logID, trailID, eventID, logTime, difficulty FROM HikerLogs WHERE hikerID = :hikerID_selected_from_hiker_page

-- add a new trail. trailID is auto-incremented
INSERT INTO Trails (trailName, length, difficulty, trailInfo) VALUES (:trailNameInput, :lengthInput, :difficultyInput, :trailInfoInput)

-- add a new event eventID is auto-incremented
INSERT INTO Events (eventName, eventDate, weather, eventInfo) VALUES (:eventNameInput, :eventDateInput, :weatherInput, :eventInfoInput)

-- add a new hiker hikerID is auto-incremented
INSERT INTO Hikers (email, userName, biography) VALUES (:emailInput, :userNameInput, :biographyInput)

-- register a hiker for an event. registrationID is auto-incremented
INSERT INTO EventRegistrations (eventID, hikerID, registrationTime) VALUES (:eventID_from_dropdown_Input, :hikerID_from_dropdown_Input, :registrationTimeInput)

-- add a new hiker log. logID is auto-incremented
INSERT INTO HikerLogs (hikerID, trailID, eventID, logTime, difficulty) VALUES (:hikerID_from_dropdown_Input, :trailID_from_dropdown_Input, :eventID_from_dropdown_Input, :logTimeInput, :difficultyInput)

-- update a trail's data based on submission of the Update Trail form
UPDATE Trails SET trailName = :trailNameInput, length = :lengthInput, difficulty = :difficultyInput, trailInfo = :trailInfoInput WHERE trailID = :difficultyInput

-- update an event's data based on submission of the Update Event form
UPDATE Events SET eventName = :eventNameInput, eventDate = :eventDateInput, weather = :weatherInput, eventInfo = :eventInfoInput WHERE eventID = :eventID_from_the_update_form

-- update a hiker's data based on submission of the Update Hiker form
UPDATE Hikers SET email = :emailInput, userName = :userNameInput, biography

--Update EventRegistration's data based on the edit changes made to a certain registrationID
UPDATE EventRegistrations SET eventID = :eventID_from_dropdown_Input, hikerID = :hikerID_from_dropdown_Input, registrationTime = :registrationTimeInput WHERE registrationID = :registrationID_from_the_update_form

--Update HikerLog's data based no the edit changes made to a certain logID
UPDATE HikerLogs SET hikerID = :hikerID_from_dropdown_Input, trailID = :trailID_from_dropdown_Input, eventID = :eventID_from_the_update_form, logTime = :logTimeInput, difficulty = :difficultyInput WHERE logID = :logID_from_the_update_form

-- delete a hiker and their associated data
DELETE FROM Hikers WHERE hikerID = :hikerID_selected_from_hiker_page;
DELETE FROM EventRegistrations WHERE hikerID = :hikerID_selected_from_hiker_page;
DELETE FROM HikerLogs WHERE hikerID = :hikerID_selected_from_hiker_page;

-- delete an event and its associated registrations
DELETE FROM EventRegistrations WHERE eventID = :eventID_selected_from_event_page;
DELETE FROM Events WHERE eventID = :eventID_selected_from_event_page;

-- delete a trail and its associated logs
DELETE FROM HikerLogs WHERE trailID = :trailID_selected_from_trail_page;
DELETE FROM Trails WHERE trailID = :trailID_selected_from_trail_page;