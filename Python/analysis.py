def customers_system(dataframe, total_revenue):
    total_revenue_customers = dataframe["TotalSpent"].sum()
    average_customer_spending = dataframe["TotalSpent"].mean()
    top_customer_revenue = dataframe["TotalSpent"].max()
    top_customer_name = dataframe.loc[dataframe["TotalSpent"].idxmax(),"CustomerName"]
    top_customer_percentage = (top_customer_revenue / total_revenue) * 100
    top_3_revenue = dataframe["TotalSpent"].head(3).sum()
    top_3_customer_percentage = (top_3_revenue / total_revenue) * 100
    return {
        "total_revenue_customers": total_revenue_customers,
        "average_customer_spending": average_customer_spending,
        "top_customer_revenue": top_customer_revenue,
        "top_customer_name": top_customer_name,
        "top_customer_percentage": top_customer_percentage,
        "top_3_customer_percentage": top_3_customer_percentage
    }


def categories_system(dataframe):
    total_revenue_categories = dataframe["Revenue"].sum()
    average_category_revenue = dataframe["Revenue"].mean()
    top_category_revenue = dataframe["Revenue"].max()
    top_category_name = dataframe.loc[dataframe["Revenue"].idxmax(), "CategoryName"]
    top_category_percentage = (top_category_revenue / total_revenue_categories) * 100
    return {
        "total_revenue_categories": total_revenue_categories,
        "average_category_revenue": average_category_revenue,
        "top_category_revenue": top_category_revenue,
        "top_category_name": top_category_name,
        "top_category_percentage": top_category_percentage
    } 


def employees_system(dataframe):
    total_revenue_employees = dataframe["Revenue"].sum()
    average_employee_revenue = dataframe["Revenue"].mean()
    top_employee_revenue = dataframe["Revenue"].max()
    top_employee_name = dataframe.loc[dataframe["Revenue"].idxmax(), "EmployeeName"]
    top_employee_percentage = (top_employee_revenue / total_revenue_employees) * 100
    top_5_revenue = dataframe["Revenue"].head(5).sum()
    top_5_employee_percentage = (top_5_revenue / total_revenue_employees) * 100
    return {
        "total_revenue_employees": total_revenue_employees,
        "average_employee_revenue": average_employee_revenue,
        "top_employee_revenue": top_employee_revenue,
        "top_employee_name": top_employee_name,
        "top_employee_percentage": top_employee_percentage,
        "top_5_employee_percentage": top_5_employee_percentage
    } 


def countries_system(dataframe, total_revenue):
    total_revenue_countries = dataframe["Revenue"].sum()
    average_country_revenue = dataframe["Revenue"].mean()
    top_country_revenue = dataframe["Revenue"].max()
    top_country_name = dataframe.loc[dataframe["Revenue"].idxmax(), "Country"]
    top_country_percentage = (top_country_revenue / total_revenue) * 100
    return {
        "total_revenue_countries": total_revenue_countries,
        "average_country_revenue": average_country_revenue,
        "top_country_revenue": top_country_revenue,
        "top_country_name": top_country_name,
        "top_country_percentage": top_country_percentage
    } 

