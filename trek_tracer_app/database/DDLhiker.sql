-- Disable foreign key checks to allow for quick table creation
SET FOREIGN_KEY_CHECKS=0;
-- Disable autocommit to allow for multiple statements to be executed in a single transaction
SET AUTOCOMMIT = 0;

-- Added "NOT NULL UNIQUE to all of the *ID cards that were not added earlier for the CREATE TABLE"

-- Create Hikers table
CREATE TABLE Hikers (
  hikerID INT AUTO_INCREMENT NOT NULL UNIQUE, 
  email VARCHAR(255) NOT NULL,
  userName VARCHAR(15) NOT NULL UNIQUE,
  biography VARCHAR(255),
  PRIMARY KEY (hikerID)
);

-- Create Trails table
CREATE TABLE Trails (
  trailID INT AUTO_INCREMENT NOT NULL UNIQUE,
  trailName VARCHAR(255) NOT NULL,
  length VARCHAR(50),
  difficulty ENUM('easy', 'medium', 'hard', 'expert'),
  trailInfo VARCHAR(255),
  PRIMARY KEY (trailID)
);

-- Create Events table
CREATE TABLE Events (
  eventID INT AUTO_INCREMENT NOT NULL UNIQUE,
  eventName VARCHAR(255) NOT NULL,
  eventDate DATETIME,
  weather VARCHAR(50),
  eventInfo VARCHAR(255),
  PRIMARY KEY (eventID)
);

-- Create EventRegistrations table
CREATE TABLE EventRegistrations (
  registrationID INT AUTO_INCREMENT NOT NULL UNIQUE,
  eventID INT,
  hikerID INT,
  registrationTime DATETIME,
  PRIMARY KEY (registrationID),
  FOREIGN KEY (eventID) REFERENCES Events(eventID) ON DELETE CASCADE,
  FOREIGN KEY (hikerID) REFERENCES Hikers(hikerID) ON DELETE CASCADE
);

-- Create HikerLogs table
CREATE TABLE HikerLogs (
  logID INT AUTO_INCREMENT NOT NULL UNIQUE, 
  hikerID INT,
  trailID INT,
  eventID INT,
  logTime DATETIME,
  difficulty ENUM('easy', 'medium', 'hard', 'expert'),
  PRIMARY KEY (logID),
  FOREIGN KEY (hikerID) REFERENCES Hikers(hikerID) ON DELETE CASCADE,
  FOREIGN KEY (trailID) REFERENCES Trails(trailID) ON DELETE CASCADE,
  FOREIGN KEY (eventID) REFERENCES Events(eventID) ON DELETE CASCADE
);

-- Insert data into Hikers table
INSERT INTO Hikers (email, userName, biography)
VALUES ('arborenthusiast@aol.com', 'sprucelover', 'Loves going on hikes and getting outdoors as much as possible'),
       ('burnallforests@hotmail.com', 'notanarsonist', 'Anyone need help with prescribed fires?'),
       ('trees4life@yahoo.com', 'redwoodcoast', 'Oregon native who spends all their time in the redwood forests');

-- Insert data into Trails table
INSERT INTO Trails (trailName, length, difficulty, trailInfo)
VALUES ('Crabtree Falls', '3 miles', 'easy', 'Steep and rocky hike with scenic waterfall'),
       ('Humpback Rock', '1 mile', 'easy', 'Short and uphill hike to panamoric view at the top'),
       ('Elliot Knob', '9 miles', 'hard', 'Strenuous and long elevation climb to the top, Scenic view with fire tower at the top');

-- Insert data into Events table
INSERT INTO Events (eventName, eventDate, weather, eventInfo)
VALUES ('Welcome to summer', '2024-06-20 08:00:00', 'Sunny', 'Early morning hike to celebrate first day of summer'),
       ('Waterfall Friday', '2024-07-15 10:00:00', 'Cloudy', 'Hike along a waterfall with scenic views along the way'),
       ('Crack of Dawn', '2024-05-05 05:00:00', 'Clear', 'Very early sunrise hike, timed to view the sunrise at the summit');

-- Insert data into EventRegistrations table
INSERT INTO EventRegistrations (eventID, hikerID, registrationTime)
VALUES (1, 1, '2024-03-27 14:56:34'),
       (2, 2, '2024-02-18 10:06:43'),
       (3, 3, '2024-04-20 18:33:04');

-- Insert data into HikerLogs table
INSERT INTO HikerLogs (hikerID, trailID, eventID, logTime, difficulty)
VALUES (1, 1, 1, '2024-06-20 08:30:00', 'easy'),
       (2, 2, 2, '2024-07-15 10:30:00', 'easy'),
       (3, 3, 3, '2024-05-05 05:30:00', 'hard');

-- Re-enable foreign key checks
SET FOREIGN_KEY_CHECKS=1;

-- Commit the transaction
COMMIT;