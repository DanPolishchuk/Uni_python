import pandas as pd

df1 = pd.read_csv("c:/lab5/orders.csv")
task1 = df1[(df1["ship_mode"] == "First") & ((df1["order_date"].str.contains("2016")) |
                                            (df1["order_date"].str.contains("2017")))]
print("Task 1", "\nAmount of orders that were sent first class for 2016-2017: ", task1.shape[0])

df2 = pd.read_csv("c:/lab5/customers.csv")
task2 = df2[(df2["state"] == "California") & (df2["segment"] == "Consumer")]
print("\nTask 2", "\nAmount of California customers in the database: ", task2.shape[0])

cali_cust = [task2["id"].values]
all_cust = [df1["customer_id"].values]
all_cust = list(set(all_cust[0]))
cali_orders = []
for i in range(len(all_cust)):
    if all_cust[i] in cali_cust[0]:
        x = df1[df1["customer_id"] == all_cust[i]].shape[0]
        cali_orders.append(x)
print("\nTask 3\nAmount of orders from California customers: ", sum(cali_orders))

df1.rename(columns={"id": "order_id", "customer_id": "id"}, inplace=True)
df3 = pd.merge(df1, df2, on=["id"], how="inner")
df3["order_date"] = pd.to_datetime(df3["order_date"])
df3["Year"] = df3["order_date"].dt.year
task4 = df3.pivot_table(values="sales", index="state", columns="Year", aggfunc="mean", margins=False, dropna=True,
                        fill_value=None)
print("\nTask4\nAverage order receipt across all states for each year:\n")
print(task4)
