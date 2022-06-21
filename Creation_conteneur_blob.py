# La creation de l’objet  BlobServiceClient 
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Pour garantir l’unicité du nom du conteneur 
container_name = str(uuid.uuid4())

# Création du conteneur
container_client = blob_service_client.create_container(container_name)
