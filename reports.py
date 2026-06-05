def report_northwind_txt(customers_data, categories_data, employees_data, countries_data):
    with open("Northwind Business Analysis v1\\report_northwind.txt", "w", encoding="UTF-8") as archive_txt:
        archive_txt.write(f'''
                        EXECUTIVE SUMMARY\n\n\n
                        This report analyzes customer spending, product category performance,
                        employee sales performance, and revenue distribution by country
                        using the Northwind database.\n

                        The objective is to identify key revenue drivers and provide
                        business recommendations based on the available data.\n\n\n
                        CUSTOMER ANALYSIS\n\n\n
                        The top 3 customers accounted for {customers_data["top_3_customer_percentage"]:.2f}% of the total revenue.\n
                        indicating that a significant portion of sales comes from a small
                        group of strategic customers.\n

                        The highest-value customer was {customers_data["top_customer_name"]}, generating ${customers_data["top_customer_revenue"]} and representing
                        {customers_data["top_customer_percentage"]:.2f}% of the total revenue analyzed.\n

                        Additionally, The average customer spending is ${customers_data["average_customer_spending"]}\n\n\n
                        CATEGORY ANALYSIS\n\n\n
                        The category with the highest revenue was {categories_data["top_category_name"]}.\n

                        This category generated ${categories_data["top_category_revenue"]} and represented {categories_data["top_category_percentage"]:.2f}% of the total category revenue.\n

                        This suggests that the category plays a major role in the company's
                        overall sales performance.\n\n\n
                        EMPLOYEE ANALYSIS\n\n\n
                        The highest-performing employee was {employees_data["top_employee_name"]}.\n

                        This employee generated ${employees_data["top_employee_revenue"]} and contributed {employees_data["top_employee_percentage"]:.2f}% of the total employee revenue analyzed.\n

                        The top five employees represented {employees_data["top_5_employee_percentage"]:.2f}% of total revenue,
                        showing that sales performance is concentrated among a limited
                        group of employees.\n\n\n
                        GEOGRAPHIC ANALYSIS\n\n\n
                        The country with the highest revenue was {countries_data["top_country_name"]}.\n

                        This market generated ${countries_data["top_country_revenue"]} and accounted for {countries_data["top_country_percentage"]:.2f}% of the revenue analyzed.\n

                        The results suggest that this country represents one of the company's
                        most important markets.\n\n\n
                        RECOMMENDATIONS\n\n\n
                        Maintain strong relationships with high-value customers.\n\n

                        Increase investment in top-performing categories.\n\n

                        Study the sales strategies of top-performing employees.\n\n

                        Strengthen marketing efforts in high-revenue countries.\n\n

                        Monitor revenue concentration to reduce dependence on a small number of customers.\n\n\n\n
                        FINAL CONCLUSION\n\n\n
                        The analysis identified the main customers, categories, employees,
                        and countries responsible for generating revenue.

                        These findings can help the company focus resources on its strongest
                        areas while improving opportunities in lower-performing segments.
                        ''')


