query_high_value_customers = '''
    SELECT CustomerName, SUM(Price * Quantity) AS TotalSpent FROM Customers c
    INNER JOIN Orders o 
    ON o.CustomerID = c.CustomerID
    INNER JOIN OrderDetails od 
    ON od.OrderID = o.OrderID
    INNER JOIN Products p 
    ON p.ProductID = od.ProductID
    GROUP BY c.CustomerID
    ORDER BY TotalSpent DESC
    LIMIT 10;
'''


query_top_categories_revenue = '''
    SELECT CategoryName, SUM(Price * Quantity) AS Revenue FROM Categories c
    INNER JOIN Products p 
    ON p.CategoryID = c.CategoryID
    INNER JOIN OrderDetails od 
    ON od.ProductID = p.ProductID
    GROUP BY c.CategoryID
    ORDER BY Revenue DESC
    LIMIT 10;
'''


query_top_employees_by_revenue = '''
    SELECT FirstName || ' ' || LastName AS EmployeeName, SUM(p.Price * od.Quantity) AS Revenue FROM Employees e
    INNER JOIN Orders o 
    ON o.EmployeeID = e.EmployeeID
    INNER JOIN OrderDetails od 
    ON od.OrderID = o.OrderID
    INNER JOIN Products p 
    ON p.ProductID = od.ProductID
    GROUP BY e.EmployeeID
    ORDER BY Revenue DESC
    LIMIT 10;
'''


query_top_revenue_by_country = '''
    SELECT Country, SUM(Price * Quantity) AS Revenue FROM Customers c
    INNER JOIN Orders o 
    ON o.CustomerID = c.CustomerID
    INNER JOIN OrderDetails od 
    ON od.OrderID = o.OrderID
    INNER JOIN Products p 
    ON p.ProductID = od.ProductID
    GROUP BY c.Country
    ORDER BY Revenue DESC
    LIMIT 10;
'''


query_customers_total_revenue = '''
    SELECT CustomerName, SUM(Price * Quantity) AS TotalSpent FROM Customers c
    INNER JOIN Orders o 
    ON o.CustomerID = c.CustomerID
    INNER JOIN OrderDetails od 
    ON od.OrderID = o.OrderID
    INNER JOIN Products p 
    ON p.ProductID = od.ProductID
    GROUP BY c.CustomerID
    ORDER BY TotalSpent DESC
'''


query_revenue_total_by_country = '''
    SELECT Country, SUM(Price * Quantity) AS Revenue FROM Customers c
    INNER JOIN Orders o 
    ON o.CustomerID = c.CustomerID
    INNER JOIN OrderDetails od ON od.OrderID = o.OrderID
    INNER JOIN Products p 
    ON p.ProductID = od.ProductID
    GROUP BY c.Country
    ORDER BY Revenue DESC;
'''


query_categories_total_revenue = '''
    SELECT CategoryName, SUM(Price * Quantity) AS Revenue FROM Categories c
    INNER JOIN Products p 
    ON p.CategoryID = c.CategoryID
    INNER JOIN OrderDetails od 
    ON od.ProductID = p.ProductID
    GROUP BY c.CategoryID
    ORDER BY Revenue DESC;
'''


query_total_revenue = '''
    SELECT SUM(Price * Quantity) AS TotalRevenue FROM OrderDetails od
    INNER JOIN Products p
    ON p.ProductID = od.ProductID;
'''


query_power_bi = '''
SELECT c.CustomerName, c.Country, cat.CategoryName, e.FirstName || ' ' || e.LastName AS EmployeeName,
p.ProductName, od.Quantity, p.Price, (p.Price * od.Quantity) AS Revenue FROM Customers c
    INNER JOIN Orders o
    ON o.CustomerID = c.CustomerID
    INNER JOIN OrderDetails od
    ON od.OrderID = o.OrderID
    INNER JOIN Products p
    ON p.ProductID = od.ProductID
    INNER JOIN Categories cat
    ON cat.CategoryID = p.CategoryID
    INNER JOIN Employees e
    ON e.EmployeeID = o.EmployeeID;
'''









