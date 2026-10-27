# Databricks notebook source
import os
from databricks.sdk import WorkspaceClient

workspace_url = os.environ.get("WORKSPACE_URL")
sp_client_id = os.environ.get("SP_CLIENT_ID")
sp_client_secret = os.environ.get("SP_CLIENT_SECRET")

if all([workspace_url, sp_client_id, sp_client_secret]):
    w = WorkspaceClient(host=workspace_url, client_id=sp_client_id, client_secret=sp_client_secret)
else:
    w = WorkspaceClient()

results = w.vector_search_indexes.query_index(
    index_name="agentic_catalog.agentic_schema.product_docs_index",
    columns=["indexed_doc", "product_id"],
    query_text="where can i find tutorial for AccountEase Pro  product",
    query_type="HYBRID",
    num_results=3
)

for doc in results.result.data_array:
    print(doc)