# Dockerfile
FROM python:3.10-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du projet dans le conteneur
COPY . .

# Définir la variable d'environnement PORT (Render utilise $PORT automatiquement)
ENV PORT 10000

# Commande pour lancer l'application avec gunicorn
CMD ["gunicorn", "agent:app", "--bind", "0.0.0.0:10000"]
