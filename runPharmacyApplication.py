#! /usr/bin/env python

#  runPharmacyApplication Solution

import psycopg2, sys, datetime

# --------------------------------------------------------------------------
def countNumberOfCustomers(conn, thePharmacyID):
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM Pharmacy WHERE pharmacyID = %s", (thePharmacyID,))
    if cur.fetchone() is None:
        return -1
    cur.execute("""
        SELECT COUNT(DISTINCT customerID)
        FROM Purchase
        WHERE pharmacyID = %s
    """, (thePharmacyID,))
    result = cur.fetchone()
    return result[0] if result else 0

# --------------------------------------------------------------------------
def updateOrderStatus(conn, currentYear):
    if currentYear < 2000 or currentYear > 2030:
        return -1
    cur = conn.cursor()
    cur.execute("""
        UPDATE OrderSupply
        SET status = status || ' AS OF ' || %s
        WHERE status != 'cnld'
    """, (str(currentYear),))
    return cur.rowcount

# --------------------------------------------------------------------------
def deleteSomeOrders(conn, maxOrderDeletions):
    try:
        cur = conn.cursor()
        cur.execute("SELECT deleteSomeOrdersFunction(%s)", (maxOrderDeletions,))
        result = cur.fetchone()
        cur.close()
        return result[0]
    except:
        print("Call of deleteSomeOrdersFunction with argument", maxOrderDeletions, "had error", file=sys.stderr)
        cur.close()
        conn.close()
        sys.exit(-1)

# --------------------------------------------------------------------------
def main():
    port = "5432"
    userID = "cse182"
    pwd = "database4me"

    try:
        conn = psycopg2.connect(port=port, user=userID, password=pwd)
    except:
        print("Connection to database failed", file=sys.stderr)
        sys.exit(-1)

    conn.autocommit = True

    # -------------------------------
    # Tests for countNumberOfCustomers
    for pid in [11, 17, 44, 66]:
        result = countNumberOfCustomers(conn, pid)
        if result >= 0:
            print(f"Number of customers for pharmacy {pid} is {result}\n")
        else:
            print(f"ERROR: Pharmacy {pid} does not exist\n")

    # -------------------------------
    # Tests for updateOrderStatus
    for year in [1999, 2025, 2031]:
        result = updateOrderStatus(conn, year)
        if result == -1:
            print(f"ERROR: Invalid year {year} for updateOrderStatus\n")
        else:
            print(f"Number of orders whose status values were updated by updateOrderStatus is {result}\n")

    # -------------------------------
    # Tests for deleteSomeOrders
    for val in [2, 4, 3, 1]:
        result = deleteSomeOrders(conn, val)
        if result >= 0:
            print(f"Number of orders which were deleted for maxOrderDeletions value {val} is {result}\n")
        else:
            print(f"ERROR: Could not delete orders for maxOrderDeletions value {val}\n")

    conn.close()
    sys.exit(0)

# --------------------------------------------------------------------------
if __name__ == '__main__':
    main()
    

