/*
===============================================================================
DQL Script: Data Quality Checks – Gold Layer Validation
===============================================================================
Script Purpose:

    This script performs data validation and quality checks to ensure that the 
    Gold layer (dimension and fact views) is accurate, consistent, and reliable.

    These checks validate:
    - Duplicate records
    - Data consistency across sources
    - Referential integrity between fact and dimension tables

Usage:
    - Run after creating Gold views.
    - Investigate any returned records as potential data issues.
===============================================================================
*/

-- =============================================================================
-- Check 1: Duplicate Customers
-- =============================================================================
SELECT cst_id, COUNT(*) AS duplicated  -- Check if any duplicates
FROM (
	SELECT
		ci.cst_id,
		ci.cst_key,
		ci.cst_firstname,
		ci.cst_lastname,
		ci.cst_marital_status,
		ci.cst_gender,
		ci.cst_create_date,
		ca.bdate,
		ca.gen,
		la.country
	FROM silver.crm_cst_info ci
	LEFT JOIN silver.erp_cust_az12 ca
	ON ci.cst_key = ca.cid
	LEFT JOIN silver.erp_loc_a101 la
	ON ci.cst_key = la.cid
)t GROUP BY cst_id
HAVING COUNT(*) > 1;

-- =============================================================================
-- Check 2: Gender Data Consistency
-- =============================================================================
SELECT DISTINCT  -- Data Consistency Check
	ci.cst_gender,
	ca.gen
FROM silver.crm_cst_info ci
LEFT JOIN silver.erp_cust_az12 ca
ON ci.cst_key = ca.cid
LEFT JOIN silver.erp_loc_a101 la
ON ci.cst_key = la.cid
ORDER BY 1, 2;

-- =============================================================================
-- Check 3: Duplicate Products
-- =============================================================================
SELECT prd_id, COUNT(*)  -- Check if any duplicates
FROM (
	SELECT
		pi.prd_id,
		pi.cat_id,
		pi.prd_key,
		pi.prd_nm,
		pi.prd_cost,
		pi.prd_line,
		pi.prd_start_dt,
		pe.cat,
		pe.subcat,
		pe.maintenance
	FROM silver.crm_prd_info pi
	LEFT JOIN silver.erp_px_cat_g1v2 pe
	ON pe.id = pi.cat_id
	WHERE pi.prd_end_dt IS NULL  -- Filter out all historical data
)t GROUP BY prd_id
HAVING COUNT(*) > 1;

-- =============================================================================
-- Check 4: Referential Integrity (Fact ↔ Dimensions)
-- =============================================================================
SELECT *  -- Foreign Key Integration Check
FROM gold.fact_sales fs
LEFT JOIN gold.dim_customers ct
ON ct.customer_key = fs.customer_key
LEFT JOIN gold.dim_products pd
ON pd.product_key = fs.product_key
WHERE ct.customer_key IS NULL OR pd.product_key IS NULL;