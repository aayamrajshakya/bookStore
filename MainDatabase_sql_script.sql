CREATE TABLE Cart (
    userID TEXT NOT NULL,
    ISBN TEXT NOT NULL,
    Title TEXT NOT NULL,
    Stock INT NOT NULL,
    FOREIGN KEY (ISBN) REFERENCES Inventory (ISBN),
    FOREIGN KEY (userID) REFERENCES User (userID)
);

CREATE TABLE Inventory (
    ISBN TEXT NOT NULL,
    Title TEXT NOT NULL,
    Author TEXT NOT NULL,
    Genre TEXT NOT NULL,
    Pages INTEGER NOT NULL,
    ReleaseDate TEXT NOT NULL,
    Stock INTEGER NOT NULL,
    PRIMARY KEY (ISBN)
);

CREATE TABLE User (
    userID TEXT NOT NULL,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Address TEXT NOT NULL,
    City TEXT NOT NULL,
    State TEXT NOT NULL,
    Zip INT NOT NULL,
    Payment TEXT NOT NULL,
    PRIMARY KEY (userID)
);

INSERT INTO Inventory (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock)
VALUES
('996-5-46797-528-9', 'A Light in the Attic', 'Izabella Johnston', 'Poetry', 717, '6/2/1983', 17),
('905-8-30368-364-1', 'Tipping the Velvet', 'Ajay Connolly', 'Historical Fiction', 352, '1/19/1996', 8),
('902-2-56822-191-8', 'Soumission', 'Clifford Dotson', 'Fiction', 334, '9/17/2018', 20),
('972-4-81382-454-9', 'Sharp Objects', 'Rishi Garrett', 'Mystery', 1232, '3/18/2019', 10),
('955-0-61471-717-6', 'Sapiens: A Brief History of Humankind', 'Kirsty Glenn', 'History', 977, '8/7/1974', 81),
('944-1-27776-208-9', 'The Requiem Red', 'Celeste Morse', 'Young Adult', 1770, '8/20/2014', 67),
('989-1-14847-590-1', 'The Dirty Little Secrets of Getting Your Dream Job', 'Markus Shelton', 'Business', 456, '8/8/1973', 43),
('990-1-68390-321-3', 'The Black Maria', 'Jaya West', 'Poetry', 198, '2/19/1978', 55),
('957-6-63027-937-5', 'Shakespeare''s Sonnets', 'Cassandra Mckay', 'Poetry', 545, '3/6/2007', 4),
('902-9-92919-582-6', 'Set Me Free', 'May Donnelly', 'Young Adult', 1927, '2/14/1983', 9),
('992-1-26254-320-8', 'Scott Pilgrim''s Precious Little Life (Scott Pilgrim #1)', 'Jakob Jackson', 'Sequential Art', 709, '5/11/1990', 78),
('995-6-72044-493-0', 'Rip it Up and Start Again', 'Alec Gross', 'Music', 1646, '4/10/1996', 56),
('995-9-75389-803-3', 'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991', 'Bobby Gardner', 'Music', 609, '4/24/2022', 33),
('939-0-70749-341-1', 'Olio', 'Theodore Boyle', 'Poetry', 1503, '9/2/2005', 14),
('944-8-30214-799-5', 'Mesaerion: The Best Science Fiction Stories 1800-1849', 'Yousef Tanner', 'Science Fiction', 1248, '4/13/1986', 5);

INSERT INTO User (userID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment)
VALUES ('rachellustamey', 'rachellustamey@icloud.com', 'Memphis123!', 'Rachel', 'Stamey', 'East Creek Road #11', 'Germantown', 'Tennessee', 38138, 'Wells Fargo debit');
