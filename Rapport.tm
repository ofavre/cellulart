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

    <with|par-left|3fn|Agents <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-8>>

    <with|par-left|3fn|Automates cellulaires
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-9>>

    <with|par-left|3fn|Objets <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-10>>

    <with|par-left|3fn|Requ�tes <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-11>>

    <vspace*|1fn><with|font-series|bold|math-font-series|bold|Agents
    impl�ment�s> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-12><vspace|0.5fn>

    <with|par-left|3fn|Jeu de la vie <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-13>>

    <with|par-left|3fn|Flocking birds <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-14>>

    <with|par-left|3fn|Vaches et herbes <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-15>>

    <with|par-left|3fn|Guardes, voleurs et tr�sors
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-16>>

    <vspace*|1fn><\with|font-series|bold|math-font-series|bold>
      Variation de param�tres
    </with> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-17><vspace|0.5fn>

    <vspace*|1fn><with|font-series|bold|math-font-series|bold|Conclusion>
    <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
    <no-break><pageref|auto-18><vspace|0.5fn>
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
    Variation de param�tres
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
    <associate|auto-12|<tuple|4|3>>
    <associate|auto-13|<tuple|4.0.5|3>>
    <associate|auto-14|<tuple|4.0.6|3>>
    <associate|auto-15|<tuple|4.0.7|3>>
    <associate|auto-16|<tuple|4.0.8|3>>
    <associate|auto-17|<tuple|5|3>>
    <associate|auto-18|<tuple|6|3>>
    <associate|auto-19|<tuple|7|?>>
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

      <with|par-left|<quote|3fn>|Agents <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-8>>

      <with|par-left|<quote|3fn>|Automates cellulaires
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-9>>

      <with|par-left|<quote|3fn>|Objets <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-10>>

      <with|par-left|<quote|3fn>|Requ�tes
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-11>>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Agents
      impl�ment�s> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
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

      <with|par-left|<quote|3fn>|Guardes, voleurs et tr�sors
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-16>>

      <vspace*|1fn><\with|font-series|<quote|bold>|math-font-series|<quote|bold>>
        Variation de param�tres
      </with> <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-17><vspace|0.5fn>

      <vspace*|1fn><with|font-series|<quote|bold>|math-font-series|<quote|bold>|Conclusion>
      <datoms|<macro|x|<repeat|<arg|x>|<with|font-series|medium|<with|font-size|1|<space|0.2fn>.<space|0.2fn>>>>>|<htab|5mm>>
      <no-break><pageref|auto-18><vspace|0.5fn>
    </associate>
  </collection>
</auxiliary>