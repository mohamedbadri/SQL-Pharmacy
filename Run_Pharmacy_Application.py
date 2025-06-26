#! /usr/bin/env python

#  runPharmacyApplication Solution

import psycopg2, sys, datetime

# The three Python functions for Lab4 should appear below.
# Write those functions, as described in Lab4 Section 4 (and Section 5,
# which describes the Stored Function used by the third Python function).
#
# Write the tests of those function in main, as described in Section 6
# of Lab4.


 # countNumberOfCustomers (myConn, thePharmacyID):
 # The Purchase table tells us about purchases made by a customer (customerID) in a pharmacy (pharmacyID).
 #
 # Besides the database connection, the countNumberOfCustomers function has one parameter, an
 # integer, thePharmacyID.
 #
 # countNumberOfCustomers counts the number of different customers that the pharmacy with thePharmacyID has,
 # based on the number of different customerID values that appears in the Purchase table.
 #
 # countNumberOfCustomers returns that value.
 #
 # For more details, including error handling and return codes, see the Lab4 pdf.

def countNumberOfCustomers (myConn, thePharmacyID):
    pass

    # Python function to be supplied by students

# end countNumberOfCustomers


# updateOrderStatus (myConn, currentYear):
# In the OrderSuppy table, the value of status is either 'dlvd' (delivered), 'pndg' (pending), or 'cnld' (cancelled). 
#
# Besides the database connection, updateOrderStatus has another parameter, currentYear, which is an integer.
# If currentYear is between 2000 and 2030 (inclusive), then updateOrderStatus should append ' AS OF <currentYear>' at the end of the status value
# if status is not 'cnld'.
# Other values of currentYear are errors.
#
# updateOrderStatus should return the number of orders whose status values were updated.
#
# For more details, including error handling, see the Lab4 pdf.

def updateOrderStatus (myConn, currentYear):
    pass
    
    # Python function to be supplied by students
    # You'll need to figure out value to return.

# end updateOrderStatus


# deleteSomeOrders (myConn, maxOrderDeletions):
# Besides the database connection, this Python function has one other parameter,
# maxOrderDeletions, which is an integer.
#
# deleteSomeOrders invokes a Stored Function, deleteSomeOrdersFunction, that you will need to
# implement and store in the database according to the description in Section 5.  The Stored
# Function deleteSomeOrdersFunction has all the same parameters as deleteSomeOrders (except
# for the database connection, which is not a parameter for the Stored Function), and it returns
# an integer.
#
# Section 5 of the Lab4 tells you which orders to delete and explains the integer value
# that deleteSomeOrdersFunction returns.  The deleteSomeOrders Python function returns the
# the same integer value that the deleteSomeOrdersFunction Stored Function returns.
#
# deleteSomeOrdersFunction doesn’t print anything.  The deleteSomeOrders function must only
# invoke the Stored Function deleteSomeOrdersFunction, which does all of the work for this part
# of the assignment; deleteSomeOrders should not do any of the work itself.
#
# For more details, see the Lab4 pdf.

def deleteSomeOrders (myConn, maxOrderDeletions):

# We're giving you the code for deleteSomeOrders, but you'll have to write the
# Stored Function deleteSomeOrdersFunction yourselves in a PL/pgSQL file named
# deleteSomeOrdersFunction.pgsql
        
    try:
        myCursor = myConn.cursor()
        sql = "SELECT deleteSomeOrdersFunction(%s)"
        myCursor.execute(sql, (maxOrderDeletions, ))
    except:
        print("Call of deleteSomeOrdersFunction with argument", maxOrderDeletions, "had error", file=sys.stderr)
        myCursor.close()
        myConn.close()
        sys.exit(-1)
    
    row = myCursor.fetchone()
    myCursor.close()
    return(row[0])

#end deleteSomeOrders


def main():
    port = "5432"
    userID = "cse182"
    pwd = "database4me"

    # Try to make a connection to the database
    try:
        myConn = psycopg2.connect(port=port, user=userID, password=pwd)
    except:
        print("Connection to database failed", file=sys.stderr)
        sys.exit(-1)
        
    # We're making every SQL statement a transaction that commits.
    # Don't need to explicitly begin a transaction.
    # Could have multiple statement in a transaction, using myConn.commit when we want to commit.
    
    myConn.autocommit = True
    
    # There are other correct ways of writing all of these calls correctly in Python.
        
    # Perform tests of countNumberOfCustomers, as described in Section 6 of Lab4.
    # Print their outputs (including error outputs) here, not in countNumberOfCustomers.
    # You may use a Python method to help you do the printing.


    # Perform tests of updateOrderStatus, as described in Section 6 of Lab4.
    # Print their outputs (including error outputs) here, not in updateOrderStatus.
    # You may use a Python method to help you do the printing.
 
 
    # Perform tests of deleteSomeOrders, as described in Section 6 of Lab4,
    # Print their outputs (including error outputs) here, not in deleteSomeOrders.
    # You may use a Python method to help you do the printing.
  
  
    myConn.close()
    sys.exit(0)
#end

#------------------------------------------------------------------------------
if __name__=='__main__':

    main()

# end
