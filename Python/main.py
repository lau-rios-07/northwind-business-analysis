import sqlite3
import pandas as pd
from pathlib import Path


from queries import query_high_value_customers
from queries import query_top_categories_revenue
from queries import query_top_employees_by_revenue
from queries import query_top_revenue_by_country
from queries import query_revenue_total_by_country
from queries import query_categories_total_revenue
from queries import query_customers_total_revenue
from queries import query_total_revenue
from queries import query_power_bi

from graphics import graphics_high_value_customers
from graphics import graphics_top_categories_revenue
from graphics import graphics_top_employees_by_revenue
from graphics import graphics_top_countries_by_revenue

from analysis import customers_system
from analysis import categories_system
from analysis import employees_system
from analysis import countries_system

from reports import report_northwind_txt

DB_PATH = Path(__file__).parent.parent / "Northwind.db"

db_path = Path("..") / "Northwind Business Analysis v1" / "Northwind.db"

with sqlite3.connect(DB_PATH) as conn:
    df_high_value_customers = pd.read_sql_query(query_high_value_customers,conn)
    df_top_categories_revenue = pd.read_sql_query(query_top_categories_revenue,conn)
    df_top_employees_by_revenue = pd.read_sql_query(query_top_employees_by_revenue,conn)
    df_top_revenue_by_country = pd.read_sql_query(query_top_revenue_by_country,conn)
    df_revenue_by_country = pd.read_sql_query( query_revenue_total_by_country,conn)
    df_revenue_by_categories = pd.read_sql_query( query_categories_total_revenue,conn)
    df_customers_revenue = pd.read_sql_query( query_customers_total_revenue,conn)
    df_total_revenue = pd.read_sql_query( query_total_revenue,conn)
    df_power_bi = pd.read_sql_query( query_power_bi,conn)



# =========================
# HIGH VALUE COSTUMERS ANALYSIS
# =========================



print(df_high_value_customers)

customers_data = customers_system(
    df_high_value_customers,
    df_total_revenue["TotalRevenue"].iloc[0]
)


graphics_high_value_customers(df_high_value_customers)



# =========================
# TOP CATEGORIES ANALYSIS
# =========================



print(df_top_categories_revenue)

categories_data = categories_system(df_top_categories_revenue)


graphics_top_categories_revenue(df_top_categories_revenue)



# =========================
# TOP EMPLOYEES BY REVENUE ANALYSIS
# =========================


print(df_top_employees_by_revenue)

employees_data = employees_system(df_top_employees_by_revenue)


graphics_top_employees_by_revenue(df_top_employees_by_revenue)



# =========================
# TOP REVENUE BY COUNTRY ANALYSIS
# =========================


print(df_top_revenue_by_country)

countries_data = countries_system(
    df_top_revenue_by_country,
    df_total_revenue["TotalRevenue"].iloc[0]
)



graphics_top_countries_by_revenue(df_top_revenue_by_country)



# =========================
# REPORT
# =========================

report_northwind_txt(customers_data, categories_data, employees_data, countries_data)