DROP TABLE IF EXISTS Details;
DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerName TEXT,
    OrderDate DATE,
    TotalAmount NUMERIC(10, 2)
);

CREATE TABLE Details (
    DetailID INTEGER PRIMARY KEY,
    OrderID INTEGER REFERENCES Orders(OrderID),
    ProductName TEXT,
    Quantity INTEGER,
    Price NUMERIC(10, 2)
);

--Total Sales per customer--
SELECT CustomerName, SUM(TotalAmount) AS TotalSpent
FROM Orders
GROUP BY CustomerName
ORDER BY TotalSpent DESC;

--Most ordered products--
SELECT ProductName, SUM(Quantity) AS TotalQuantity
FROM Details
GROUP BY ProductName
ORDER BY TotalQuantity DESC;

--Order Details with Totals--
SELECT o.OrderID, o.CustomerName, o.OrderDate,
       d.ProductName, d.Quantity, d.Price,
       (d.Quantity * d.Price) AS LineTotal
FROM Orders o
JOIN Details d ON o.OrderID = d.OrderID
ORDER BY o.OrderID;
