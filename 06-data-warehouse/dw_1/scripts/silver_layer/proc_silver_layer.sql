TRUNCATE TABLE silver.crm_cst_info;

INSERT INTO silver.crm_cst_info (
	cst_id,
	cst_key,
	cst_firstname,
	cst_lastname,
	cst_material_status,
	cst_gender,
	cst_create_date
)
SELECT
	cst_id,
	cst_key,
	TRIM(cst_firstname) AS cst_firstname,  -- Remove Unwanted Trailing Spaces
	TRIM(cst_lastname) AS cst_lastname,
	CASE
		WHEN UPPER(TRIM(cst_material_status)) = 'M' THEN 'Married'
		WHEN UPPER(TRIM(cst_material_status)) = 'S' THEN 'Single'
		ELSE 'n/a'
	END AS cst_material_status,  -- Data Normalization & Standardization
	CASE
		WHEN UPPER(TRIM(cst_gender)) = 'F' THEN 'Female'
		WHEN UPPER(TRIM(cst_gender)) = 'M' THEN 'Male'
		ELSE 'n/a'
	END AS cst_gender,
	cst_create_date
FROM
(SELECT  -- Remove Duplicates
	*,
	ROW_NUMBER() OVER (PARTITION BY cst_id ORDER BY cst_create_date DESC) AS flag_last
FROM bronze.crm_cst_info)
WHERE flag_last = 1;  -- Select the most recent record per customer

TRUNCATE TABLE silver.crm_prd_info;

INSERT INTO silver.crm_prd_info (
	prd_id,
	cat_id,
	prd_key,
	prd_nm,
	prd_cost,
	prd_line,
	prd_start_dt,
	prd_end_dt
)
SELECT
	prd_id,
	REPLACE(SUBSTR(prd_key, 1, 5), '-', '_') AS cat_id,  -- Extract category ID
	SUBSTR(prd_key, 7, LENGTH(prd_key)) AS prd_key,  -- Extract product key
	prd_nm,
	COALESCE(prd_cost, 0) AS prd_cost,  -- Null or Negative Numbers
	CASE
		WHEN UPPER(TRIM(prd_line)) = 'M' THEN 'Mountain'
		WHEN UPPER(TRIM(prd_line)) = 'R' THEN 'Road'
		WHEN UPPER(TRIM(prd_line)) = 'S' THEN 'Other Sales'
		WHEN UPPER(TRIM(prd_line)) = 'T' THEN 'Touring'
		ELSE 'n/a'
	END AS prd_line,  -- Data product line Normalization & Standardization
	(prd_start_dt):: DATE AS prd_start_dt,
	(LEAD(prd_start_dt) OVER (PARTITION BY prd_key ORDER BY prd_start_dt) - INTERVAL '1 days'):: DATE AS prd_end_dt  -- Calculate end date as one day before the next start date
FROM bronze.crm_prd_info;

TRUNCATE TABLE silver.crm_sales_details;

INSERT INTO silver.crm_sales_details (
	sls_ord_num,
	sls_prd_key,
	sls_cust_id,
	sls_order_dt,
	sls_ship_dt,
	sls_due_dt,
	sls_sales,
	sls_quantity,
	sls_price
)
SELECT
	sls_ord_num,
	sls_prd_key,
	sls_cust_id,
	CASE
		WHEN sls_order_dt <= 0 OR LENGTH(sls_order_dt:: VARCHAR) <> 8 THEN NULL
		ELSE (sls_order_dt:: VARCHAR):: DATE
	END AS sls_order_dt,
	CASE
		WHEN sls_ship_dt <= 0 OR LENGTH(sls_order_dt:: VARCHAR) <> 8 THEN NULL
		ELSE (sls_ship_dt:: VARCHAR):: DATE
	END AS sls_ship_dt,
	CASE
		WHEN sls_due_dt <= 0 OR LENGTH(sls_order_dt:: VARCHAR) <> 8 THEN NULL
		ELSE (sls_due_dt:: VARCHAR):: DATE
	END AS sls_due_dt,
	CASE
		WHEN sls_sales <> sls_quantity * ABS(sls_price) OR sls_sales <= 0 OR sls_sales IS NULL
			THEN sls_quantity * ABS(sls_price)
		ELSE sls_sales
	END AS sls_sales,
	sls_quantity,
	CASE
		WHEN sls_price <= 0 OR sls_price IS NULL
			THEN sls_sales / NULLIF(sls_quantity, 0)
		ELSE sls_price
	END AS sls_price
FROM bronze.crm_sales_details;