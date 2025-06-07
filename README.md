# 🌐 End-to-End Azure Cloud Data Engineering Project

This project demonstrates a complete cloud-based data engineering pipeline built on **Azure Cloud**. It involves ingestion of raw data from multiple sources, transformation using **Azure Databricks**, enrichment from **MongoDB**, storage in **ADLS Gen2**, and loading into **Azure Synapse Analytics** for visualization via **Power BI**, **Tableau**, or **Microsoft Fabric**.

---

## 🔧 Tech Stack

- **Azure Data Factory** – for data ingestion
- **Azure Data Lake Storage Gen2 (ADLS Gen2)** – for raw and transformed data storage
- **Azure Databricks** – for data transformation and enrichment
- **MongoDB** – as external enrichment data source
- **Azure Synapse Analytics** – for data warehousing and querying
- **Power BI / Tableau / Fabric** – for data visualization

---

## 📈 Project Workflow

1. **Data Sources**  
   - HTTP endpoint (e.g., GitHub CSVs)  
   - SQL tables

2. **Data Ingestion**  
   - Azure Data Factory pipelines ingest raw data into ADLS Gen2.

3. **Data Transformation & Enrichment**  
   - Azure Databricks reads raw data from ADLS Gen2.
   - Enrichment is performed by joining with MongoDB tables.
   - Transformed data is written back to ADLS Gen2.

4. **Data Warehousing & Analytics**  
   - Azure Synapse reads transformed data.
   - Data is used for analytics and dashboards.

---

## 🧩 Architecture Diagram

![Architecture Diagram](./Architecture%20Diagram.png)

This image illustrates the complete flow of data from ingestion to visualization across Azure services.

---

## ⚙️ Azure Data Factory Pipeline Screenshot

> 📸 Add a screenshot of your ADF pipeline here:
![Azure Data Factory Pipeline](./ADF_Pipeline_Screenshot.png)

---

## 📂 Folder Structure

