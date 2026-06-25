/* What are the 10 most expensive products in the company? */

SELECT 
	PRODUCT_NAME AS Product
	,PRODUCT_VAL AS Value
FROM data_product
ORDER BY PRODUCT_VAL DESC
LIMIT 10


/* What sections do the 'BEBIDAS' and 'PADARIA' departments have? */

SELECT DISTINCT 
	DEP_NAME AS Department
,	SECTION_NAME AS Section
FROM data_product
WHERE DEP_NAME IN ('BEBIDAS', 'PADARIA')
ORDER BY DEP_NAME

/* What was the total sale of products (in $) of each Business Area in the first quarter of 2019? */

SELECT 
	t2.BUSINESS_NAME AS 'Business Area'
,	SUM(t1.SALES_VALUE) AS 'Total Sale'
FROM data_product_sales t1
LEFT JOIN data_store_cad t2 ON t1.STORE_CODE = t2.STORE_CODE 
WHERE 1=1 
	AND t1.`DATE` >= '2019-01-01'
	AND t1.`DATE` < '2019-04-01'
GROUP BY t2.BUSINESS_NAME
ORDER BY SUM(t1.SALES_VALUE) DESC






