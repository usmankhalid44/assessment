from pyspark.sql import SparkSession
from pyspark.sql.functions import month, year,sum as spark_sum,avg

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Monthly Active Users") \
    .getOrCreate()

# Monthly Active Users (MAU) for January 2024: Count of unique users active in January 2024.
customer_purchases = spark.table("CustomerPurchases")
customer_purchases = customer_purchases.withColumn("purchase_date", customer_purchases["purchase_date"].cast("date"))
january_2024_purchases = customer_purchases.filter((year("purchase_date") == 2024) & (month("purchase_date") == 1))
january_2024_mau = january_2024_purchases.select("customer_id").distinct().count()
print("Monthly Active Users (MAU) for January 2024:", january_2024_mau)


# Total Sales Revenue for January 2024: Sum of sales in January 2024.
sales = spark.table("Sales")
sales = sales.withColumn("sale_date", sales["sale_date"].cast("date"))
january_2024_sales = sales.filter((year("sale_date") == 2024) & (month("sale_date") == 1))
total_sales_revenue_january_2024 = january_2024_sales.select(spark_sum("amount")).collect()[0][0]
print("Total Sales Revenue for January 2024:", total_sales_revenue_january_2024)


# Average Sale Amount Per Category for January 2024:Average sale amount per category in January 2024.
products = spark.table("Products")
joined_data = sales.join(products, sales["product_id"] == products["product_id"], "inner")
january_2024_sales = joined_data.filter((year("sale_date") == 2024) & (month("sale_date") == 1))
average_sale_per_category_january_2024 = january_2024_sales.groupBy("category_id").agg(avg("amount").alias("average_sale_amount"))
average_sale_per_category_january_2024.show()


# Number of New Users in January 2024: Count of users who joined in January 2024.
users = spark.table("Users")
users = users.withColumn("join_date", users["join_date"].cast("date"))
new_users_january_2024 = users.filter((year("join_date") == 2024) & (month("join_date") == 1))
number_of_new_users_january_2024 = new_users_january_2024.count()
print("Number of New Users in January 2024:", number_of_new_users_january_2024)

# Top Selling Product Category in January 2024: Product category with highest sales in
# January 2024.
categories = spark.table("Categories")
sales_by_category = january_2024_sales.groupBy("category_id").agg(spark_sum("amount").alias("total_sales_amount"))
top_selling_product_category = sales_by_category.orderBy("total_sales_amount", ascending=False).first()[0]
top_selling_product_category = top_selling_product_category.join(categories, sales["category_id"] == products["category_id"], "inner")
top_selling_product_category.show()