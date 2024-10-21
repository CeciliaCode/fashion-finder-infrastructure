# infrastructure-monomap
![Infrastructure](https://github.com/user-attachments/assets/4867082d-a38d-4f1a-bcb6-18eef948f178)
This project involves the deployment of an infrastructure using Terraform. The objective is to create a virtual machine in the cloud with Docker automatically installed during the initial setup. Furthermore, a docker-compose.yml file will be executed to launch the specified containers.

Despliegue de Infraestructura con Terraform, Docker y GitHub Actions 

Descripción 

Este proyecto despliega una infraestructura en la nube utilizando Terraform, llamda MonoApp, la cual permite registrar los Casos de la enfermedad "Viruela del Mono". Incluye una máquina virtual con los siguientes contenedores: Nginx como reverse proxy, Let’s Encrypt para la gestión de certificados SSL, la API MonoMap disponible en Docker Hub y MongoDB como base de datos. Además, el despliegue y destrucción de la infraestructura están automatizados mediante GitHub Actions, y el estado de Terraform se almacena remotamente en Azure Storage. 


Requisitos previos 

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas: 

- Terraform 

- Docker y Docker Compose 

- GitHub (para gestionar el código y configurar GitHub Actions) 

- Cuenta de Azure (para desplegar la infraestructura) 

Además, debes configurar las credenciales de acceso para Azure y GitHub. 

Configurar Credenciales de Azure para Terraform:
Para poder desplegar recursos en Azure utilizando Terraform, debes configurar tus credenciales de acceso. Aquí tienes un tutorial paso a paso: 

1. Instalar Azure CLI 

2. Iniciar Sesión en Azure 

Abre la terminal y usa el siguiente comando para iniciar sesión en Azure: 

az login 

Esto abrirá una ventana del navegador para autenticarte. Una vez que inicies sesión, verás en la terminal los detalles de tus suscripciones. 

3. Configurar la Suscripción de Azure 

Si tienes varias suscripciones, selecciona la que vas a usar: 

az account set --subscription "ID_DE_LA_SUSCRIPCIÓN" 

Puedes verificar las suscripciones disponibles con: 

az account list --output table 

4. Crear un Service Principal para Terraform 

Terraform necesita permisos en tu suscripción para gestionar los recursos. Crea un Service Principal con el siguiente comando: 

az ad sp create-for-rbac --name "terraform-sp" --role Contributor --scopes /subscriptions/{subscription-id} 

Esto generará las credenciales necesarias (appId, password, tenant). Guarda esta información, ya que la necesitarás en los siguientes pasos. 

5. Configurar Variables de Entorno 

En la terminal, exporta las credenciales del Service Principal: 

export ARM_CLIENT_ID="appId"  

export ARM_CLIENT_SECRET="password"  

export ARM_SUBSCRIPTION_ID="{subscription-id}"  

export ARM_TENANT_ID="tenant" 


Configurar Credenciales de GitHub en GitHub Actions:
Para que GitHub Actions pueda acceder a las credenciales y secretos necesarios, debes configurarlos en tu repositorio. Aquí tienes un tutorial paso a paso para añadir los secretos necesarios: 

1. Abrir Configuración del Repositorio en GitHub 

Ve al repositorio donde estás utilizando GitHub Actions. 

Haz clic en Settings (Configuración). 

2. Agregar Secrets en GitHub 

En la sección Security, selecciona Secrets and variables > Actions. 

Haz clic en New repository secret. 

3. Agregar los Secrets Necesarios 

Añade los siguientes secretos: 

AZURE_CLIENT_ID: appId del Service Principal. 

AZURE_CLIENT_SECRET: password del Service Principal. 

AZURE_TENANT_ID: tenant ID. 

AZURE_SUBSCRIPTION_ID: ID de la suscripción. 

Otros secretos relacionados, como: 

DOCKER_HUB_USERNAME y DOCKER_HUB_PASSWORD (si es necesario para autenticación en Docker Hub). 

SSH_PRIVATE_KEY: si necesitas acceder a la máquina virtual con una clave SSH. 

4. Uso de Secrets en el Workflow de GitHub Actions 

En tu archivo .github/workflows/deploy.yml, utiliza los secretos agregados para autenticación. 

El archivo main.tf define los siguientes recursos clave: 

Máquina virtual: Se despliega en Azure y tiene Docker instalado automáticamente mediante un script cloud-init. 

Red y reglas de seguridad: Para asegurar el acceso a la máquina virtual. 

Almacenamiento en Azure: Un contenedor de Azure Storage se utiliza para almacenar el estado de Terraform de manera remota. 


Instalación automática de Docker 

La máquina virtual se configura para tener Docker instalado al momento de la creación, utilizando un script cloud-init. Esto garantiza que Docker esté listo para ejecutar los contenedores una vez que la máquina virtual esté en funcionamiento. 

Almacenamiento del estado en Azure Storage 

El estado de Terraform se almacena en un contenedor de Azure Storage configurado en el bloque backend de Terraform. Asegúrate de haber creado el contenedor antes de desplegar la infraestructura. 

Ejemplo de configuración en main.tf: 

terraform { 
  backend "azurerm" { 
    storage_account_name = "nombre_de_cuenta" 
    container_name       = "nombre_de_contenedor" 
    key                  = "terraform.tfstate" 
  } 
} 
 

Archivo Docker Compose 

El archivo docker-compose.yml incluye los siguientes servicios: 

Nginx Reverse Proxy: Gestiona el tráfico y lo redirige a los servicios correspondientes. 

Let’s Encrypt: Automatiza la obtención de certificados SSL para asegurar el tráfico. 

MonoMap API: Usa la imagen oficial desde Docker Hub y gestiona la API principal del proyecto. 

MongoDB: Base de datos utilizada para almacenar la información de la API. 

Una vez que la máquina virtual esté lista, Docker Compose se ejecuta automáticamente utilizando provisioners en Terraform para levantar estos contenedores. 

 
GitHub Actions 

Este repositorio incluye un archivo de configuración para GitHub Actions en .github/workflows/deploy.yml que permite: 

- Despliegue automático al hacer push a la rama main. 

- Destrucción manual de la infraestructura mediante workflow_dispatch. 

- Despliegue 

- Al hacer push a la rama main, GitHub Actions ejecuta los siguientes comandos: 

terraform init para inicializar el entorno. 

terraform plan para planificar el despliegue. 

terraform apply para aplicar los cambios y desplegar la infraestructura. 

 

Para que GitHub Actions pueda interactuar de manera segura con la infraestructura  es necesario configurar los secrets en el repositorio de GitHub.  

En este proyecto, debes agregar los siguientes secrets correspondientes: 

- ENVIRONMENT: Indica el entorno en el que se va a desplegar la infraestructura (por ejemplo, production o development). 

- MAIL_SECRET_KEY: Clave secreta utilizada para la autenticación en el servicio de correo. 

- MAIL_USER: Usuario del servicio de correo que envía notificaciones o alertas. 

- ADMIN_USERNAME: Nombre de usuario administrador de la máquina virtual. 

- DOMAIN: Dominio que será utilizado para acceder a los servicios. 

- RESOURCE_GROUP: Nombre del grupo de recursos en Azure donde se despliega la infraestructura. 

- NIC_NAME: Nombre de la interfaz de red utilizada en la máquina virtual. 

- MAIL_SERVICE: Servicio de correo utilizado (por ejemplo, Gmail, Outlook). 

- SECURITY_GROUP_NAME: Nombre del grupo de seguridad configurado en la infraestructura. 

- SSH_KEY_PATH: Ruta de la clave SSH para acceder a la máquina virtual (por ejemplo, "./keys/monomap"). 

- PORT: Puerto en el que se ejecuta la aplicación o el servidor web. 

- SERVER_NAME: Nombre del servidor configurado para la API. 

- MONGO_DB: Nombre de la base de datos MongoDB. 

- MONGO_URL: URL de conexión a la base de datos MongoDB. 

- LOCATION: Ubicación geográfica donde se desplegará la infraestructura en Azure. 

- MAPBOX_ACCESS_TOKEN: Token de acceso para utilizar los servicios de Mapbox (si es necesario para MonoMap API). 

- MONGO_INITDB_ROOT_PASSWORD: Contraseña de root para la instancia de MongoDB. 

- MONGO_INITDB_ROOT_USERNAME: Nombre de usuario root para MongoDB. 

- IP_NAME: Nombre de la dirección IP pública asignada a la máquina virtual. 

- VNET_NAME: Nombre de la red virtual utilizada en la infraestructura de Azure. 

- MONGO_URL_DOCKER: URL de conexión a MongoDB desde el contenedor Docker. 

- SUBNET_NAME: Nombre de la subred en la red virtual. 

 

Cómo agregar secrets en GitHub: 

Ve al repositorio de GitHub. 

Haz clic en la pestaña Settings (Configuración). 

En el menú de la izquierda, selecciona Secrets and variables y luego selecciona Actions. 

Haz clic en el botón New repository secret. 

Introduce el nombre del secret (por ejemplo, ENVIRONMENT) y su valor correspondiente. 

Repite este proceso para cada una de las variables listadas. 

Estos secrets se usarán automáticamente en los workflows de GitHub Actions para el despliegue y configuración de la infraestructura. 

 

Destrucción 

Para destruir la infraestructura, debes activar manualmente el workflow desde GitHub usando la opción workflow_dispatch, que ejecutará terraform destroy y eliminará todos los recursos creados. 


Despliegue y pruebas 

Despliegue de la infraestructura:

- Configura tus credenciales de Azure en tu entorno. 

- Realiza un push a la rama main. Esto activará el workflow y desplegará la infraestructura. 

- Verifica el estado del despliegue: Puedes usar el portal de Azure para revisar los recursos creados y asegurarte de que la máquina virtual y los contenedores están funcionando. 

 

Acceso a la VM 

Para acceder a la máquina virtual creada, utiliza SSH con la IP pública proporcionada: 

ssh -i ./keys/monomap adminuser@20.14.162.192 
 

Prueba de la API 

La API se puede probar utilizando Postman o cualquier cliente HTTP. Usa la IP pública o el dominio asignado para hacer solicitudes: 

Cómo crear un dominio personalizado en No-IP 

No-IP es un servicio que permite registrar dominios y configurar DNS dinámicos (Dynamic DNS o DDNS) para dispositivos con direcciones IP dinámicas, como routers y servidores domésticos. A continuación te explico los pasos para crear un dominio personalizado en No-IP. 

1. Crear una cuenta en No-IP 

Visita el sitio web de No-IP: https://www.noip.com/es-MX. 

Haz clic en el botón Registrarse en la esquina superior derecha. 

Completa el formulario de registro con tu nombre, dirección de correo electrónico y una contraseña. 

Después del registro, recibirás un correo de confirmación. Haz clic en el enlace de activación que se envía a tu correo para activar la cuenta. 

2. Configurar un dominio gratuito o personalizado 

No-IP ofrece dos tipos de dominios: 

Dominios gratuitos: Puedes elegir un subdominio gratuito en varios dominios que No-IP proporciona (por ejemplo, mi-dominio.ddns.net). 

Dominios personalizados (Premium): Puedes registrar un dominio propio (por ejemplo, mi-dominio.com) o usar uno que ya tengas y administrarlo a través de No-IP. 


Para crear un dominio gratuito: 

- Inicia sesión en tu cuenta de No-IP. 

- Ve al panel de control y selecciona Dynamic DNS en el menú superior. 

- Haz clic en Agregar Host. 

- En el campo Hostname, introduce el nombre que deseas para tu subdominio (por ejemplo, mi-servidor). 

- Selecciona el dominio que deseas usar del menú desplegable (por ejemplo, ddns.net). 

- En la sección Tipo de registro (Record Type), selecciona A (IPv4) y asegúrate de que tu dirección IP pública esté detectada automáticamente (aparecerá en el campo correspondiente). 

- Haz clic en Guardar Host. 

- Para un dominio personalizado (Premium): 

- Ve a la pestaña Comprar un Dominio o Registrar un Dominio. 

- Ingresa el nombre de dominio que deseas comprar y selecciona entre las extensiones disponibles (.com, .net, .org, etc.). 

Completa el proceso de pago para adquirir el dominio o tienes la posibilidad de crear 1 gratuita. 

Una vez que tengas el dominio, puedes gestionarlo desde la pestaña Administrar Dominios. 

Guarda los cambios. 

3. Comprobar la configuración 

Después de configurar tu dominio, prueba accediendo a tu dirección de dominio desde un navegador para verificar que esté funcionando correctamente. 


Destrucción de la infraestructura 

Para destruir la infraestructura, utiliza el workflow manual workflow_dispatch en GitHub Actions. Esto eliminará todos los recursos creados por Terraform. 

 
Recomendaciones 

Para mantener la infraestructura a largo plazo: 

- Monitorea la renovación automática de los certificados SSL con Let’s Encrypt. 

- Realiza backups regulares de la base de datos MongoDB. 

 
