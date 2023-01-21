# Projet-Python
Ce premier scan entièrement codé en python permet de récupérer les ports open ainsi qu'un whois simple à partir d'une url ou d'une IP. Simple d'utilisation vu que tout est indiqué au niveau de la marche à suivre ex : google.fr Il va faire un Reverse host et nous indiqué l'IP puis va nous demandez le min et max port à scanner. Cela permet de cibler vraiment une plage de port.

Ce script utilise les modules socket pour scanner les ports et requests pour effectuer une requête HTTP pour récupérer les informations Whois via https://who.is . Il prend en entrée une adresse IP ou un nom d'hôte qui est ensuite passé aux fonctions de scan de ports et de requête Whois. La fonction port_scan() utilise la méthode connect_ex() pour vérifier si un port est ouvert ou fermé sur l'adresse IP spécifiée, et la fonction whois() utilise l'API Whois pour récupérer les informations Whois pour l'adresse IP ou le nom d'hôte spécifié.

Il est important de noter que la plupart des systèmes d'exploitation ont des protections contre les scans de ports non autorisés, il est donc important de ne pas utiliser ce script pour des activités illégales ou nuisibles.
Il est également important de noter que https://who.is ne permet pas un grand nombre de requêtes par jour, il est donc important de vérifier les limites d'utilisation avant de l'utiliser en production.
