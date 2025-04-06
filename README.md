# MISW4502-ProyectoFinal2-Proxy-Service

Este repositorio contiene el código de un servicio proxy desarrollado con **Flask** y desplegado en **Google Cloud Run**. El servicio actúa como intermediario entre un frontend en React desplegado en Cloud Run y un backend en Kubernetes Engine (GKE).

## 📌 Descripción

El servicio proxy permite redirigir solicitudes HTTPS desde el frontend hacia un backend alojado en un clúster de GKE utilizando HTTP. Esto permite mantener un punto único de entrada con HTTPS mientras se comunican servicios internos a través de HTTP.

## 🚀 Características
- Soporte para múltiples métodos HTTP: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`.
- Configuración de variables de entorno para ocultar URL sensibles.
- Despliegue automatizado con **GitHub Actions**.
- Construcción y despliegue de imágenes Docker en **Google Cloud Run**.

## 📂 Estructura del Proyecto
```
MISW4502-ProyectoFinal2-Proxy-Service/
├── .github/
│   └── workflows/
│       └── deploy-proxy.yml
├── main.py
├── Dockerfile
├── requirements.txt
```

## 📦 Requisitos
- Python 3.9
- Flask
- requests
- flask-cors
- Docker
- Google Cloud SDK

## ⚙️ Configuración de Variables de Entorno
Este proyecto utiliza variables de entorno definidas como secretos en GitHub:
- `GCP_CREDENTIALS`: JSON de autenticación de la cuenta de servicio (`key.json`).
- `GCP_PROJECT`: ID del proyecto de Google Cloud (`proyecto-final-452204`).
- `GCP_REGION`: Región de despliegue (`us-central1`).
- `GKE_API_URL`: URL del backend (Ejemplo: `http://34.160.33.188`).

## 📌 Despliegue Continuo con GitHub Actions
El flujo de trabajo se configura en `.github/workflows/deploy-proxy.yml` y se ejecuta en cada push a la rama `main`.

### Pasos del Despliegue:
1. Construcción de la imagen Docker.
2. Subida de la imagen a **Artifact Registry**.
3. Despliegue de la imagen en **Google Cloud Run**.

## 🚀 Despliegue Manual
Si deseas desplegar manualmente desde tu máquina local:
```bash
# Autenticarse con Google Cloud
$ gcloud auth login

# Configurar el proyecto
$ gcloud config set project proyecto-final-452204

# Construir la imagen
$ docker build -t gcr.io/proyecto-final-452204/proxy-service .

# Subir la imagen
$ docker push gcr.io/proyecto-final-452204/proxy-service

# Desplegar en Cloud Run
$ gcloud run deploy proxy-service \
    --image gcr.io/proyecto-final-452204/proxy-service \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars GKE_API_URL=http://34.160.33.188
```

## 📜 Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.

## 📞 Contacto
Desarrollado por **Grupo 18 MISW Proyecto Final**.