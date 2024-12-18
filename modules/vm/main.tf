resource "azurerm_resource_group" "IN_RG" {
  name     = "${var.RESOURCE_GROUP}_${var.ENVIRONMENT}"
  location = var.LOCATION
  tags = {
    environment = var.ENVIRONMENT
  }
}

resource "azurerm_virtual_network" "IN_VNET" {
  name                = "${var.VNET_NAME}_${var.ENVIRONMENT}"
  resource_group_name = azurerm_resource_group.IN_RG.name
  location            = var.LOCATION
  address_space       = ["10.123.0.0/16"]
  tags = {
    environment = var.ENVIRONMENT
  }
}

resource "azurerm_subnet" "IN_SUBNET" {
  name                 = "${var.SUBNET_NAME}_${var.ENVIRONMENT}"
  resource_group_name  = azurerm_resource_group.IN_RG.name
  virtual_network_name = azurerm_virtual_network.IN_VNET.name
  address_prefixes     = ["10.123.1.0/24"]
}

resource "azurerm_network_security_group" "IN_SG" {
  name                = var.SECURITY_GROUP_NAME
  location            = var.LOCATION
  resource_group_name = azurerm_resource_group.IN_RG.name
  tags = {
    "environment" = var.ENVIRONMENT
  }

  security_rule {
    name                       = "allow-all"
    priority                   = 101
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }
}

resource "azurerm_subnet_network_security_group_association" "IN_SGA" {
  subnet_id                 = azurerm_subnet.IN_SUBNET.id
  network_security_group_id = azurerm_network_security_group.IN_SG.id
}

resource "azurerm_public_ip" "IN_IP" {
  name                = "${var.IP_NAME}_${var.ENVIRONMENT}"
  resource_group_name = azurerm_resource_group.IN_RG.name
  location            = var.LOCATION
  allocation_method   = "Dynamic"
}

resource "azurerm_network_interface" "IN_NIC" {
  name                = var.NIC_NAME
  location            = var.LOCATION
  resource_group_name = azurerm_resource_group.IN_RG.name

  ip_configuration {
    name                          = "${var.IP_NAME}-Config-${var.ENVIRONMENT}"
    subnet_id                     = azurerm_subnet.IN_SUBNET.id
    public_ip_address_id          = azurerm_public_ip.IN_IP.id
    private_ip_address_allocation = "Dynamic"
  }

  tags = {
    environment = var.ENVIRONMENT
  }
}

# Crear máquina virtual.
resource "azurerm_linux_virtual_machine" "IN_VM" {
  name                  = "${var.SERVER_NAME}-${var.ENVIRONMENT}"
  resource_group_name   = azurerm_resource_group.IN_RG.name
  location              = azurerm_resource_group.IN_RG.location
  size                  = "Standard_B2s"
  admin_username        = var.ADMIN_USERNAME
  network_interface_ids = [azurerm_network_interface.IN_NIC.id]
  custom_data           = filebase64("${path.module}/scripts/docker-install.tpl")

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-LTS"
    version   = "latest"
  }

  admin_ssh_key {
    username   = var.ADMIN_USERNAME
    public_key = file("${var.SSH_KEY_PATH}.pub")
  }

  provisioner "file" {
    source = "./containers/docker-compose.yml"
    destination = "/home/${var.ADMIN_USERNAME}/docker-compose.yml"

    connection {
        type = "ssh"
        user = var.ADMIN_USERNAME
        private_key = file(var.SSH_KEY_PATH)
        host = self.public_ip_address
    }
  }

  provisioner "remote-exec" {
    inline = [ 
      "sudo su -c 'mkdir -p /volumes/nginx/html'",
      "sudo su -c 'mkdir -p /volumes/nginx/certs'",
      "sudo su -c 'mkdir -p /volumes/nginx/vhostd'",
      "sudo su -c 'mkdir -p /volumes/mongo/data'",
      "sudo su -c 'chmod 775 /volumes/nginx/html'",
      "sudo su -c 'chmod 775 /volumes/nginx/certs'",
      "sudo su -c 'chmod 775 /volumes/nginx/vhostd'",
      "sudo su -c 'chmod 770 /volumes/mongo/data'",
      "sudo su -c 'touch /home/${var.ADMIN_USERNAME}/.env'", 
      "sudo su -c 'echo \"MONGO_URI=${var.MONGO_URI}\" >> /home/${var.ADMIN_USERNAME}/.env'",
      "sudo su -c 'echo \"PORT=${var.PORT}\" >> /home/${var.ADMIN_USERNAME}/.env'",
      "sudo su -c 'echo \"EMAIL_SERVICE=${var.EMAIL_SERVICE}\" >> /home/${var.ADMIN_USERNAME}/.env'",
      "sudo su -c 'echo \"EMAIL_USER=${var.EMAIL_USER}\" >> /home/${var.ADMIN_USERNAME}/.env'",
      "sudo su -c 'echo \"EMAIL_PASS=${var.EMAIL_PASS}\" >> /home/${var.ADMIN_USERNAME}/.env'",
      "sudo su -c 'echo \"MONGO_INITDB_ROOT_USERNAME=${var.MONGO_INITDB_ROOT_USERNAME}\" >> /home/${var.ADMIN_USERNAME}/.env'",
      "sudo su -c 'echo \"MONGO_INITDB_ROOT_PASSWORD=${var.MONGO_INITDB_ROOT_PASSWORD}\" >> /home/${var.ADMIN_USERNAME}/.env'"
    ]

    connection {
      type        = "ssh"
      user        = var.ADMIN_USERNAME
      private_key = file(var.SSH_KEY_PATH)
      host        = self.public_ip_address
    }
  }
}

resource "time_sleep" "wait_3_minutes" {
  depends_on = [ azurerm_linux_virtual_machine.IN_VM ]
  create_duration = "180s"
}

resource "null_resource" "init_docker" {
  depends_on = [ time_sleep.wait_3_minutes ]

  connection {
    type = "ssh"
    user = var.ADMIN_USERNAME
    private_key = file(var.SSH_KEY_PATH)
    host = azurerm_linux_virtual_machine.IN_VM.public_ip_address
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update -y",
      "sudo apt-get install -y docker.io",
      "sudo systemctl enable docker",
      "sudo systemctl start docker",
      "sudo curl -L \"https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose",
      "sudo chmod +x /usr/local/bin/docker-compose",
      "cd /home/${var.ADMIN_USERNAME}",
      "sudo docker-compose up -d"
    ]
  }
}

output "resource_group_name" {
  value = azurerm_resource_group.IN_RG.name
}

output "virtual_network_name" {
  value = azurerm_virtual_network.IN_VNET.name
}

output "vm_name" {
  value = azurerm_linux_virtual_machine.IN_VM.name
}
