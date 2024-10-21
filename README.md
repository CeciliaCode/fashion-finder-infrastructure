# Infrastructure Deployment with Terraform, Docker, and GitHub Actions

![Infrastructure](https://github.com/user-attachments/assets/4867082d-a38d-4f1a-bcb6-18eef948f178)

## Description

This project deploys infrastructure in the cloud using Terraform, called MonoApp, which registers Monkeypox cases. It includes a virtual machine with the following containers: Nginx as a reverse proxy, Let’s Encrypt for SSL certificate management, the MonoMap API (available on Docker Hub), and MongoDB as the database. Additionally, the infrastructure deployment and destruction are automated using GitHub Actions, and the Terraform state is stored remotely in Azure Storage.

## Prerequisites

Before starting, ensure you have the following tools installed:

- Terraform
- Docker and Docker Compose
- GitHub (for managing code and setting up GitHub Actions)
- Azure account (for deploying infrastructure)

Also, you must configure access credentials for Azure and GitHub.

### Setting up Azure Credentials for Terraform

To deploy resources in Azure using Terraform, you must configure your access credentials. Here’s a step-by-step guide:

1. **Install Azure CLI**

2. **Log into Azure**

Open the terminal and use the following command to log in to Azure:

```bash
az login
```

This will open a browser window for authentication. Once logged in, you'll see your subscription details in the terminal.

3. **Configure Azure Subscription**

If you have multiple subscriptions, select the one you're going to use:

```bash
az account set --subscription "YOUR_SUBSCRIPTION_ID"
```

You can check available subscriptions with:

```bash
az account list --output table
```

4. **Create a Service Principal for Terraform**

Terraform needs permissions in your subscription to manage resources. Create a Service Principal with the following command:

```bash
az ad sp create-for-rbac --name "terraform-sp" --role Contributor --scopes /subscriptions/{subscription-id}
```

This will generate the necessary credentials (appId, password, tenant). Save this information, as you'll need it in the next steps.

5. **Set Environment Variables**

In the terminal, export the Service Principal credentials:

```bash
export ARM_CLIENT_ID="appId"
export ARM_CLIENT_SECRET="password"
export ARM_SUBSCRIPTION_ID="{subscription-id}"
export ARM_TENANT_ID="tenant"
```

### Setting up GitHub Credentials in GitHub Actions

For GitHub Actions to access the necessary credentials and secrets, you need to configure them in your repository. Here's a step-by-step guide to adding the necessary secrets:

1. **Open Repository Settings in GitHub**

Go to the repository where you're using GitHub Actions.

Click on **Settings**.

2. **Add Secrets in GitHub**

Under **Security**, select **Secrets and variables** > **Actions**.

Click on **New repository secret**.

3. **Add the Necessary Secrets**

Add the following secrets:

- **AZURE_CLIENT_ID**: appId of the Service Principal.
- **AZURE_CLIENT_SECRET**: password of the Service Principal.
- **AZURE_TENANT_ID**: tenant ID.
- **AZURE_SUBSCRIPTION_ID**: subscription ID.

Other related secrets, such as:

- **DOCKER_HUB_USERNAME** and **DOCKER_HUB_PASSWORD** (if needed for Docker Hub authentication).
- **SSH_PRIVATE_KEY**: if you need to access the virtual machine with an SSH key.

4. **Use Secrets in GitHub Actions Workflow**

In your `.github/workflows/deploy.yml` file, use the added secrets for authentication.

---

## Key Resources Defined in `main.tf`

- **Virtual Machine**: Deployed in Azure with Docker automatically installed via a cloud-init script.
- **Network and Security Rules**: To ensure access to the virtual machine.
- **Azure Storage**: An Azure Storage container is used to store the Terraform state remotely.

### Automatic Docker Installation

The virtual machine is configured to have Docker installed at the time of creation using a cloud-init script. This ensures Docker is ready to run containers as soon as the virtual machine is operational.

### Storing the State in Azure Storage

The Terraform state is stored in an Azure Storage container configured in the `backend` block of Terraform. Make sure to have created the container before deploying the infrastructure.

Example configuration in `main.tf`:

```hcl
terraform {
  backend "azurerm" {
    storage_account_name = "account_name"
    container_name       = "container_name"
    key                  = "terraform.tfstate"
  }
}
```

---

### Docker Compose File

The `docker-compose.yml` file includes the following services:

- **Nginx Reverse Proxy**: Manages traffic and directs it to the appropriate services.
- **Let’s Encrypt**: Automates the acquisition of SSL certificates to secure traffic.
- **MonoMap API**: Uses the official image from Docker Hub and manages the project's main API.
- **MongoDB**: Database used to store API information.

Once the virtual machine is ready, Docker Compose is automatically executed using Terraform provisioners to start these containers.

---

## GitHub Actions

This repository includes a configuration file for GitHub Actions in `.github/workflows/deploy.yml` that allows:

- **Automatic deployment** when pushing to the `main` branch.
- **Manual infrastructure destruction** via `workflow_dispatch`.
- **Deployment**:

When pushing to the `main` branch, GitHub Actions runs the following commands:

- `terraform init` to initialize the environment.
- `terraform plan` to plan the deployment.
- `terraform apply` to apply the changes and deploy the infrastructure.

---

To securely interact with the infrastructure via GitHub Actions, configure the secrets in your GitHub repository.

### Secrets to Add:

- **ENVIRONMENT**: Indicates the environment (e.g., production or development).
- **MAIL_SECRET_KEY**: Secret key for authentication with the mail service.
- **MAIL_USER**: Mail service user sending notifications or alerts.
- **ADMIN_USERNAME**: Admin username for the virtual machine.
- **DOMAIN**: Domain used to access services.
- **RESOURCE_GROUP**: Name of the resource group in Azure where the infrastructure is deployed.
- **NIC_NAME**: Name of the network interface used by the virtual machine.
- **MAIL_SERVICE**: Mail service used (e.g., Gmail, Outlook).
- **SECURITY_GROUP_NAME**: Name of the security group configured in the infrastructure.
- **SSH_KEY_PATH**: Path to the SSH key for accessing the virtual machine (e.g., `./keys/monomap`).
- **PORT**: Port where the application or web server runs.
- **SERVER_NAME**: Server name configured for the API.
- **MONGO_DB**: MongoDB database name.
- **MONGO_URL**: MongoDB connection URL.
- **LOCATION**: Geographic location for the Azure infrastructure deployment.
- **MAPBOX_ACCESS_TOKEN**: Access token to use Mapbox services (if needed for MonoMap API).
- **MONGO_INITDB_ROOT_PASSWORD**: Root password for the MongoDB instance.
- **MONGO_INITDB_ROOT_USERNAME**: Root username for MongoDB.
- **IP_NAME**: Name of the public IP assigned to the virtual machine.
- **VNET_NAME**: Name of the virtual network used in Azure.
- **MONGO_URL_DOCKER**: MongoDB connection URL from the Docker container.
- **SUBNET_NAME**: Name of the subnet in the virtual network.

---

### Infrastructure Destruction

To destroy the infrastructure, manually activate the `workflow_dispatch` in GitHub Actions. This will run `terraform destroy` and remove all resources created.

---

## Deployment and Testing

### Deploy the Infrastructure:

1. Set your Azure credentials in your environment.
2. Push to the `main` branch. This will trigger the workflow and deploy the infrastructure.
3. Verify deployment status: You can use the Azure portal to check the created resources and ensure that the virtual machine and containers are running.

### Access the VM

To access the created virtual machine, use SSH with the provided public IP:

```bash
ssh -i ./keys/monomap adminuser@20.14.162.192
```

---

## API Testing

You can test the API using Postman or any HTTP client. Use the public IP or assigned domain to make requests.

---

## Destroy the Infrastructure

To destroy the infrastructure, use the manual `workflow_dispatch` in GitHub Actions. This will remove all resources created by Terraform.

---

## Recommendations

For long-term infrastructure maintenance:

- Monitor the automatic renewal of SSL certificates with Let’s Encrypt.
- Regularly back up the MongoDB database.

---
