terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.0.0"
    }
  }

  /*backend "azurerm" {
    resource_group_name = "tfstateRGCeci"
    storage_account_name = "tfstatececi"
    container_name = "ceciliatfstate"
    key = "terraform.tfstate"
  }*/
}

provider "azurerm" {
  features {}
}