
-- =========================================
-- CONSULTAS SQL
-- =========================================

-- VISTA: Total de ventas por ciudad
CREATE VIEW ventas_por_ciudad AS
SELECT 
    ci.CityName,
    SUM(s.TotalPrice) AS TotalVentas
FROM sales s
JOIN customers c ON s.CustomerID = c.CustomerID
JOIN cities ci ON c.CityID = ci.CityID
GROUP BY ci.CityName;

-- VISTA: Ranking de productos por ingresos
CREATE VIEW ranking_productos AS
SELECT 
    p.ProductName,
    SUM(s.TotalPrice) AS TotalIngresos
FROM sales s
JOIN products p ON s.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalIngresos DESC;

-- PROCEDIMIENTO: Obtener top N productos por ingresos
DELIMITER //
CREATE PROCEDURE TopProductos(IN limite INT)
BEGIN
    SELECT p.ProductName, SUM(s.TotalPrice) AS Ingresos
    FROM sales s
    JOIN products p ON s.ProductID = p.ProductID
    GROUP BY p.ProductName
    ORDER BY Ingresos DESC
    LIMIT limite;
END;
//
DELIMITER ;

-- CONSULTA AVANZADA: Top 3 ventas por ciudad (usando CTE + RANK)
WITH VentasConRanking AS (
    SELECT 
        c.CityName,
        s.TotalPrice,
        RANK() OVER (PARTITION BY c.CityName ORDER BY s.TotalPrice DESC) AS RankVenta
    FROM sales s
    JOIN customers cu ON s.CustomerID = cu.CustomerID
    JOIN cities c ON cu.CityID = c.CityID
)
SELECT * FROM VentasConRanking WHERE RankVenta <= 3;

-- ÍNDICES PARA OPTIMIZACIÓN
CREATE INDEX idx_customer_city ON customers (CityID);
CREATE INDEX idx_sale_customer ON sales (CustomerID);
CREATE INDEX idx_sale_product ON sales (ProductID);

-- Calcular TotalPrice automáticamente antes de insertar venta
DELIMITER //
CREATE TRIGGER calcular_total_price
BEFORE INSERT ON sales
FOR EACH ROW
BEGIN
    DECLARE precio_unitario FLOAT;
    SELECT Price INTO precio_unitario
    FROM products
    WHERE ProductID = NEW.ProductID;

    SET NEW.TotalPrice = (precio_unitario * NEW.Quantity) * (1 - NEW.Discount);
END;
//
DELIMITER ;

--------------------------------------------------
-- TRIGGER: Auditar eliminación de ventas
-------------------------------------------------
CREATE TABLE audit_ventas (
    SalesID INT,
    DeletedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    SalesPersonID INT,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    Discount FLOAT,
    TotalPrice FLOAT,
    SalesDate VARCHAR(20),
    TransactionNumber VARCHAR(50)
);

DELIMITER //
CREATE TRIGGER auditar_eliminacion_venta
BEFORE DELETE ON sales
FOR EACH ROW
BEGIN
    INSERT INTO audit_ventas
    VALUES (
        OLD.SalesID, NOW(), OLD.SalesPersonID, OLD.CustomerID,
        OLD.ProductID, OLD.Quantity, OLD.Discount,
        OLD.TotalPrice, OLD.SalesDate, OLD.TransactionNumber
    );
END;
//
DELIMITER ;

------------------------------------------------------
-- TRIGGER: Normalizar nombres al insertar clientes
------------------------------------------------------

DELIMITER //
CREATE TRIGGER normalizar_nombres_cliente
BEFORE INSERT ON customers
FOR EACH ROW
BEGIN
    SET NEW.FirstName = CONCAT(UCASE(LEFT(NEW.FirstName,1)), LCASE(SUBSTRING(NEW.FirstName,2)));
    SET NEW.LastName = CONCAT(UCASE(LEFT(NEW.LastName,1)), LCASE(SUBSTRING(NEW.LastName,2)));
END;
//
DELIMITER ;
