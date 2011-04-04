<TeXmacs|1.0.7.9>

<style|generic>

<\body>
  <doc-data|<doc-title|Cellulart>|<doc-author-data|<author-name|Olivier
  Favre>>||>

  <section|Introduction>

  Cellulart est notre contribution pour le projet de vie artficielle de
  l'option IAD 2011. C'est un logiciel libre disponible sur gitorious à
  l'adresse http://gitorious.org/cellulart/. Ce rapport présente la
  conception du logiciel, en allant des objectifs de conception à
  l'implémentation, puis discute à propos des agents implémentés. Le terme \S
  agent \T signifie simplement les différentes éléments que nous avions à
  implémenter : automate cellulaire, système multi-agents, L-System.

  <section|Objectifs>

  Avant d'implémenter Cellulart, il fallait se mettre d'accord sur un langage
  de programmation à utiliser, mais aussi sur les principes de conceptions
  qui allaient guider le développement.

  Le premier objectif est la facilité d'utilisation : il faut que ce soit
  très facile d'ajouter un nouvel agent, de le modifier, bref, d'expérimenter
  ! C'est, selon nous, la principale qualité d'un tel programme, et c'est
  seulement grâce à de nombreuses itérations qu'on peut parvenir à un
  résultat correct. C'est aussi cette philosophie qui explique l'interface
  graphique intuitive permettant de gérer simplement les différents calques
  (affichage ou non, niveau de transparence) et permettant de mettre
  l'animation en pause.

  Le second objectif est la modularité. Cet objectif découle naturellement du
  premier, étant donnéNous avons décidé de découper le programme en
  différents modules bien distincts et indépendants les uns des autres. Le
  programme est donc suffisament générique pour qu'il soit possible d'ajouter
  facilement de nouveaux \S agents \T. L'intérêt est de pouvoir extrêmement
  facilement déclarer de nouveaux agents, modifier leur comportement, et
  faire en sorte que le couplage entre ces agents soit extrêmement léger. Ce
  couplage faible nous permet d'avoir des interactions très naturelles entre
  les différents agents : il suffit de charger dynamiquer le code nécessaire
  à ces interactions au début de l'implémentation, et Cellulart s'occupe du
  reste.

  Le troisième objectif est la performance. C'est important mais ne devait
  pas sacrifier les avantages des deux objectifs précédents. Le programme a
  été profilé, les goulots d'étranglement ont étés identifiés, afin de gagner
  suffisament de performances pour pouvoir avoir l'impression de temps réel
  dans les cas les plus courants, c'est-à-dire une dizaine d'agents sur une
  grille de 265 par 256 pixels. L'interface graphique a été modifé pour
  pouvoir choisir le taux d'affichage. Il est ainsi possible de laisser le
  programme calculer un certain nombre d'itérations avant d'afficher le
  résultats, ce qui est utile lorsque l'on veut avancer rapidement dans le
  temps.

  <section|Implémentation>

  <subsection|Coeur>

  <subsubsection|Interface graphique>

  <subsubsection|Gestion des modules>

  <subsection|Modules>

  <subsubsection|Agents>

  <subsubsection|Automates cellulaires>

  <subsubsection|Objets>

  <subsubsection|Requêtes>

  <section|Agents implémentés>

  <subsubsection|Jeu de la vie>

  <subsubsection|Flocking birds>

  <subsubsection|Vaches et herbes>

  <subsubsection|Guardes, voleurs et trésors>

  <\section>
    Sensibilité aux paramètres
  </section>

  <section|Conclusion>
</body>

<\initial>
  <\collection>
    <associate|language|french>
  </collection>
</initial>

<\references>
  <\collection>
    <associate|auto-1|<tuple|1|?>>
    <associate|auto-10|<tuple|3.2.3|?>>
    <associate|auto-11|<tuple|3.2.4|?>>
    <associate|auto-12|<tuple|4|?>>
    <associate|auto-13|<tuple|4.0.5|?>>
    <associate|auto-14|<tuple|4.0.6|?>>
    <associate|auto-15|<tuple|4.0.7|?>>
    <associate|auto-16|<tuple|4.0.8|?>>
    <associate|auto-17|<tuple|5|?>>
    <associate|auto-18|<tuple|6|?>>
    <associate|auto-19|<tuple|7|?>>
    <associate|auto-2|<tuple|2|?>>
    <associate|auto-20|<tuple|8|?>>
    <associate|auto-3|<tuple|3|?>>
    <associate|auto-4|<tuple|3.1|?>>
    <associate|auto-5|<tuple|3.1.1|?>>
    <associate|auto-6|<tuple|3.1.2|?>>
    <associate|auto-7|<tuple|3.2|?>>
    <associate|auto-8|<tuple|3.2.1|?>>
    <associate|auto-9|<tuple|3.2.2|?>>
  </collection>
</references>