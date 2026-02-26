/*
===============================================================================
Stored Procedure: Load Silver Layer (Bronze -> Silver)
===============================================================================
Script Purpose:
    This stored procedure performs the ETL (Extract, Transform, Load) process to 
    populate the 'silver' schema tables from the 'bronze' schema.
	Actions Performed:
		- Truncates Silver tables.
		- Inserts transformed and cleansed data from Bronze into Silver tables.
		
Parameters:
    None. 
	  This stored procedure does not accept any parameters or return any values.

Usage Example:
    CALL silver.load_silver_layer();
===============================================================================
*/

CREATE EXTENSION IF NOT EXISTS plpgsql;

DROP PROCEDURE IF EXISTS silver.load_silver_layer;

CREATE OR REPLACE PROCEDURE silver.load_silver_layer()
LANGUAGE plpgsql
AS $$
DECLARE
	start_time TIMESTAMP;
	end_time TIMESTAMP;
	batch_start_time TIMESTAMP;
	batch_end_time TIMESTAMP;
BEGIN
	batch_start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '================================================';
    RAISE NOTICE 'Loading Silver Layer';
    RAISE NOTICE '================================================';

	RAISE NOTICE '------------------------------------------------';
	RAISE NOTICE 'Loading CRM Tables';
	RAISE NOTICE '------------------------------------------------';

    start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '>> Truncating Table: silver.crm_cst_info';
	TRUNCATE TABLE silver.crm_cst_info;
	RAISE NOTICE '>> Inserting Data Into: silver.crm_cst_info';
	INSERT INTO silver.crm_cst_info (
		cst_id,
		cst_key,
		cst_firstname,
		cst_lastname,
		cst_marital_status,
		cst_gender,
		cst_create_date
	)
	SELECT
		cst_id,
		cst_key,
		TRIM(cst_firstname) AS cst_firstname,  -- Remove Unwanted Trailing Spaces
		TRIM(cst_lastname) AS cst_lastname,
		CASE
			WHEN UPPER(TRIM(cst_marital_status)) = 'M' THEN 'Married'
			WHEN UPPER(TRIM(cst_marital_status)) = 'S' THEN 'Single'
			ELSE 'n/a'
		END AS cst_marital_status,  -- Data Normalization & Standardization
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
    end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
	RAISE NOTICE '>> -------------';

    start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '>> Truncating Table: silver.crm_prd_info';
    TRUNCATE TABLE silver.crm_prd_info;
    RAISE NOTICE '>> Inserting Data Into: silver.crm_prd_info';
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
    end_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
    RAISE NOTICE '>> -------------';

    start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '>> Truncating Table: silver.crm_sales_details';
    TRUNCATE TABLE silver.crm_sales_details;
    RAISE NOTICE '>> Inserting Data Into: silver.crm_sales_details';
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
    end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
	RAISE NOTICE '>> -------------';
    
    RAISE NOTICE '------------------------------------------------';
	RAISE NOTICE 'Loading ERP Tables';
	RAISE NOTICE '------------------------------------------------';

    start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '>> Truncating Table: silver.erp_cust_az12';
    TRUNCATE TABLE silver.erp_cust_az12;
    RAISE NOTICE '>> Inserting Data Into: silver.erp_cust_az12';
    INSERT INTO silver.erp_cust_az12 (
        cid,
        bdate,
        gen
    )
    SELECT
        CASE
            WHEN cid LIKE 'NAS%' THEN SUBSTR(cid, 4, LENGTH(cid))
            ELSE cid
        END AS cid,  -- Remove 'NAS' prefix if exist
        CASE
            WHEN bdate > CURRENT_DATE THEN NULL
            ELSE bdate
        END AS bdate,  -- Set future birthdates to null
        CASE
            WHEN UPPER(TRIM(gen)) IN ('F', 'FEMALE') THEN 'Female'
            WHEN UPPER(TRIM(gen)) IN ('M', 'MALE') THEN 'Male'
            ELSE 'n/a'  -- Normalize gender values and handle unknown cases
        END AS gen
    FROM bronze.erp_cust_az12;
    end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
	RAISE NOTICE '>> -------------';

    start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '>> Truncating Table: silver.erp_loc_a101';
    TRUNCATE TABLE silver.erp_loc_a101;
    RAISE NOTICE '>> Inserting Data Into: silver.erp_loc_a101';
    INSERT INTO silver.erp_loc_a101 (
        cid,
        country
    )
    SELECT
        REPLACE(cid, '-', '') AS cid,
        CASE
            WHEN TRIM(country) = 'DE' THEN 'Germany'
            WHEN TRIM(country) IN ('US', 'USA') THEN 'United States'
            WHEN TRIM(country) = '' OR country IS NULL THEN 'n/a'
            ELSE TRIM(country)
        END AS country --Normalize and Handling missing or blank country codes
    FROM bronze.erp_loc_a101;
    end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
	RAISE NOTICE '>> -------------';

    start_time := CURRENT_TIMESTAMP;
    RAISE NOTICE '>> Truncating Table: silver.erp_px_cat_g1v2';
    TRUNCATE TABLE silver.erp_px_cat_g1v2;
    RAISE NOTICE '>> Inserting Data Into: silver.erp_px_cat_g1v2';
    INSERT INTO silver.erp_px_cat_g1v2 (
        id,
        cat,
        subcat,
        maintenance
    )
    SELECT
        id,
        cat,
        subcat,
        maintenance
    FROM bronze.erp_px_cat_g1v2;
    end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
	RAISE NOTICE '>> -------------';

    batch_end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '==========================================';
	RAISE NOTICE 'Loading Bronze Layer is Completed';
    RAISE NOTICE '   - Total Load Duration: % seconds',
		EXTRACT(EPOCH FROM (batch_end_time - batch_start_time));
	RAISE NOTICE '==========================================';
EXCEPTION
	WHEN OTHERS THEN
	RAISE NOTICE 'Error Occurred at: %', CURRENT_TIMESTAMP;
    RAISE NOTICE 'SQLSTATE: %', SQLSTATE;
    RAISE NOTICE 'Error Message: %', SQLERRM;
	RAISE;
END;
$$;