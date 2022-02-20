# Emplacement des ensembles de données
Ce répertoire contient trois autres dossiers liés aux jeux de données et appelés **raw**, **processed**, **cleaned**. Une description de chacun est donnée ci-dessous.

## Répertoire raw
Ce répertoire contient des ensembles de données originaux et immuables. Ne pas toucher aux données brutes, en particulier avec Excel. 
Ce répertoire contient deux sous-dossiers, chacun contenant des données relatives aux étages. 
Le premier est lié au rez-de-chaussée et le second au premier étage. 
Chaque nom de sous-dossier commence par la localisation et se termine le jour de la mesure. 
Chaque sous-dossier contient des fichiers de données liés à la force du signal de chaque réseau Wi-Fi annoncé par les SSIDs. 
Le nom du fichier comporte plusieurs parties séparées par un - et la dernière partie indique l'endroit où la mesure a été réalisée selon le plan du bâtiment. 
Tous les fichiers de données ont la structure suivante :

- le nom du réseau Wi-Fi,
- l'adresse MAC virtuelle annonçant le réseau.
- la puissance du signal (dBm).

L'adresse MAC virtuelle est codée directement dans une chaîne de bits (b' '), pour représenter le format hexadécimal.

## Répertoire processed
Ce répertoire contient des ensembles de données transformées intermédiaires.

## Répertoire others
Ce dossier contient des fichiers qui nous ont été utiles à la réalisation de la SAE, qui ne nous servent plus mais que nous voulons gardr en cas de problèmes

