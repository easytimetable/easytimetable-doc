Organisation et Difficultés rencontrées
########################################

Organisation
=============

Attribution des rôles
----------------------

Le seul rôle spécifique que nous ayons attribué était celui de chef de projet,
qui est allé à Alexis en raison de son expérience sur des projets similaires.

Par ailleurs, nous avons tous effectué les tâches selon ce qui nous intéressait.
Nicolas à pu par exemple travailler sur la mise en place d'un système extensible
de gestion d'éléments (CRUD) alors que Guillaume s'occupait de la gestion du
calendrier. Nous avons tous travaillé sur quasiment l'ensemble des
fonctionnalités du logiciel, lorsque nous voyions des modifications à y apporter.

Répartition des tâches
----------------------

Travaux centraux
'''''''''''''''''

Notre équipe s'est réunie très tôt pour décider du déroulement du projet.
Lors de ces premières réunions, et après une première ébauche réalisée en commun
du modèle de données, nous avons décidé de diviser le projet selon les 4
ressources que nous avons manipulé :

     - Les évènements
     - La pédagogie
     - Les espaces
     - Les classes

La gestion des évènements a été confiée principalement à Alexis et Guillaume,
celle de la pédagogie et des espaces à Julien et Nicolas.

Ces assignations n'ont bien évidement empêché personne de se pencher sur une
autre ressource que la sienne, et chaque membre a eu l'occasion de travailler
avec chacun des trois autres sur chaque partie.

Travaux périphériques
'''''''''''''''''''''' 

En plus des tâches directement relatives au métier, la réalisation de
l'application a nécessité d'autres travaux relatifs à l'infrastructure et à la
création de l'environnement de développement.

Ces tâches ont notamment été :

    - La création d'un dépôt git [*]_ (sur github)
    - La mise en place d'un squelette d'application
    - La rédaction de la présente documentation


Difficultés
============

Design
-------

La réalisation d'une telle application a nécessité une importante réflexion lors
de sa conception.

L'ensemble de l'application reposant sur le modèle, toute l'équipe a
participé à son écriture, et nous n'avons dû y apporter que des modifications
mineures au cours du projet.


Javascript et FullCalendar
---------------------------

Pour l'affichage du calendrier et des évènements, nous avons choisi d'utiliser
la bibliothèque FullCalendar [*]_ dont il nous a été nécessaire d'appréhender le
fonctionnement.

Nous nous sommes également  heurtés à notre méconnaissance du Javascript, que
nous avons surmonté, non sans difficultés (gestion des dates, par exemple).


Division du groupe
-------------------

Il a été de plus en plus difficile pour notre équipe de dégager du temps en
commun pour des réunions d'avancement. Nous avons cependant réussi à pallier ce
problème grâce à Mumble [*]_ et au fait que nous étions suffisamment avancés pour
permettre un développement relativement indépendant des différentes parties de
l'application.

.. [*] Git est un logiciel de gestion de versions décentralisé. C'est un
   logiciel libre créé par Linus Torvalds, le créateur du noyau Linux, et
   distribué sous la GNU GPL version 2. : http://git-scm.om
.. [*] Fullcalendar est une bibliothèque Javascript dédiée à l'affichage de
   calendriers : http://arshaw.com/fullcalendar/
.. [*] "Mumble is an open source, low-latency, high quality voice chat software
   primarily intended for use while gaming." : http://mumble.sourceforge.net/
