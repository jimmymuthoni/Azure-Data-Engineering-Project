import requests
from azure.storage.blob import BlobServiceClient, ContentSettings

connect_str = "rapace with your Azure connection string"
container_name = "replace with your Azure storage conainer name"

#CSV file list from GitHub
csv_files = [
   {
   "csv_relative_url": "Azure-Data-Engineering-Project/blob/main/Data/olist_customers_dataset.csv",
   "file_name": "olist_customers_dataset.csv"
   }, 
   {
   "csv_relative_url": "Azure-Data-Engineering-Project/blob/main/Data/olist_geolocation_dataset.csv",
   "file_name": "olist_geolocation_dataset.csv"
   }, 
   {
   "csv_relative_url": "Azure-Data-Engineering-Project/blob/main/Data/olist_order_items_dataset.csv",
   "file_name": "olist_order_items_dataset.csv"
   },  
   {
   "csv_relative_url": "Azure-Data-Engineering-Project/blob/main/Data//olist_order_reviews_dataset.csv",
   "file_name": "olist_order_reviews_dataset.csv"
   }, 
   {
   "csv_relative_url": "Azure-Data-Engineering-Project/blob/main/Data//olist_orders_dataset.csv",
   "file_name": "olist_orders_dataset.csv"
   },
   {
   "csv_relative_url": "Azure-Data-Engineering-Project/blob/main/Data//olist_products_dataset.csv",
   "file_name": "olist_products_dataset.csv"
   },
   {
   "csv_relative_url": "Azure-Data-Engineering-Project/blob/main/Data/olist_sellers_dataset.csv",
   "file_name": "olist_sellers_dataset.csv"
   }  
]

# Connecting to Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)

for file in csv_files:
    # Convert GitHub UI URL to raw content URL
    raw_url = file['csv_relative_url'].replace("blob/", "")
    github_raw_url = f"https://raw.githubusercontent.com/{raw_url}"

    try:
        response = requests.get(github_raw_url)
        response.raise_for_status()

        blob_path = f"bronze/{file['file_name']}" 
        blob_client = container_client.get_blob_client(blob_path)

        print(f"Uploading {blob_path}...")

        blob_client.upload_blob(
            response.content,
            overwrite=True,
            content_settings=ContentSettings(content_type='text/csv')
        )

        print(f"Uploaded: {blob_path}")

    except Exception as e:
        print(f"Failed to upload {file['file_name']}: {e}")
