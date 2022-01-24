"""
author: evan fedorko, evanjfedorko@gmail.com
date: 6/2021

this script was written to help a client migrate their customer list from one CRM
(Local Food Marketplace) to another (Reserva)
"""

import pandas as pan
import os

# workspace, target table, template of output
ws = os.getcwd()
inCSV = ws + "ToProcess2.csv"
outCSV = ws + "output.csv"
outTemplate = ws + "template.csv"

# read input table as pandas data frame type
dfIn = pan.DataFrame(pan.read_csv(inCSV))
dfTemp = pan.DataFrame(pan.read_csv(outTemplate))
# this creates an empty data frame with the same structure as the source data frame
dfOut = pan.DataFrame(data=None, columns=dfTemp.columns)  # , index=df.index)
# this (should) set the dfTemp dataframe to null to release it's contents from memory
dfTemp = pan.DataFrame()

# add needed fields
newFields = ["Default Location", "Route"]
for item in newFields:
    shape = dfOut.shape
    position = int(shape[1])
    dfOut.insert(position, item, [], False)
for index, row in dfIn.iterrows():
    # check if these two are not equal, and if so, make the "company" record
    if row['Name'] != row['business name']:
        record1 = {
            "Is a company": "TRUE",
            "customer": row["customer"],
            "supplier": row["supplier"],
            "Name": row["business name"],
            "Parent Company": "",
            "Address type": "Default",
            "street": row["street"],
            "street2": row["street2"],
            "city": row["city"],
            "state": row["state"],
            "zip": row["zip"],
            "country": row["country"],
            "email": row["email"],
            "phone": row["phone"],
            "fax": row["fax"],
            "mobile": row["mobile"],
            "credit_limit": row["credit_limit"],
            "debit_limit": row["debit_limit"],
            "website": row["website"],
            "Default Location": row["Default Location"],
            "Route": row["Route"]
        }

        dfOut.loc[len(dfOut.index)] = record1

        # and then make a record for the individual w/reference to parent company
        record2 = {
            "Is a company": "FALSE",
            "customer": row["customer"],
            "supplier": row["supplier"],
            "Name": row["Name"],
            "Parent Company": row["business name"],
            "Address type": "Shipping",
            "street": row["street"],
            "street2": row["street2"],
            "city": row["city"],
            "state": row["state"],
            "zip": row["zip"],
            "country": row["country"],
            "email": row["email"],
            "phone": row["phone"],
            "fax": row["fax"],
            "mobile": row["mobile"],
            "credit_limit": row["credit_limit"],
            "debit_limit": row["debit_limit"],
            "website": row["website"],
            "Default Location": row["Default Location"],
            "Route": row["Route"]
        }

        dfOut.loc[len(dfOut.index)] = record2

    else:
        # otherwise just make a record
        record2 = {
            "Is a company": "TRUE",
            "customer": row["customer"],
            "supplier": row["supplier"],
            "Name": row["business name"],
            "Parent Company": "",
            "Address type": "Default",
            "street": row["street"],
            "street2": row["street2"],
            "city": row["city"],
            "state": row["state"],
            "zip": row["zip"],
            "country": row["country"],
            "email": row["email"],
            "phone": row["phone"],
            "fax": row["fax"],
            "mobile": row["mobile"],
            "credit_limit": row["credit_limit"],
            "debit_limit": row["debit_limit"],
            "website": row["website"],
            "Default Location": row["Default Location"],
            "Route": row["Route"]
        }
        dfOut.loc[len(dfOut.index)] = record2

dfOut.to_csv(outCSV, index=True)
