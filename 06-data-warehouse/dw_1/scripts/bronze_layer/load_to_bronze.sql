/*
===============================================================================
Load Scripts: Load Bronze Layer (Source -> Bronze)
===============================================================================
Script Purpose:
    This stored procedure loads data into the 'bronze' schema from external CSV files. 
    It performs the following actions:
    - Truncates the bronze tables before loading data.
    - Uses the `COPY` command to load data from csv Files to bronze tables.
*/

TRUNCATE TABLE bronze.crm_cst_info;

COPY bronze.crm_cst_info
FROM '.\00-datasets\dataset_1\source_crm\cust_info.csv'
WITH(
	FORMAT CSV,
	HEADER TRUE,
	DELIMITER ','
);

TRUNCATE TABLE bronze.crm_prd_info;

COPY bronze.crm_prd_info
FROM '.\00-datasets\dataset_1\source_crm\prd_info.csv'
WITH(
	FORMAT CSV,
	HEADER TRUE,
	DELIMITER ','
);

TRUNCATE TABLE bronze.crm_sales_details;

COPY bronze.crm_sales_details
FROM '.\00-datasets\dataset_1\source_crm\sales_details.csv'
WITH(
	FORMAT CSV,
	HEADER TRUE,
	DELIMITER ','
);

TRUNCATE TABLE bronze.erp_cust_az12;

COPY bronze.erp_cust_az12
FROM '.\00-datasets\dataset_1\source_erp\CUST_AZ12.csv'
WITH(
	FORMAT CSV,
	HEADER TRUE,
	DELIMITER ','
);

TRUNCATE TABLE bronze.erp_loc_a101;

COPY bronze.erp_loc_a101
FROM '.\00-datasets\dataset_1\source_erp\LOC_A101.csv'
WITH(
	FORMAT CSV,
	HEADER TRUE,
	DELIMITER ','
);

TRUNCATE TABLE bronze.erp_px_cat_g1v2;

COPY bronze.erp_px_cat_g1v2
FROM '.\00-datasets\dataset_1\source_erp\PX_CAT_G1V2.csv'
WITH(
	FORMAT CSV,
	HEADER TRUE,
	DELIMITER ','
);