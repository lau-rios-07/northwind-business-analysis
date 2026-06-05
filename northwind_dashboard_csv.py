from main import df_power_bi as power_bi_table



power_bi_table["Revenue"] = power_bi_table["Revenue"].round(2)




power_bi_table.to_csv(
    "power_bi_table.csv",
    index=False,
    sep=";",
    decimal=","
)
