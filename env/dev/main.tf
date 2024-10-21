module "dev_vm" {
  source = "../../modules/vm"
  ENVIRONMENT = var.ENVIRONMENT
  MAIL_SECRET_KEY = var.MAIL_SECRET_KEY
  MAIL_USER = var.MAIL_USER
  ADMIN_USERNAME = var.ADMIN_USERNAME
  DOMAIN = var.DOMAIN
  RESOURCE_GROUP = var.RESOURCE_GROUP
  NIC_NAME = var.NIC_NAME
  MAIL_SERVICE = var.MAIL_SERVICE
  SECURITY_GROUP_NAME = var.SECURITY_GROUP_NAME
  SSH_KEY_PATH = "./keys/monomap"
  PORT = var.PORT
  SERVER_NAME = var.SERVER_NAME
  MONGO_DB = var.MONGO_DB
  MONGO_URL = var.MONGO_URL
  LOCATION = var.LOCATION
  MAPBOX_ACCESS_TOKEN = var.MAPBOX_ACCESS_TOKEN
  MONGO_INITDB_ROOT_PASSWORD = var.MONGO_INITDB_ROOT_PASSWORD
  MONGO_INITDB_ROOT_USERNAME = var.MONGO_INITDB_ROOT_USERNAME
  IP_NAME = var.IP_NAME
  VNET_NAME = var.VNET_NAME
  MONGO_URL_DOCKER = var.MONGO_URL_DOCKER
  SUBNET_NAME = var.SUBNET_NAME
}

resource "azurerm_resource_group" "monomapceci15" {
  name = "monomapceci15"
  location = "eastus2"
}

resource "azurerm_resource_group" "mel" {
  name = "mel"
  location = "eastus2"
}

resource "azurerm_resource_group" "gonzalez" {
  name = "gonzalez"
  location = "eastus2"

}