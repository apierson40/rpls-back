# MEILLEURS AGENTS TEST


## Information générale
Le travail a été réalisé en python avec le framework django.
Un schéma de la base de données est disponible (voir fichier database_schema.png).
Le fichier csv géocodé est rpls_cannes_geocoded_pierson.csv

## Lancement de l'application
Pour lancer l'application, il faut utilise le fichier docker-compose.yml situé dans le dossier rpls-back.
Pour celà il suffit d'appliquer la commande suivant :
```
docker-compose up
```

## Endpoints
J'avais pensé le travail sous forme d'une API. Je n'ai pas eu le temps de faire tout ce que je souhaitais.
Néanmoins, pour lancer le géocodage il faut réaliser une simple requête GET à l'adresse suivante :
```
http://localhost:8000/api/geocodage
```
Et pour l'intégration, il faut réaliser une simple requête GET à l'adresse suivante :
```
http://localhost:8000/api/geocodage
```

## Répertoires
Le rendu est organisé de la façon suivante :
* /rpls-back/app/api/models : contient les objets utilisés en base de données
* /rpls-back/app/api/services : contient les différents traitements effectués
* /rpls-back/app/api/views : contient les vues permettant de lancer les traitements

Le traitement permettant le géocodage se situe dans le dossier de service sous le nom geocodage_service.
Le traitement permettant l'intégration des données se situe dans le dossier de service sous le nom data_integration_service.