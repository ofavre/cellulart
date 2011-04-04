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

    <vspace*|1fn><with|font-series|bold|math-font-series|bold|Impl�mentation>
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

    <with|par-left|3fn|Matrices <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-8>>

    <with|par-left|3fn|Automates cellulaires
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-9>>

    <with|par-left|3fn|Syst�mes multi-agents
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-10>>

    <with|par-left|3fn|Objets <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-11>>

    <with|par-left|3fn|Requ�tes <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-12>>

    <vspace*|1fn><with|font-series|bold|math-font-series|bold|Agents
    impl�ment�s> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-13><vspace|0.5fn>

    <with|par-left|3fn|Jeu de la vie <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-14>>

    <with|par-left|3fn|Flocking birds <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-15>>

    <with|par-left|3fn|Vaches et herbe <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-16>>

    <with|par-left|3fn|Gardes, voleurs et tr�sors
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-17>>

    <vspace*|1fn><\with|font-series|bold|math-font-series|bold>
      Variation de param�tres
    </with> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-18><vspace|0.5fn>

    <with|par-left|1.5fn|Flocking birds <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-19>>

    <with|par-left|1.5fn|Gardes, voleurs et tr�sors
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-20>>

    <vspace*|1fn><with|font-series|bold|math-font-series|bold|Conclusion>
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-24><vspace|0.5fn>
  </table-of-contents>

  <page-break*><section|Introduction>

  <em|Cellulart> est notre contribution pour le projet de vie artficielle de
  l'option IAD 2011. C'est un logiciel libre disponible sur gitorious �
  l'adresse <hlink|http://gitorious.org/cellulart/|http://gitorious.org/cellulart/>.
  Ce rapport pr�sente la conception du logiciel, en allant des objectifs de
  conception � l'impl�mentation, puis discute � propos des agents
  impl�ment�s.

  Le terme \S agent \T signifie simplement les diff�rents �l�ments que nous
  avions � impl�menter : automate cellulaire, syst�me multi-agents,
  L-syst�me.

  <section|Objectifs>

  Avant d'impl�menter Cellulart, il fallait se mettre d'accord sur un langage
  de programmation � utiliser, mais aussi sur les principes de conception qui
  allaient guider le d�veloppement.

  Le premier objectif est la facilit� d'utilisation : il faut que ce soit
  tr�s facile d'ajouter un nouvel agent, de le modifier, bref, d'exp�rimenter
  ! C'est, selon nous, la principale qualit� d'un tel projet, et c'est
  seulement gr�ce � de nombreuses it�rations qu'on peut parvenir � un
  r�sultat correct. C'est aussi cette philosophie qui explique l'interface
  graphique intuitive permettant de g�rer simplement les diff�rents calques
  (affichage ou non, niveau de transparence) et permettant de mettre
  l'animation en pause ou d'en changer la vitesse.

  Le second objectif est la modularit�. Cet objectif d�coule naturellement du
  premier, �tant donn� que nous avons d�cid� de d�couper le programme en
  diff�rents modules bien distincts et faiblement d�pendants les uns des
  autres. Le programme est donc suffisament g�n�rique pour qu'il soit
  possible d'ajouter facilement de nouveaux \S agents \T. L'int�r�t est de
  pouvoir tr�s facilement d�clarer de nouveaux agents, modifier leur
  comportement, et faire en sorte que le couplage entre ces agents soit
  extr�mement l�ger. Ce couplage faible nous permet d'avoir des interactions
  tr�s naturelles entre les diff�rents agents : il suffit de charger
  dynamiquer le code n�cessaire � ces interactions au d�but de
  l'impl�mentation, et Cellulart s'occupe du reste.

  Le troisi�me objectif est la performance. C'est important mais ne devait
  pas sacrifier les avantages des deux objectifs pr�c�dents. Le programme a
  �t� profil�, les goulots d'�tranglement ont �t�s identifi�s, afin de gagner
  suffisament de performances pour pouvoir avoir l'impression de temps r�el
  dans les cas les plus courants, c'est-�-dire une dizaine d'agents sur une
  grille de 265 par 256 pixels. L'interface graphique a �t� modif� pour
  pouvoir choisir le taux d'affichage. Il est ainsi possible de laisser le
  programme calculer un certain nombre d'it�rations avant d'afficher le
  r�sultat, ce qui est utile lorsque l'on veut avancer rapidement dans le
  temps.

  <section|Impl�mentation>

  Dans cette section nous allons d�tailler l'impl�mentation des diverses
  fonctionnalit�s du projet.

  <subsection|Coeur>

  Le code �tant modulaire, nous allons commencer par d�crire la partie
  commune et la partie g�rant les modules.

  <subsubsection|Interface graphique>

  Commen�ons par l'interface graphique, l'endroit le plus facile pour
  comprendre le programme dans sa globalit�.

  Elle est d�compos�e en 2 parties principales : � gauche la visualisation et
  � droite les contr�les. La visualisation est bas�e sur un composant OpenGL,
  ceci nous permet des manipulations et des compositions rapides des images,
  telles des zoom et d�placements.

  Les contr�les sont eux d�compos�s en 3 parties.

  La premi�re ligne g�re l'animation avec un bouton play, pause-step et une
  r�glette de vitesse. La vitesse est sp�cifi�e en millisecondes d'attente
  entre chaque calcul d'it�ration et d'affichage d'image, ou en millisecondes
  d'attente entre chaque affichage d'image, le calcul des it�rations �tant
  fait en continu, ou bien encore calcul en continu d'une image et affichage,
  le plus rapidement possible. Le premier mode permet de bien voir le d�tail
  de ce qui se passe, le second d'acc�l�rer les calculs en perdant moins de
  temps � visualiser, le dernier permet de ne rien rater de ce qui se passe
  en allant le plus vite possible.

  La seconde ligne permet l'exportation de la visualisation en fichier PNG et
  d'en choisir le dossier de destination. La derni�re partie enfin est une
  liste des diff�rents calques disponibles. Chaque cache est une matrice de
  valeurs transform�e en pixels de couleur. Il est possible d'en g�rer
  l'opacit� ainsi que l'ordre d'affichage, par glisser-d�poser.

  Nous voyons donc ici le premier concept : l'image affich�e est form�e de
  diff�rentes couches, chacune �tant une matrice de donn�es qui subit une
  conversion en pixels. Les pixels et les donn�es sont effectivement
  totalement dissoci�s. Une palette de couleur est charg�e d'en faire la
  conversion. Les palettes sont interchangeables.

  <subsubsection|Gestion des modules>

  Nous manipulons plusieurs composants dans notre projet : des matrices, des
  automates cellulaires, des syst�mes multi-agents, des L-syst�mes mais
  �galement des objets arbitraires et des moteurs de requ�tes. Les syst�mes
  multi-agents sont subdivis�s en : �tats, percepts, actions et cerveaux. Les
  matrices poss�dent plusieurs types de bouclage aux bords. Chacun de ces
  types de composants fait l'objet d'une ou de plusieurs classes, ainsi que
  d'une m�thode d'instanciation.

  <subsection|Modules>

  Nous allons maintenant d�crire plus en d�tail la mani�re dont chaque module
  fonctionne.

  <subsubsection|Matrices>

  Elles ont toutes la m�me dimension que le monde lui m�me, mais leur type de
  donn�e peut varier du flottant au quadruplet d'entiers en passant par des
  objets Python.

  Une matrice poss�de �galement des pr�f�rences de visualisation (opacit�,
  visibilit�, palette de couleurs), mais �galement un syst�me de bouclage aux
  bords. En effet nous pouvons avoir envie que le monde soit torique, ou
  comme un anneau de Mobius.

  Les matrices ont �galement un code d'initialisation, qui permet par exemple
  de placer certaines valeurs au centre du monde ou sur certaines lignes.

  Elles repr�sentent bien souvent une plateforme de support pour tous les
  agents. Lorsqu'une information est beaucoup plus �parse par contre, on
  utilisera des objets.

  <subsubsection|Automates cellulaires>

  Les automates cellulaires eux se branchent sur une ou plusieurs matrices
  qu'ils peuvent lire ou �crire. Typiquement un automate cellulaire est
  coupl� avec une et une seule matrice dont il g�re exclusivement la mise �
  jour. Beaucoup de calcul matriciel est utilis� ici via NumPy pour optimiser
  les traitements comme le calcul du nombre de voisins et l'�criture des
  nouvelles valeurs en fonction de tests bool�ens. Ceci a beaucoup contribu�
  � l'acc�l�ration des traitements, mais les a aussi complexifi�s en les
  rendant moins explicites.

  <subsubsection|Syst�mes multi-agents>

  Ce sont des composants tr�s complexes. Chaque agent d'un tel syst�me
  poss�de des �tats, des percepts et des actions disponibles, ainsi qu'un ou
  plusieurs cerveaux, centres de d�cision.

  Un agent poss�de une collection pr�d�finie d'�tats, qui sont initialis�s
  lors de sa naissance, suivant le code donn� dans le module repr�sentant
  ledit �tat. Les �tats d'un agent est en r�alit� un dictionnaire qui peut
  �tre tr�s dynamique en taille comme en type de valeurs.

  Les percepts sont des modules qui sont charg�s de retourner une valeur
  particuli�re, mesure d'une perception de l'agent. Un percept d�pend donc
  des �tats de l'agent, mais �galement du monde qui l'entoure, il a donc
  acc�s � tout cela.

  Une action est tr�s similaire � un percept dans son impl�mentation, mais
  est habit� d'un r�le oppos�. Une action peut changer un �tat ou modifier le
  monde, alors qu'un percept ne doit se contenter que d'y acc�der en lecture.

  Si des comportements sont ind�pendants les uns des autres, ils pourront
  alors sans probl�me �tre impl�ment�s dans plusieurs cerveaux diff�rents.
  Dans le cas contraire, moyennant une communication entre cerveaux bas�s sur
  des �tats particuliers, il est �galement possible de s�parer des
  comportements g�n�riques, bien que cela soit plus difficile.

  <subsubsection|Objets>

  Des objets arbitraires peuvent �tre cr��s, supprim�s et modifi�s. Le monde
  poss�de une liste d'objet d'un type donn� -- un simple nom -- que l'on peut
  r�cup�rer.

  Les objets sont notifi�s de leur cr�ation, leur suppression mais �galement
  du fait qu'ils n'aient �t� laiss� tranquilles. Ceci permet par exemple de
  tracer un pixel color� � une certaine position et de le cacher � leur
  suppression.

  Les objets permettent de stocker une information arbitraire, mais �galement
  des objets cens�s �tre positionn�s dans le monde, sur une matrice, mais
  dont la quantit� ne justifie par une repr�sentation aussi dense en
  information et difficile � chercher.

  <subsubsection|Requ�tes>

  Le moteur de requ�tes sert � effectuer un pr�traitement unique par
  it�ration apr�s la mise � jour des automates cellulaires et avant celle des
  syst�mes multi-agents, puis doit r�pondre � de multiples requ�tes, en
  g�n�ral une par agent.

  Ce syst�me permet d'am�liorer les performances en optant encore une fois
  pour un point de vue plus macro du probl�me en construisant une structure
  optimis�e de recherche par exemple, afin de perdre moins de temps �
  r�pondre � chaque requ�te unique centr�e sur le point de vue micro d'un
  l'agent. Il �tait �galement n�cessaire de suivre le fil des it�rations,
  chose qui n'�tait faisable qu'en cr�ant un v�ritable moteur de requ�tes.

  <section|Agents impl�ment�s>

  <subsubsection|Jeu de la vie>

  Le jeu de la vie est un grand classique que nous avons pris plaisir �
  r�impl�menter. Il n'y a rien de particulier � expliquer concernant son
  impl�mentation : nous mettons � jour la matrice en utilisant les r�gles
  dict�es par Conway. Nous avons d'abord essay� de faire fonctionner un
  planneur pour v�rifier que le comportement �tait correct, puis nous avons
  d�cid� de faire davantages d'exp�rimentations.

  Tout l'int�r�t du jeu de la vie r�side dans l'�tat initial. Nous avons
  essay� des �tats initiaux al�atoires, et il s'av�re que ce n'�tait pas tr�s
  int�ressant. Nous obtenions, apr�s un certain nombre d'it�rations, toujours
  les m�mes motifs. Soit des carr�s qui restaient stables, soit des \S lignes
  \T qui suivaient une rotation de 90<degreesign> � chaque it�ration. Nous
  avons cependant trouv� un motif int�ressant : � partir de deux \S carr�s \T
  imbriqu�s, nous avons d�couvert une suite de sortes d'arabesques
  remarquables. Peu � peu, l'image se stabilise, avant d'arriver sur un cycle
  infini.

  Ce qui est int�ressant ici c'est de voir � quel point de r�gles simples et
  un �tat initial plut�t simple m�ne � des comportements dits \S complexes
  \T, mais a priori pas compliqu�s.

  <subsubsection|Flocking birds>

  Nous avons souhait� poursuivre cette exp�rience en impl�mentant un autre
  syst�me simple. Le principe ici est de simuler le comportement d'une \S
  nu�e \T d'oiseaux, comme on a pu le voir en d�monstration en cours. Le
  principe, commun�ment admis, est plut�t simple : il suffit de trois r�gles
  pour impl�menter ce comportement. C'est donc un choix attirant : facile
  pour la premi�re r�alisation, un certain nombre de param�tres � �tudier, et
  un r�sultat amusant. Les trois r�gles, par ordre d'importance, sont :

  <\itemize-dot>
    <item>�viter les oiseaux proches (pour ne pas les cogner) ;

    <item>suivre la direction des oiseaux autour (pas que les plus proches) ;

    <item>aller dans la m�me direction g�n�rale qu'eux.
  </itemize-dot>

  L'impl�mentation est donc simple : si on est trop proche d'un ou plusieurs
  oiseaux, on les �vite. Sinon, on peut se concentrer sur le fait de suivre
  les oiseaux aux alentours. Le comportement obtenu est assez r�aliste et on
  pourrait vraiment avoir l'impression de se retrouver dans une nu�e.
  Malheureusement, c'est un comportement qui n'est pas facile � montrer dans
  un rapport, et on devra ici se contenter des traces laiss�es par nos
  oiseaux.

  Il est amusant de constater qu'avec deux oiseaux, c'est un cercle entier
  qui est r�alis�. En effet, la r�gle d'�vitement ne se d�clenche pas, et la
  direction moyenne est d�fini par un angle constant de rotation. Dans le
  code, on demande aux agents de se tourner vers la moyenne des positions, ce
  qui donne toujours le m�me angle o� qu'on soit dans le cercle.

  \<less\>ins�rer image bigger.png\<gtr\>

  Ce comportement �mergent est en quelque sorte un �quilibre instable : d�s
  qu'un agent vient perturber nos deux agents, le cercle est cass� et ne se
  reconstruira plus. On obtient au contraire des sortes de zigzag que l'on
  aurait pas pu pr�dire autrement, et qu'il aurait �t� impossible de deviner
  en voyant � chaque instant les positions des oiseaux : seule la trace le
  r�v�le.

  Encore une fois, c'est pr�cis�ment ce genre de comportement inattendus et
  passionants auxquels nous nous attentions avec ce travail : comment
  produire des comportements complexes avec des r�gles simples.

  <subsubsection|Vaches et herbe>

  Afin de tester un autre automate cellulaire de notre conception et le
  moteur de requ�tes, ainsi que la recherche locale dans des matrices, nous
  avons impl�ment� une autre d�monstration. Cette d�monstration �tait
  �galement l'occasion de cr�er une int�raction entre un automate cellulaire
  et les syst�mes multi-agents

  Premi�rement, l'automate cellulaire a �t� pense de fa�on � faire des formes
  rondes, et pleines. Ainsi une cellule survit si au moins 3 de ses voisins
  sont vivants, et une cellule na�t si au moins 5 de ses voisins sont
  vivants. Ceci fait des petites \S t�ches d'huile \T, que nous avons plut�t
  interpr�t� comme des touffes d'herbe. Cet automate cellulaire est tr�s tr�s
  stable, et il faut un minimum de 4 cellules en carr� pour qu'un paquet
  survive.

  Sur cette prairie, des vaches viennent brouter. Si elles voient de la
  nourriture dans un rayon de 4 cases, elles s'y dirigent. Dans le cas
  contraire elle cherchent � se diriger vers la zone la plus dense en herbe
  dans un rayon de 4 zones de 8 cases sur 8 cases (d�tails plus loin). S'il
  n'y a pas d'herbe en vue dans ce p�rim�tre, la vache avance al�atoirement.
  De plus, dans tous ses d�placements, la vache s'�carte un peu de ses
  voisines dans un rayon de 5 cases, sans pour autant aller faire des virages
  � 180<degreesign> car elle se limite � des ajustements de 30<degreesign>
  par it�ration.

  Ainsi, une vache effectue une recherche locale dans une matrice, en
  recherchant la case la plus proche poss�dant de l'herbe. Ceci est fait par
  un percept.

  Mais une vache effectue �galement une recherche de <em|densit�>. Cette
  derni�re a �t� impl�ment�e en r�duisant par 8 la taille de la matrice
  d'herbe, de mani�re � d�limiter des zones de 8 cases par 8 cases dont la
  valeur est le nombre de cases d'herbe vivantes dans la zone. Cette �tape
  n'est r�alis�e qu'une fois par it�ration, gr�ce au moteur de requ�tes.
  Apr�s r�duction, chaque vache va r�aliser une recherche locale pour la zone
  avec la plus grande valeur dans un rayon de 4 zones. Cette recherche est
  plus semblable au percepts d�crit pr�c�dement, mais se fait au sein du
  moteur de requ�te. Il est important de noter que la r�solution de la
  r�ponse retourn�e est limit�e � la taille des zones d�crites, dont on
  retourne le centre.

  La r�alisation fonctionne comme pr�vu, mais � cause des faibles ajustement
  de direction, il n'est pas rare qu'une vache passe juste � c�t� d'une case
  d'herbe, ou se rapproche beaucoup plus de sa voisine que ce que le rayon de
  recherche sugg�rait. D'un autre c�t�, la diminution de la densit� d'agents
  autonomes est difficile, surtout quand tous les agents se dirigent vers la
  m�me direction !

  En rajoutant aux vaches une trace qui s'�vapore un peu, on remarque
  qu'elles redessinent des bouts des zones qu'elles broutent, en s'attaquant
  par les bords. En effet, le centre d'une touffe repousse instantan�ment, et
  la vache n'a aucune raison de tourner dans un sens plut�t que dans un
  autre. De ce fait les vaches passent plus de temps � revenir aux bords des
  touffes qu'elles viennent de traverser.

  <subsubsection|Gardes, voleurs et tr�sors>

  Une des premi�res et des plus jolies d�monstrations que nous avons
  impl�ment�es simule un mode avec quelques tr�sors qui attirent les
  convoitises de quelques voleurs, mais surveill�s par un bon nombre de
  gardes.

  Les tr�sors sont des objets dont la valeur se limitent � leur coordonn�es,
  car il sont cens�s �tre plac�s dans le monde. Les fonctions de tr�sors ne
  font que dessiner ou cacher le pixel color� jaune qui marque leur position.
  Le fait que leur valeur soit �gale � leur coordonn�es nous permet surtout
  de pouvoir faire une recherche locale.

  Un voleur se dirige, lentement, en marchant, vers le tr�sor le plus proche.
  Il se ballade al�atoirement si aucun n'est en vue dans un rayon de 50
  cases. Une fois que le voleur passe sur le tr�sor, il le ramasse -- le
  supprime du monde -- et prend les jambes � son coup pour ent�mer une folle
  course poursuite ! Un voleur en fuite cherche � �viter les 5 gardes les
  plus proches de lui, dans un rayon de 20 cases. Il �vite leur position
  moyenne, pond�r�e par leur rapprochement.

  Les gardes quant � eux marchent al�atoirement, au milieu des passants --
  les voleurs qui ont encore les mains vides (distinction faite en observant
  l'�tat des agents voisins). Lorsqu'un garde aper�oit un voleur, dans un
  rayon de 50 cases, il fonce vers lui pour le rattraper. S'il en voit
  plusieurs il se dirige vers le plus proche. Si le garde se trouve � moins
  d'une case du voleur, il lui prend le tr�sor (en modifiant l'�tat du voleur
  qui se remet alors � marcher). Une fois qu'un garde a confisqu� un tr�sor,
  il trotine et cherche � s'�loigner le plus possible des passants -- des
  voleurs potentiels -- et d�pose le tr�sor (en recr�e un nouveau avec ses
  nouvelles coordonn�es) si personne n'est � moins de 50 cases. Une fois le
  tr�sor repos�, il recommence � marcher et peut recommencer � scruter les
  horizons pour voir un �ventuel voleur.

  Afin de faire un joli rendu, nous avons attribu� une couleur � chaque
  garde, et nous avons fait en sorte qu'il laisse une trace color�e lorsqu'il
  se met � courses un voleur. On observe alors un regroupement de plusieurs
  lignes lors du d�but d'une course poursuite. Lors de virages serr�s
  (lorsqu'un garde libre s'interpose devant un voleur) les lignes se
  d�serrent. Il arrive �galement qu'une ligne passe d'un faisceau � un autre,
  quand deux courses poursuites se croisent.

  Nous avons rencontr� un probl�me lors de cette d�monstration : les agents
  ne pouvant pas r�guler leur vitesse, certains se retrouvaient � tourner
  sans cesses autour du m�me point. Par exemple un voleur ayant un mauvais
  angle d'arriv�e vers un tr�sor (ne venant pas de tout droit), va se mettre
  � tourner autours, comme s'il gravitait. Quelques fois, et c'�tait plus
  emb�tant � cause de la trace, les gardes et le voleur tournaient en rond
  sur eux m�mes, souvent jusqu'� ce qu'un nouveau garde vienne \S casser la
  boucle \T.

  <\section>
    Variation de param�tres
  </section>

  <subsection|Flocking birds>

  <subsection|Gardes, voleurs et tr�sors>

  Regardons plus en d�tail l'astuce permettant d'�viter des boucles
  infernales.

  Lors de la course poursuite, il ne faut surtout pas d�passer le voleur,
  sinon il va se mettre � tourner tr�s fortement. Pour �viter cela, il faut
  que le garde d�cel�re lorsqu'il est � une case du voleur (�tant donn� que
  le garde en course poursuite avance d'une case par it�ration). Nous avons
  d�cid� de le faire avancer de la distance qui le s�pare du voleur, moins
  une certaine quantit� fixe, le tout restant scrupuleusement born� entre 0
  et 1. On a donc :

  <\equation*>
    <with|mode|text|<em|speed>> = min<left|(>1.00, \ max<left|(><rsub|>0.00,
    \ <with|mode|text|<em|distance>>-\<varepsilon\><right|)><right|)>
  </equation*>

  Voici les diff�rents r�sultats obtenus pour des valeurs de
  <math|\<varepsilon\>> comprises entre 0 et 1 :

  <big-figure||>

  <big-figure||>

  <big-figure||>

  <section|Conclusion>

  Si nous n'avons pas sp�cialement mis l'accent sur la beaut� des images
  g�n�r�es, nous avons surtout cherch� � cr�er une architecture extr�mement
  modulaire et riche en fonctionnalit�s, tout en gardant de bonnes
  performances malgr� l'utilisation d'un langage interpr�t�.

  Notre projet est libre et disponible sous licence BSD. Nous esp�ront que
  cette disponibilit� libre ainsi que la modularit� et la multitude de
  fonctionnalit�s int�resseront d'autres personnes � la recherche d'une
  plateforme de simulation ou d'art num�rique !
</body>

<\initial>
  <\collection>
    <associate|language|french>
    <associate|page-medium|paper>
    <associate|page-screen-margin|false>
    <associate|page-show-hf|true>
    <associate|par-hyphen|normal>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|auto-1|<tuple|1|2>>
    <associate|auto-10|<tuple|3.2.3|3>>
    <associate|auto-11|<tuple|3.2.4|4>>
    <associate|auto-12|<tuple|3.2.5|4>>
    <associate|auto-13|<tuple|4|4>>
    <associate|auto-14|<tuple|4.0.6|4>>
    <associate|auto-15|<tuple|4.0.7|5>>
    <associate|auto-16|<tuple|4.0.8|5>>
    <associate|auto-17|<tuple|4.0.9|6>>
    <associate|auto-18|<tuple|5|7>>
    <associate|auto-19|<tuple|5.1|7>>
    <associate|auto-2|<tuple|2|2>>
    <associate|auto-20|<tuple|5.2|7>>
    <associate|auto-21|<tuple|1|7>>
    <associate|auto-22|<tuple|2|7>>
    <associate|auto-23|<tuple|3|7>>
    <associate|auto-24|<tuple|6|7>>
    <associate|auto-3|<tuple|3|2>>
    <associate|auto-4|<tuple|3.1|2>>
    <associate|auto-5|<tuple|3.1.1|2>>
    <associate|auto-6|<tuple|3.1.2|3>>
    <associate|auto-7|<tuple|3.2|3>>
    <associate|auto-8|<tuple|3.2.1|3>>
    <associate|auto-9|<tuple|3.2.2|3>>
  </collection>
</references>

<\auxiliary>
  <\collection>
    <\associate|figure>
      <tuple|normal||<pageref|auto-21>>

      <tuple|normal||<pageref|auto-22>>

      <tuple|normal||<pageref|auto-23>>
    </associate>
    <\associate|toc>
      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Introduction>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-1><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Objectifs>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-2><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Impl�mentation>
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

      <with|par-left|<quote|3fn>|Matrices
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8>>

      <with|par-left|<quote|3fn>|Automates cellulaires
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-9>>

      <with|par-left|<quote|3fn>|Syst�mes multi-agents
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-10>>

      <with|par-left|<quote|3fn>|Objets <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-11>>

      <with|par-left|<quote|3fn>|Requ�tes
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-12>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Agents
      impl�ment�s> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-13><vspace|0.5fn>

      <with|par-left|<quote|3fn>|Jeu de la vie
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-14>>

      <with|par-left|<quote|3fn>|Flocking birds
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-15>>

      <with|par-left|<quote|3fn>|Vaches et herbe
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-16>>

      <with|par-left|<quote|3fn>|Gardes, voleurs et tr�sors
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-17>>

      <vspace*|1fn><\with|font-series|<quote|bold>|math-font-series|<quote|bold>>
        Variation de param�tres
      </with> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-18><vspace|0.5fn>

      <with|par-left|<quote|1.5fn>|Flocking birds
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-19>>

      <with|par-left|<quote|1.5fn>|Gardes, voleurs et tr�sors
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-20>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Conclusion>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-24><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>