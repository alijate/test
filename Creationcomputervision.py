COGNITIVE_RESOURCE_GROUP="CnamorangeTP"
REGION="France Central"
COGNITIVE_ACCOUNT_NAME="vision-ordi-test"

echo "Create Resource Group: $COGNITIVE_RESOURCE_GROUP"
az group create --name $COGNITIVE_RESOURCE_GROUP --location $REGION

echo "Create Cognitive Resource for Computer Vision: $COGNITIVE_ACCOUNT_NAME"
az cognitiveservices account create \
  -n $COGNITIVE_ACCOUNT_NAME \
  -g $COGNITIVE_RESOURCE_GROUP \
  --kind ComputerVision \
  --sku S1 \
  -l $REGION \
  --yes