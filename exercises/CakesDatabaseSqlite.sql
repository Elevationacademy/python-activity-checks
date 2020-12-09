

DROP TABLE IF EXISTS "CakeOrders";

CREATE TABLE CakeOrders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    Name TEXT,
    Age INTEGER,
    Address TEXT,
    Cake_Flavor TEXT,
    Cake_Price REAL );

INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (1, 12345678, 'Yan Cohen', 51, 'Moshe Dayan Blvd Jerusalem', 'Chocolate', 150.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (2, 74639274, 'Yossi Cohen', 86, 'Moshava Germanit 11 Haifa', 'Cheese', 252.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (3, 93765527, 'Mia San', 32,'Ben Yehuda 3 Tel-Aviv', 'Banana', 181.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (4, 73559787, 'Elad Levi', 48,'Derech Hashalom Elad', 'Fruits', 301.1);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (5, 12345678, 'Yan Cohen', 51, 'Moshe Dayan Blvd Jerusalem', 'Banana', 181.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (6, 12345678, 'Yan Cohen', 51, 'Moshe Dayan Blvd Jerusalem', 'Fruits', 301.1);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (7, 12345678, 'Yan Cohen', 51, 'Moshe Dayan Blvd Jerusalem', 'Chocolate', 150.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (8, 74639274, 'Yossi Cohen', 86, 'Moshava Germanit 11 Haifa', 'Chocolate', 150.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (9, 93765527, 'Mia San', 32, 'Ben Yehuda 3 Tel-Aviv', 'Chocolate', 150.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (10, 73559787, 'Elad Levi', 48, 'Derech Hashalom Elad', 'Chocolate', 150.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (11, 12345678, 'Yan Cohen', 51,'Moshe Dayan Blvd Jerusalem', 'Banana', 181.9);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (12, 12345678, 'Yan Cohen', 51,'Moshe Dayan Blvd Jerusalem', 'Fruits', 301.1);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (13, 12345678, 'Yan Cohen', 51, 'Moshe Dayan Blvd Jerusalem', 'Banana', 181.9);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (14, 12345678, 'Yan Cohen', 51, 'Moshe Dayan Blvd Jerusalem', 'Banana', 181.9);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (15, 12345678, 'Yan Cohen', 51, 'Moshe Dayan Blvd Jerusalem', 'Chocolate', 150.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (16, 74639274, 'Sam Goldberg', 76, 'Moshava Germanit 2 Haifa', 'Fruits', 301.1);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (17, 74639274, 'Sam Goldberg', 76, 'Moshava Germanit 2 Haifa', 'Cheese', 252.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (18, 88746435, 'Lia Goldberg', 76, 'Moshava Germanit 3 Haifa', 'Fruits', 302.7);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (19, 87536868, 'James Smith', 18, 'Moshava Germanit 4 Haifa', 'Chocolate', 150.4);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (20, 99842376, 'Bob Smith', 44, 'Moshava Germanit 5 Haifa', 'Fruits', 301.1);
INSERT INTO CakeOrders (OrderID, CustomerID, Name, Age, Address, Cake_Flavor, Cake_Price) VALUES (21, 93765527, 'Sarah Smith', 41, 'Moshava Germanit 5 Haifa', 'Cheese', 252.4);

