# 🌐 End-to-End Azure Cloud Data Engineering Project

This project demonstrates a complete cloud-based data engineering pipeline built on **Azure Cloud**. It involves ingestion of raw data from multiple sources, transformation using **Azure Databricks**, enrichment from **MongoDB**, storage in **ADLS Gen2**, and loading into **Azure Synapse Analytics** for visualization via **Power BI**, **Tableau**, or **Microsoft Fabric**.

---

## Tech Stack

- **Azure Data Factory** – for data ingestion
- **Azure Data Lake Storage Gen2 (ADLS Gen2)** – for raw and transformed data storage
- **Azure Databricks** – for data transformation and enrichment
- **MongoDB** – as external enrichment data source
- **Azure Synapse Analytics** – for data warehousing and querying
- **Power BI** – for data visualization
- **Python** – for writing automation scripts to send data to ADLS Gen2
- **GitHub & MySQL** – data sources

---

## Medallion Architecture

This project follows the **Medallion Architecture** (Bronze, Silver, Gold) pattern to build a scalable and maintainable lakehouse structure using Azure services.

###  Bronze Layer – Raw
- Raw data is ingested using **Azure Data Factory** from:
  - Public GitHub repositories (CSV via HTTP)
  - MySQL SQL Tables
- Data is stored in **ADLS Gen2** without transformations.

###  Silver Layer – Cleaned & Enriched
- **Azure Databricks** reads raw data from the Bronze layer.
- Cleans and transforms the data using spark.
- Joins with **MongoDB** collections for enrichment.
- Outputs enriched data to the Silver layer in ADLS Gen2.

### Gold Layer – Aggregated
- Final transformed datasets are optimized for analytics and reporting.
- **Azure Synapse** reads Gold data for warehousing and querying.
- Output supports **Power BI**, **Tableau**, or **Fabric** dashboards.

---

## Project Workflow

1. **Data Sources**  
   - HTTP endpoint (e.g., GitHub CSVs)  
   - SQL tables (MySQL)

2. **Data Ingestion (Bronze Layer)**  
   - Azure Data Factory pipelines move raw data into ADLS Gen2.

3. **Data Transformation & Enrichment (Silver Layer)**  
   - Azure Databricks performs cleansing, filtering, and joins with MongoDB.
   - Data is saved back to ADLS Gen2 as enriched, cleaned data.

4. **Data Warehousing & Analytics (Gold Layer)**  
   - Azure Synapse loads transformed Gold layer data.
   - Data is visualized using Power BI or similar tools.

---

## Architecture Diagram

![Architecture Diagram](./Architecture%20Diagram.png)

This image illustrates the complete flow of data from ingestion to visualization using Medallion Architecture across Azure services.

---

## ⚙️ Azure Data Factory Pipeline

![Azure Data Factory Pipeline](https://github.com/jimmymuthoni/Azure-Data-Engineering-Project/blob/0cee85b5eaccfba118a700d93a502e9885aba656/Extract_pipeline.png)

---
