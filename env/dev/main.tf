module "dev_vm" {
  source                     = "../../modules/vm"
  RESOURCE_GROUP             = var.RESOURCE_GROUP
  LOCATION                   = var.LOCATION
  ENVIRONMENT                = var.ENVIRONMENT
  VNET_NAME                  = var.VNET_NAME
  SUBNET_NAME                = var.SUBNET_NAME
  SECURITY_GROUP_NAME        = var.SECURITY_GROUP_NAME
  IP_NAME                    = var.IP_NAME
  NIC_NAME                   = var.NIC_NAME
  SERVER_NAME                = var.SERVER_NAME
  PORT                       = var.PORT
  MONGO_URI                  = var.MONGO_URI
  MONGO_INITDB_ROOT_USERNAME = var.MONGO_INITDB_ROOT_USERNAME
  MONGO_INITDB_ROOT_PASSWORD = var.MONGO_INITDB_ROOT_PASSWORD
  EMAIL_SERVICE              = var.EMAIL_SERVICE
  EMAIL_USER                 = var.EMAIL_USER
  EMAIL_PASS                 = var.EMAIL_PASS
  ADMIN_USERNAME             = var.ADMIN_USERNAME
  SSH_KEY_PATH               = var.SSH_KEY_PATH
}

# Unlocked test 2.