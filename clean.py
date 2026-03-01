import pandas as pd

data = pd.read_csv("messy_dataset.csv")



#########
data.columns = (
    data.columns
    .str.lower()
    .str.strip()
    .str.replace(" ", "_")
)
#########

#########
date_columns = ["ship_date", "orderdate"]

for column in date_columns:
    data[column] = pd.to_datetime(data[column], errors='coerce')
#########

#########
cash_columns = ["unit_price", "shippingcost", "order_total"]

for cols in cash_columns:
    data[cols] = (
        data[cols]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace("USD", "", regex=False)
        .str.strip()
    )
    data[cols] = pd.to_numeric(data[cols], errors='coerce')
#########

#########
data["taxrate"] = (data["taxrate"]
                      .astype(str)
                      .str.replace("%", "", regex=False)
                      .str.strip()
                      )
data["taxrate"] = pd.to_numeric(data["taxrate"], errors='coerce')
data.loc[data["taxrate"] > 1, "taxrate"] = data["taxrate"] / 100
#########

#########
data["quantity"] = pd.to_numeric(data["quantity"], errors="coerce")
data["quantity"] = data["quantity"].fillna(1)
#########

#########
data = data.drop_duplicates()
#########


print(data.head(10))