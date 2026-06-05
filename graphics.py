import matplotlib.pyplot as plt
import seaborn as sns

def graphics_high_value_customers(df):
    sns.barplot(x="CustomerName", y="TotalSpent", data=df)
    plt.title("Top 10 High-Value Customers")
    plt.xlabel("Customers")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def graphics_top_categories_revenue(df):
    sns.barplot(x="CategoryName", y="Revenue", data=df)
    plt.title("Top Revenue Categories")
    plt.xlabel("Categories")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def graphics_top_employees_by_revenue(df):
    sns.barplot(x="EmployeeName", y="Revenue", data=df)
    plt.title("10 more effective employees")
    plt.xlabel("Employees")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def graphics_top_countries_by_revenue(df):
    sns.barplot(x="Country", y="Revenue", data=df)
    plt.title("Top Revenue Countries")
    plt.xlabel("Countries")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
