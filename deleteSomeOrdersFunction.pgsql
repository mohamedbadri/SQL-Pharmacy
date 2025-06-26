CREATE OR REPLACE FUNCTION deleteSomeOrdersFunction(maxOrderDeletions INT)
RETURNS INT AS
$$
DECLARE
    ordersDeleted INT := 0;
    rowCount INT := 0;
    supplierRow RECORD;
BEGIN
    IF maxOrderDeletions <= 0 THEN
        RETURN -1;
    END IF;

    FOR supplierRow IN
        SELECT s.supplierID
        FROM Supplier s
        JOIN OrderSupply o ON s.supplierID = o.supplierID
        WHERE o.orderDate <= DATE '2024-01-05' AND o.status = 'cnld'
        GROUP BY s.supplierID, s.supplierName
        ORDER BY COUNT(*) DESC, s.supplierName ASC
    LOOP
        DELETE FROM OrderSupply
        WHERE supplierID = supplierRow.supplierID
          AND orderDate > DATE '2024-01-05';

        GET DIAGNOSTICS rowCount = ROW_COUNT;

        IF ordersDeleted + rowCount > maxOrderDeletions THEN
            RETURN ordersDeleted;
        END IF;

        ordersDeleted := ordersDeleted + rowCount;

        IF ordersDeleted >= maxOrderDeletions THEN
            RETURN ordersDeleted;
        END IF;
    END LOOP;

    RETURN ordersDeleted;
END;
$$ LANGUAGE plpgsql;
