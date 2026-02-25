/*
===============================================================================
Data Quality Check: Bronze Layer
===============================================================================
Script Purpose:
    This script performs data quality validation checks on the
    Bronze layer before loading data into the Silver layer.

Checks Performed:
    - NULL and Duplicate Primary Key check
    - Unwanted leading/trailing spaces
    - Empty string validation
    - Data standardization (Gender & Marital Status)
    - Invalid or future date validation
    - Summary statistics overview

Usage:
    Run this script before executing the Silver load process.
===============================================================================
*/

-- ============================================================================
-- 1. Bronze - crm_cst_info Table
-- ============================================================================

SELECT  -- Check for Nulls or Duplicates in Primary Key
	cst_id,
	COUNT(*)
FROM bronze.crm_cst_info
GROUP BY cst_id
HAVING COUNT(*) > 1 OR cst_id IS NULL;

SELECT cst_firstname  -- Check For Unwanted Spaces
FROM bronze.crm_cst_info
WHERE cst_firstname <> TRIM(cst_firstname);

SELECT cst_lastname  -- Check For Unwanted Spaces
FROM bronze.crm_cst_info
WHERE cst_lastname <> TRIM(cst_lastname);

SELECT DISTINCT cst_gender  -- Gender Check Data Standardization & Consistency
FROM bronze.crm_cst_info;

SELECT DISTINCT cst_material_status  --  Data Standardization & Consistency
FROM bronze.crm_cst_info;

-- ============================================================================
-- 2. Bronze - crm_prd_info Table
-- ============================================================================

SELECT  -- Check for Nulls or Duplicates in Primary Key
	prd_id,
	COUNT(*)
FROM bronze.crm_prd_info
GROUP BY prd_id
HAVING COUNT(*) > 1 OR prd_id IS NULL;

SELECT prd_nm  -- Check for Unwanted Spaces
FROM bronze.crm_prd_info
WHERE prd_nm <> TRIM(prd_nm);

SELECT prd_cost  -- Check for Nulls or Negative Numbers
FROM bronze.crm_prd_info
WHERE prd_cost < 0 OR prd_cost IS NULL;

SELECT DISTINCT prd_line  -- Data Standardization & Consistency
FROM bronze.crm_prd_info;

SELECT *  -- Check for Invalid Date Orders
FROM bronze.crm_prd_info
WHERE prd_end_dt < prd_start_dt;

-- ============================================================================
-- 3. Bronze - crm_sales_details Table
-- ============================================================================

SELECT sls_ord_num  -- Check for Unwanted Trailing Spaces
FROM bronze.crm_sales_details
WHERE sls_ord_num <> TRIM(sls_ord_num);

SELECT sls_prd_key  -- Relational Integrity Check
FROM bronze.crm_sales_details
WHERE sls_prd_key NOT IN (
	SELECT prd_key
	FROM silver.crm_prd_info
);

SELECT sls_cust_id  -- Relational Integrity Check
FROM bronze.crm_sales_details
WHERE sls_cust_id NOT IN (
	SELECT cst_id
	FROM silver.crm_cst_info
);

SELECT sls_order_dt  -- Check for Invalid Date
FROM bronze.crm_sales_details
WHERE sls_order_dt <= 0
OR LENGTH(sls_order_dt:: VARCHAR) <> 8
OR sls_order_dt > 20500101
OR sls_order_dt < 19000101;

SELECT sls_ship_dt  -- Check for Invalid Date
FROM bronze.crm_sales_details
WHERE sls_ship_dt <= 0
OR LENGTH(sls_ship_dt:: VARCHAR) <> 8
OR sls_ship_dt > 20500101
OR sls_ship_dt < 19000101;

SELECT sls_due_dt  -- Check for Invalid Date
FROM bronze.crm_sales_details
WHERE sls_due_dt <= 0
OR LENGTH(sls_due_dt:: VARCHAR) <> 8
OR sls_due_dt > 20500101
OR sls_due_dt < 19000101;

SELECT *  -- Check for Invalid Date Orders
FROM bronze.crm_sales_details
WHERE sls_order_dt > sls_ship_dt OR sls_order_dt > sls_due_dt;

SELECT DISTINCT    -- Check Data Consistency: Between Sales, Quantity, & Price
	sls_sales,     -- Sales = Quantity * Price
	sls_quantity,  -- Values must not be Null, Zero, & Negative.
	sls_price
FROM bronze.crm_sales_details
WHERE sls_sales <> sls_quantity * sls_price
OR sls_sales IS NULL OR sls_quantity is NULL OR sls_price is NULL
OR sls_sales <= 0 OR sls_quantity <= 0 OR sls_price <= 0
ORDER BY sls_sales DESC, sls_quantity DESC, sls_price DESC;

-- ============================================================================
-- 4. Bronze - erp_cust_az12 Table
-- ============================================================================

SELECT DISTINCT bdate  -- Check Range of Dates
FROM bronze.erp_cust_az12
WHERE bdate < '1926-01-01' OR bdate > CURRENT_DATE;

SELECT DISTINCT gen  -- Data Standardization & Consistency
FROM bronze.erp_cust_az12;

-- ============================================================================
-- 5. Bronze - erp_cust_az12 Table
-- ============================================================================

SELECT DISTINCT country  -- Data Standardization & Consistency
FROM bronze.erp_loc_a101
ORDER BY country;

-- ============================================================================
-- 6. Bronze - erp_px_cat_g1v2 Table
-- ============================================================================

SELECT cat  -- Check for unwanted trailing spaces
FROM bronze.erp_px_cat_g1v2
WHERE cat <> TRIM(cat);

SELECT subcat  -- Check for unwanted trailing spaces
FROM bronze.erp_px_cat_g1v2
WHERE subcat <> TRIM(subcat);

SELECT maintenance  -- Check for unwanted trailing spaces
FROM bronze.erp_px_cat_g1v2
WHERE maintenance <> TRIM(maintenance);

SELECT DISTINCT cat  -- Data Standardization & Consistency
FROM bronze.erp_px_cat_g1v2;

SELECT DISTINCT subcat  -- Data Standardization & Consistency
FROM bronze.erp_px_cat_g1v2;

SELECT DISTINCT maintenance  -- Data Standardization & Consistency
FROM bronze.erp_px_cat_g1v2;