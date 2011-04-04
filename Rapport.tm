<TeXmacs|1.0.7.9>

<style|generic>

<\body>
  <doc-data|<doc-title|Cellulart>|<doc-author-data|<author-name|Olivier
  Favre>>||>

  <section|Introduction>

  Cellulart est notre contribution pour le projet de vie artficielle de
  l'option IAD 2011. C'est un logiciel libre disponible sur gitorious �
  l'adresse http://gitorious.org/cellulart/. Ce rapport pr�sente la
  conception du logiciel, en allant des objectifs de conception �
  l'impl�mentation, puis discute � propos des agents impl�ment�s. Le terme \S
  agent \T signifie simplement les diff�rentes �l�ments que nous avions �
  impl�menter : automate cellulaire, syst�me multi-agents, L-System.

  <section|Objectifs>

  Avant d'impl�menter Cellulart, il fallait se mettre d'accord sur un langage
  de programmation � utiliser, mais aussi sur les principes de conceptions
  qui allaient guider le d�veloppement.

  Le premier objectif est la facilit� d'utilisation : il faut que ce soit
  tr�s facile d'ajouter un nouvel agent, de le modifier, bref, d'exp�rimenter
  ! C'est, selon nous, la principale qualit� d'un tel programme, et c'est
  seulement gr�ce � de nombreuses it�rations qu'on peut parvenir � un
  r�sultat correct. C'est aussi cette philosophie qui explique l'interface
  graphique intuitive permettant de g�rer simplement les diff�rents calques
  (affichage ou non, niveau de transparence) et permettant de mettre
  l'animation en pause.

  Le second objectif est la modularit�. Cet objectif d�coule naturellement du
  premier, �tant donn�Nous avons d�cid� de d�couper le programme en
  diff�rents modules bien distincts et ind�pendants les uns des autres. Le
  programme est donc suffisament g�n�rique pour qu'il soit possible d'ajouter
  facilement de nouveaux \S agents \T. L'int�r�t est de pouvoir extr�mement
  facilement d�clarer de nouveaux agents, modifier leur comportement, et
  faire en sorte que le couplage entre ces agents soit extr�mement l�ger. Ce
  couplage faible nous permet d'avoir des interactions tr�s naturelles entre
  les diff�rents agents : il suffit de charger dynamiquer le code n�cessaire
  � ces interactions au d�but de l'impl�mentation, et Cellulart s'occupe du
  reste.

  Le troisi�me objectif est la performance. C'est important mais ne devait
  pas sacrifier les avantages des deux objectifs pr�c�dents. Le programme a
  �t� profil�, les goulots d'�tranglement ont �t�s identifi�s, afin de gagner
  suffisament de performances pour pouvoir avoir l'impression de temps r�el
  dans les cas les plus courants, c'est-�-dire une dizaine d'agents sur une
  grille de 265 par 256 pixels. L'interface graphique a �t� modif� pour
  pouvoir choisir le taux d'affichage. Il est ainsi possible de laisser le
  programme calculer un certain nombre d'it�rations avant d'afficher le
  r�sultats, ce qui est utile lorsque l'on veut avancer rapidement dans le
  temps.

  <section|Impl�mentation>

  <subsection|Coeur>

  <subsubsection|Interface graphique>

  <subsubsection|Gestion des modules>

  <subsection|Modules>

  <subsubsection|Agents>

  <subsubsection|Automates cellulaires>

  <subsubsection|Objets>

  <subsubsection|Requ�tes>

  <section|Agents impl�ment�s>

  <subsubsection|Jeu de la vie>

  <subsubsection|Flocking birds>

  <subsubsection|Vaches et herbes>

  <subsubsection|Guardes, voleurs et tr�sors>

  <\section>
    Sensibilit� aux param�tres
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