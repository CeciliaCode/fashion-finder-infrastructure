output "IN_IP_Output" {
  value = "${var.ENVIRONMENT}: ${azurerm_linux_virtual_machine.IN_VM.public_ip_address}"
}