<TeXmacs|1.0.7.3>

<style|generic>

<\body>
  \;

  \;

  \;

  \;

  \;

  <doc-data|<doc-title|Cellulart>|<doc-subtitle|Projet du cours Vie
  Artificielle>|<doc-author-data|<author-name|Olivier FAVRE, Haykel HADDAJI,
  Yassin PATEL, Quentin PRADET>>|<doc-date|Lundi 4 Avril 2011>||>

  \;

  \;

  \;

  \;

  <\table-of-contents|toc>
    <vspace*|1fn><with|font-series|bold|math-font-series|bold|Introduction>
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-1><vspace|0.5fn>

    <vspace*|1fn><with|font-series|bold|math-font-series|bold|Objectifs>
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-2><vspace|0.5fn>

    <vspace*|1fn><with|font-series|bold|math-font-series|bold|Implémentation>
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-3><vspace|0.5fn>

    <with|par-left|1.5fn|Coeur <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-4>>

    <with|par-left|3fn|Interface graphique
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-5>>

    <with|par-left|3fn|Gestion des modules
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-6>>

    <with|par-left|1.5fn|Modules <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-7>>

    <with|par-left|3fn|Agents <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-8>>

    <with|par-left|3fn|Automates cellulaires
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-9>>

    <with|par-left|3fn|Objets <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-10>>

    <with|par-left|3fn|Requêtes <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-11>>

    <vspace*|1fn><with|font-series|bold|math-font-series|bold|Agents
    implémentés> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-12><vspace|0.5fn>

    <with|par-left|3fn|Jeu de la vie <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-13>>

    <with|par-left|3fn|Flocking birds <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-14>>

    <with|par-left|3fn|Vaches et herbes <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-15>>

    <with|par-left|3fn|Guardes, voleurs et trésors
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-16>>

    <vspace*|1fn><\with|font-series|bold|math-font-series|bold>
      Variation de paramètres
    </with> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-17><vspace|0.5fn>

    <vspace*|1fn><with|font-series|bold|math-font-series|bold|Conclusion>
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-18><vspace|0.5fn>
  </table-of-contents>

  <page-break*><section|Introduction>

  <em|Cellulart> est notre contribution pour le projet de vie artficielle de
  l'option IAD 2011. C'est un logiciel libre disponible sur gitorious à
  l'adresse <hlink|http://gitorious.org/cellulart/|http://gitorious.org/cellulart/>.
  Ce rapport présente la conception du logiciel, en allant des objectifs de
  conception à l'implémentation, puis discute à propos des agents
  implémentés.

  Le terme \S agent \T signifie simplement les différents éléments que nous
  avions à implémenter : automate cellulaire, système multi-agents,
  L-système.

  <section|Objectifs>

  Avant d'implémenter Cellulart, il fallait se mettre d'accord sur un langage
  de programmation à utiliser, mais aussi sur les principes de conception qui
  allaient guider le développement.

  Le premier objectif est la facilité d'utilisation : il faut que ce soit
  très facile d'ajouter un nouvel agent, de le modifier, bref, d'expérimenter
  ! C'est, selon nous, la principale qualité d'un tel projet, et c'est
  seulement grâce à de nombreuses itérations qu'on peut parvenir à un
  résultat correct. C'est aussi cette philosophie qui explique l'interface
  graphique intuitive permettant de gérer simplement les différents calques
  (affichage ou non, niveau de transparence) et permettant de mettre
  l'animation en pause ou d'en changer la vitesse.

  Le second objectif est la modularité. Cet objectif découle naturellement du
  premier, étant donné que nous avons décidé de découper le programme en
  différents modules bien distincts et faiblement dépendants les uns des
  autres. Le programme est donc suffisament générique pour qu'il soit
  possible d'ajouter facilement de nouveaux \S agents \T. L'intérêt est de
  pouvoir très facilement déclarer de nouveaux agents, modifier leur
  comportement, et faire en sorte que le couplage entre ces agents soit
  extrêmement léger. Ce couplage faible nous permet d'avoir des interactions
  très naturelles entre les différents agents : il suffit de charger
  dynamiquer le code nécessaire à ces interactions au début de
  l'implémentation, et Cellulart s'occupe du reste.

  Le troisième objectif est la performance. C'est important mais ne devait
  pas sacrifier les avantages des deux objectifs précédents. Le programme a
  été profilé, les goulots d'étranglement ont étés identifiés, afin de gagner
  suffisament de performances pour pouvoir avoir l'impression de temps réel
  dans les cas les plus courants, c'est-à-dire une dizaine d'agents sur une
  grille de 265 par 256 pixels. L'interface graphique a été modifé pour
  pouvoir choisir le taux d'affichage. Il est ainsi possible de laisser le
  programme calculer un certain nombre d'itérations avant d'afficher le
  résultat, ce qui est utile lorsque l'on veut avancer rapidement dans le
  temps.

  <section|Implémentation>

  Dans cette section nous allons détailler l'implémentation des diverses
  fonctionnalités du projet.

  <subsection|Coeur>

  Le code étant modulaire, nous allons commencer par décrire la partie
  commune et la partie gérant les modules.

  <subsubsection|Interface graphique>

  Commençons par l'interface graphique, l'endroit le plus facile pour
  comprendre le programme dans sa globalité.

  Elle est décomposée en 2 parties principales : à gauche la visualisation et
  à droite les contrôles. La visualisation est basée sur un composant OpenGL,
  ceci nous permet des manipulations et des compositions rapides des images,
  telles des zoom et déplacements.

  Les contrôles sont eux décomposés en 3 parties.

  La première ligne gère l'animation avec un bouton play, pause-step et une
  réglette de vitesse. La vitesse est spécifiée en millisecondes d'attente
  entre chaque calcul d'itération et d'affichage d'image, ou en millisecondes
  d'attente entre chaque affichage d'image, le calcul des itérations étant
  fait en continu, ou bien encore calcul en continu d'une image et affichage,
  le plus rapidement possible. Le premier mode permet de bien voir le détail
  de ce qui se passe, le second d'accélérer les calculs en perdant moins de
  temps à visualiser, le dernier permet de ne rien rater de ce qui se passe
  en allant le plus vite possible.

  La seconde ligne permet l'exportation de la visualisation en fichier PNG et
  d'en choisir le dossier de destination. La dernière partie enfin est une
  liste des différents calques disponibles. Chaque cache est une matrice de
  valeurs transformée en pixels de couleur. Il est possible d'en gérer
  l'opacité ainsi que l'ordre d'affichage, par glisser-déposer.

  Nous voyons donc ici le premier concept : l'image affichée est formée de
  différentes couches, chacune étant une matrice de données qui subit une
  conversion en pixels. Les pixels et les données sont effectivement
  totalement dissociés. Une palette de couleur est chargée d'en faire la
  conversion. Les palettes sont interchangeables.

  <subsubsection|Gestion des modules>

  Nous manipulons plusieurs composants dans notre projet : des matrices, des
  automates cellulaires, des systèmes multi-agents, des L-systèmes mais
  également des objets arbitraires et des moteurs de requêtes. Les systèmes
  multi-agents sont subdivisés en : états, percepts, actions et cerveaux. Les
  matrices possèdent plusieurs types de bouclage aux bords. Chacun de ces
  types de composants fait l'objet d'une ou de plusieurs classes, ainsi que
  d'une méthode d'instanciation.

  <subsection|Modules>

  <subsubsection|Matrices>

  Elles ont toutes la même dimension que le monde lui même, mais leur type de
  donnée peut varier du flottant au quadruplet d'entiers en passant par des
  objets Python.

  Une matrice possède également des préférences de visualisation (opacité,
  visibilité, palette de couleurs), mais également un système de bouclage aux
  bords. En effet nous pouvons avoir envie que le monde soit torique, ou
  comme un anneau de Mobius.

  Les matrices ont également un code d'initialisation, qui permet par exemple
  de placer certaines valeurs au centre du monde ou sur certaines lignes.

  Elles représentent bien souvent une plateforme de support pour tous les
  agents. Lorsqu'une information est beaucoup plus éparse par contre, on
  utilisera des objets.

  <subsubsection|Automates cellulaires>

  Les automates cellulaires eux se branchent sur une ou plusieurs matrices
  qu'ils peuvent lire ou écrire. Typiquement un automate cellulaire est
  couplé avec une et une seule matrice dont il gère exclusivement la mise à
  jour. Beaucoup de calcul matriciel est utilisé ici via NumPy pour optimiser
  les traitements comme le calcul du nombre de voisins et l'écriture des
  nouvelles valeurs en fonction de tests booléens. Ceci a beaucoup contribué
  à l'accélération des traitements, mais les a aussi complexifiés en les
  rendant moins explicites.

  <subsubsection|Systèmes multi-agents>

  Ce sont des composants très complexes. Chaque agent d'un tel système
  possède des états, des percepts et des actions disponibles, ainsi qu'un ou
  plusieurs cerveaux, centres de décision.

  Un agent possède une collection prédéfinie d'états, qui sont initialisés
  lors de sa naissance, suivant le code donné dans le module représentant
  ledit état. Les états d'un agent est en réalité un dictionnaire qui peut
  être très dynamique en taille comme en type de valeurs.

  Les percepts sont des modules qui sont chargés de retourner une valeur
  particulière, mesure d'une perception de l'agent. Un percept dépend donc
  des états de l'agent, mais également du monde qui l'entoure, il a donc
  accès à tout cela.

  Une action est très similaire à un percept dans son implémentation, mais
  est habité d'un rôle opposé. Une action peut changer un état ou modifier le
  monde, alors qu'un percept ne doit se contenter que d'y accéder en lecture.

  Si des comportements sont indépendants les uns des autres, ils pourront
  alors sans problème être implémentés dans plusieurs cerveaux différents.
  Dans le cas contraire, moyennant une communication entre cerveaux basés sur
  des états particuliers, il est également possible de séparer des
  comportements génériques, bien que cela soit plus difficile.

  <subsubsection|Objets>

  Des objets arbitraires peuvent être créés, supprimés et modifiés. Le monde
  possède une liste d'objet d'un type donné -- un simple nom -- que l'on peut
  récupérer.

  Les objets sont notifiés de leur création, leur suppression mais également
  du fait qu'ils n'aient été laissé tranquilles. Ceci permet par exemple de
  tracer un pixel coloré à une certaine position et de le cacher à leur
  suppression.

  Les objets permettent de stocker une information arbitraire, mais également
  des objets censés être positionnés dans le monde, sur une matrice, mais
  dont la quantité ne justifie par une représentation aussi dense en
  information et difficile à chercher.

  <subsubsection|Requêtes>

  Le moteur de requêtes sert à effectuer un prétraitement unique par
  itération après la mise à jour des automates cellulaires et avant celle des
  systèmes multi-agents, puis doit répondre à de multiples requêtes, en
  général une par agent.

  Ce système permet d'améliorer les performances en optant encore une fois
  pour un point de vue plus macro du problème en construisant une structure
  optimisée de recherche par exemple, afin de perdre moins de temps à
  répondre à chaque requête unique centrée sur le point de vue micro d'un
  l'agent. Il était également nécessaire de suivre le fil des itérations,
  chose qui n'était faisable qu'en créant un véritable moteur de requêtes.

  <section|Agents implémentés>

  <subsubsection|Jeu de la vie>

  <subsubsection|Flocking birds>

  <subsubsection|Vaches et herbe>

  Afin de tester un autre automate cellulaire de notre conception et le
  moteur de requêtes, ainsi que la recherche locale dans des matrices, nous
  avons implémenté une autre démonstration. Cette démonstration était
  également l'occasion de créer une intéraction entre un automate cellulaire
  et les systèmes multi-agents

  Premièrement, l'automate cellulaire a été pense de façon à faire des formes
  rondes, et pleines. Ainsi une cellule survit si au moins 3 de ses voisins
  sont vivants, et une cellule naît si au moins 5 de ses voisins sont
  vivants. Ceci fait des petites \S tâches d'huile \T, que nous avons plutôt
  interprété comme des touffes d'herbe. Cet automate cellulaire est très très
  stable, et il faut un minimum de 4 cellules en carré pour qu'un paquet
  survive.

  Sur cette prairie, des vaches viennent brouter. Si elles voient de la
  nourriture dans un rayon de 4 cases, elles s'y dirigent. Dans le cas
  contraire elle cherchent à se diriger vers la zone la plus dense en herbe
  dans un rayon de 4 zones de 8 cases sur 8 cases (détails plus loin). S'il
  n'y a pas d'herbe en vue dans ce périmètre, la vache avance aléatoirement.
  De plus, dans tous ses déplacements, la vache s'écarte un peu de ses
  voisines dans un rayon de 5 cases, sans pour autant aller faire des virages
  à 180<degreesign> car elle se limite à des ajustements de 30<degreesign>
  par itération.

  Ainsi, une vache effectue une recherche locale dans une matrice, en
  recherchant la case la plus proche possédant de l'herbe. Ceci est fait par
  un percept.

  Mais une vache effectue également une recherche de <em|densité>. Cette
  dernière a été implémentée en réduisant par 8 la taille de la matrice
  d'herbe, de manière à délimiter des zones de 8 cases par 8 cases dont la
  valeur est le nombre de cases d'herbe vivantes dans la zone. Cette étape
  n'est réalisée qu'une fois par itération, grâce au moteur de requêtes.
  Après réduction, chaque vache va réaliser une recherche locale pour la zone
  avec la plus grande valeur dans un rayon de 4 zones. Cette recherche est
  plus semblable au percepts décrit précédement, mais se fait au sein du
  moteur de requête. Il est important de noter que la résolution de la
  réponse retournée est limitée à la taille des zones décrites, dont on
  retourne le centre.

  La réalisation fonctionne comme prévu, mais à cause des faibles ajustement
  de direction, il n'est pas rare qu'une vache passe juste à côté d'une case
  d'herbe, ou se rapproche beaucoup plus de sa voisine que ce que le rayon de
  recherche suggérait. D'un autre côté, la diminution de la densité d'agents
  autonomes est difficile, surtout quand tous les agents se dirigent vers la
  même direction !

  En rajoutant aux vaches une trace qui s'évapore un peu, on remarque
  qu'elles redessinent des bouts des zones qu'elles broutent, en s'attaquant
  par les bords. En effet, le centre d'une touffe repousse instantanément, et
  la vache n'a aucune raison de tourner dans un sens plutôt que dans un
  autre. De ce fait les vaches passent plus de temps à revenir aux bords des
  touffes qu'elles viennent de traverser.

  <subsubsection|Gardes, voleurs et trésors>

  <\section>
    Variation de paramètres
  </section>

  <section|Conclusion>
</body>

<\initial>
  <\collection>
    <associate|language|french>
    <associate|page-medium|paper>
    <associate|page-screen-margin|false>
    <associate|page-show-hf|true>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|auto-1|<tuple|1|2>>
    <associate|auto-10|<tuple|3.2.3|3>>
    <associate|auto-11|<tuple|3.2.4|3>>
    <associate|auto-12|<tuple|3.2.5|3>>
    <associate|auto-13|<tuple|4|3>>
    <associate|auto-14|<tuple|4.0.6|3>>
    <associate|auto-15|<tuple|4.0.7|3>>
    <associate|auto-16|<tuple|4.0.8|3>>
    <associate|auto-17|<tuple|4.0.9|3>>
    <associate|auto-18|<tuple|5|3>>
    <associate|auto-19|<tuple|6|?>>
    <associate|auto-2|<tuple|2|2>>
    <associate|auto-20|<tuple|8|?>>
    <associate|auto-3|<tuple|3|3>>
    <associate|auto-4|<tuple|3.1|3>>
    <associate|auto-5|<tuple|3.1.1|3>>
    <associate|auto-6|<tuple|3.1.2|3>>
    <associate|auto-7|<tuple|3.2|3>>
    <associate|auto-8|<tuple|3.2.1|3>>
    <associate|auto-9|<tuple|3.2.2|3>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Introduction>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Objectifs>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Implémentation>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-3><vspace|0.5fn>

      <with|par-left|<quote|1.5fn>|Coeur <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-4>>

      <with|par-left|<quote|3fn>|Interface graphique
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-5>>

      <with|par-left|<quote|3fn>|Gestion des modules
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-6>>

      <with|par-left|<quote|1.5fn>|Modules
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-7>>

      <with|par-left|<quote|3fn>|Agents <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8>>

      <with|par-left|<quote|3fn>|Automates cellulaires
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-9>>

      <with|par-left|<quote|3fn>|Objets <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-10>>

      <with|par-left|<quote|3fn>|Requêtes
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-11>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Agents
      implémentés> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-12><vspace|0.5fn>

      <with|par-left|<quote|3fn>|Jeu de la vie
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-13>>

      <with|par-left|<quote|3fn>|Flocking birds
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-14>>

      <with|par-left|<quote|3fn>|Vaches et herbes
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-15>>

      <with|par-left|<quote|3fn>|Guardes, voleurs et trésors
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-16>>

      <vspace*|1fn><\with|font-series|<quote|bold>|math-font-series|<quote|bold>>
        Variation de paramètres
      </with> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-17><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Conclusion>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-18><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>