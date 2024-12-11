![enter image description here](https://res.cloudinary.com/fortyfournorth/image/upload/v1710256288/The%20Look%20Company%20%28Staging%29/j2zi31lqofw1abqfrjux.jpg)

# **Fashion Finder Infrastructure**
## Geo-Referenced Systems

### **Team Members**
- **Becerra Díaz Alejandro**  
- **González Hernández Juan Pablo**  
- **Núñez Guerrero Melanie Guadalupe**  
- **Peña Bravo María Cecilia**  
- **Trujillo Ramírez César Andrés**  

#### **Professor**  
Frausto Ramírez Juan de Dios  

#### **Date:**  
11/12/2024  
##### **Program:**  
Software Engineering and Computational Systems - 712  

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Infrastructure Overview](#infrastructure-overview)
4. [Variables](#variables)
5. [Usage](#usage)
6. [Commands](#commands)
7. [Directory Structure](#directory-structure)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)

---

## **Introduction**

The Fashion Finder Infrastructure repository is a Terraform-based solution to deploy the backend infrastructure required for the Fashion Finder application. The deployment includes Azure Virtual Machines, Virtual Networks, Subnets, Network Security Groups, and more.

-[Fashion Finder application](https://github.com/AlexDB02/Shop-Catalog-MongoDB)

---

## **Prerequisites**

- [Terraform v1.3.7+](https://developer.hashicorp.com/terraform/downloads)
- Azure CLI (`az`) configured and authenticated.
- Azure subscription with appropriate permissions.
- SSH keys generated for VM access.
- Docker installed locally to validate configurations.

---

## **Infrastructure Overview**

This repository provisions the following resources in Azure:
1. **Virtual Network (VNet):** Connects all components securely.
2. **Subnet:** Segments network traffic for the virtual machine.
3. **Network Security Group (NSG):** Ensures controlled traffic flow.
4. **Virtual Machine:** Hosts the Dockerized backend application.
5. **Public IP Address:** Provides external access to the application.

---

## **Variables**

### Required Variables
| Variable                     | Description                                                |
|------------------------------|------------------------------------------------------------|
| `RESOURCE_GROUP`             | Name of the Azure Resource Group.                         |
| `LOCATION`                   | Azure region for deployment.                              |
| `ENVIRONMENT`                | Deployment environment (`dev`, `staging`, `prod`).        |
| `VNET_NAME`                  | Name of the Virtual Network.                              |
| `SUBNET_NAME`                | Name of the Subnet.                                       |
| `SECURITY_GROUP_NAME`        | Name of the Network Security Group.                       |
| `IP_NAME`                    | Name of the Public IP.                                    |
| `NIC_NAME`                   | Name of the Network Interface.                            |
| `SERVER_NAME`                | Name of the Virtual Machine.                              |
| `PORT`                       | Application listening port (e.g., `3000`).                |
| `MONGODB_URI`                | MongoDB connection string.                                |
| `MONGO_INITDB_ROOT_USERNAME` | MongoDB root username.                                    |
| `MONGO_INITDB_ROOT_PASSWORD` | MongoDB root password.                                    |
| `EMAIL_SERVICE`              | Email service provider (e.g., `gmail`).                   |
| `EMAIL_USER`                 | Email user account.                                       |
| `EMAIL_PASS`                 | Email access token.                                       |
| `ADMIN_USERNAME`             | Admin username for the VM.                                |
| `SSH_KEY_PATH`               | Path to the SSH private key.                              |

---

## **Usage**

### 1. Clone the Repository
```bash
git clone https://github.com/CeciliaCode/fashion-finder-infrastructure.git
cd fashion-finder-infrastructure
```

### 2. Set Up Environment Variables
Create a `terraform.tfvars` file in the root directory.

### 3. Initialize Terraform
Run the following command to initialize the working directory:
```bash
terraform init
```

### 4. Validate Configuration
Ensure the configuration is correct:
```bash
terraform validate
```

### 5. Plan Deployment
View the resources to be created:
```bash
terraform plan
```

### 6. Apply Changes
Deploy the infrastructure:
```bash
terraform apply
```

### 7. Destroy Infrastructure
Remove all resources:
```bash
terraform destroy
```

---

## **Commands**

| Command                   | Description                                                  |
|---------------------------|--------------------------------------------------------------|
| `terraform init`          | Initialize the working directory.                           |
| `terraform validate`      | Validate configuration files.                               |
| `terraform plan`          | Show the execution plan.                                    |
| `terraform apply`         | Apply the configuration and create resources.               |
| `terraform destroy`       | Destroy all resources created by Terraform.                 |

---

## **Directory Structure**

```plaintext
.
├── env/
│   └── dev/
│       ├── main.tf         # Terraform configuration file
│       ├── variables.tf    # Definitions of all variables
│       └── outputs.tf      # Outputs for resources
├── modules/
│   └── vm/
│       ├── main.tf         # VM module configuration
│       ├── variables.tf    # Module variables
│       └── outputs.tf      # Module outputs
├── terraform.tfvars        # Environment-specific variable values
└── README.md               # Project documentation
```

---

## **Troubleshooting**

### Common Errors
1. **Authentication Error:**
   - Ensure you are logged in to Azure using `az login`.
   - Verify the `ARM_CLIENT_ID`, `ARM_CLIENT_SECRET`, `ARM_TENANT_ID`, and `ARM_SUBSCRIPTION_ID` are correctly configured in your environment.

2. **SSH Key Not Found:**
   - Verify the path to your SSH keys in the `SSH_KEY_PATH` variable.

3. **Plan/Apply Fails:**
   - Ensure all required variables are defined in `terraform.tfvars`.

---
