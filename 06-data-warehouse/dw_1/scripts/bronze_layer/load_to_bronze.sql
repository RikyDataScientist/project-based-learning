/*
===============================================================================
Procedure Scripts: Load Bronze Layer (Source -> Bronze)
===============================================================================
Script Purpose:
    This stored procedure loads data into the 'bronze' schema from external CSV files. 
    It performs the following actions:
    - Truncates the bronze tables before loading data.
    - Uses the `COPY` command to load data from csv Files to bronze tables.
*/

CREATE EXTENSION IF NOT EXISTS plpgsql;

DROP PROCEDURE IF EXISTS bronze.load_data;

CREATE OR REPLACE PROCEDURE bronze.load_data()
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
	RAISE NOTICE 'Loading Bronze Layer';
	RAISE NOTICE '================================================';

	RAISE NOTICE '------------------------------------------------';
	RAISE NOTICE 'Loading CRM Tables';
	RAISE NOTICE '------------------------------------------------';

	start_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Truncating Table: bronze.crm_cst_info';
	TRUNCATE TABLE bronze.crm_cst_info;
	RAISE NOTICE '>> Inserting Data Into: bronze.crm_cst_info';
	COPY bronze.crm_cst_info
	FROM '.\00-datasets\dataset_1\source_crm\cust_info.csv'
	WITH(
		FORMAT CSV,
		HEADER TRUE,
		DELIMITER ','
	);
	end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
	RAISE NOTICE '>> -------------';

	start_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Truncating Table: bronze.crm_prd_info';
	TRUNCATE TABLE bronze.crm_prd_info;
	RAISE NOTICE '>> Inserting Data Into: bronze.crm_prd_info';
	COPY bronze.crm_prd_info
	FROM '.\00-datasets\dataset_1\source_crm\prd_info.csv'
	WITH(
		FORMAT CSV,
		HEADER TRUE,
		DELIMITER ','
	);
	end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
	RAISE NOTICE '>> -------------';

	start_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Truncating Table: bronze.crm_sales_details';
	TRUNCATE TABLE bronze.crm_sales_details;
	RAISE NOTICE '>> Inserting Data Into: bronze.crm_sales_details';
	COPY bronze.crm_sales_details
	FROM '.\00-datasets\dataset_1\source_crm\sales_details.csv'
	WITH(
		FORMAT CSV,
		HEADER TRUE,
		DELIMITER ','
	);
	end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
	RAISE NOTICE '>> -------------';

	RAISE NOTICE '------------------------------------------------';
	RAISE NOTICE 'Loading ERP Tables';
	RAISE NOTICE '------------------------------------------------';

	start_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Truncating Table: bronze.erp_cust_az12';
	TRUNCATE TABLE bronze.erp_cust_az12;
	RAISE NOTICE '>> Inserting Data Into: bronze.erp_cust_az12';
	COPY bronze.erp_cust_az12
	FROM '.\00-datasets\dataset_1\source_erp\CUST_AZ12.csv'
	WITH(
		FORMAT CSV,
		HEADER TRUE,
		DELIMITER ','
	);
	end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
	RAISE NOTICE '>> -------------';

	start_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Truncating Table: bronze.erp_loc_a101';
	TRUNCATE TABLE bronze.erp_loc_a101;
	RAISE NOTICE '>> Inserting Data Into: bronze.erp_loc_a101';
	COPY bronze.erp_loc_a101
	FROM '.\00-datasets\dataset_1\source_erp\LOC_A101.csv'
	WITH(
		FORMAT CSV,
		HEADER TRUE,
		DELIMITER ','
	);
	end_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Load Duration: % seconds', EXTRACT(EPOCH FROM (end_time - start_time));
	RAISE NOTICE '>> -------------';

	start_time := CURRENT_TIMESTAMP;
	RAISE NOTICE '>> Truncating Table: bronze.erp_px_cat_g1v2';
	TRUNCATE TABLE bronze.erp_px_cat_g1v2;
	RAISE NOTICE '>> Inserting Data Into: bronze.erp_px_cat_g1v2';
	COPY bronze.erp_px_cat_g1v2
	FROM '.\00-datasets\dataset_1\source_erp\PX_CAT_G1V2.csv'
	WITH(
		FORMAT CSV,
		HEADER TRUE,
		DELIMITER ','
	);
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
	RAISE WARNING 'Error Message: %', SQLERRM;
END;
$$;