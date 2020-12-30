Points of interest 2
====================

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet neque dui. Cras maximus, purus vel sollicitudin sodales.

.. point-of-interest:: Not in slides
  :id: poi7
  :previous: poi6
  :next: poi10
  :not_in_slides:

  This POI does not appear in the slides compiled with Presentation maker.

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. point-of-interest:: Not in book
  :id: poi8
  :not_in_book:

  This POI does not appear in the A+ chapter.

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. point-of-interest:: No POI box
  :id: poi9
  :no_poi_box:

  This POI does not have the normal borders and distinct colours.

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. define Latex math macros

.. only:: builder_html

  .. raw:: html

    <div style="display:none;">

  .. math::

    \newcommand{\vT}{{\scriptstyle\mathsf{T}}}
    \newcommand{\vF}{{\scriptstyle\mathsf{F}}}
    \newcommand{\limpl}{\rightarrow}
    \newcommand{\lequiv}{\leftrightarrow}
    \newcommand{\xor}{\oplus}

  .. raw:: html

    </div>

.. point-of-interest:: Complex mathematics
  :id: poi10
  :previous: poi7

  This POI contains complex mathematics: truth tables for propositional connectives.

  :math:`\begin{array}{|c|c|} \hline     \alpha & (\neg \alpha) \\ \hline \hline     \vF & \vT \\ \hline     \vT & \vF \\ \hline    \end{array}`
  :math:`~~`
  :math:`\begin{array}{|c|c|c|} \hline    \alpha & \beta & (\alpha\land\beta) \\ \hline \hline    \vF & \vF & \vF \\ \hline    \vF & \vT & \vF \\ \hline    \vT & \vF & \vF \\ \hline    \vT & \vT & \vT \\ \hline    \end{array}`
  :math:`~~`
  :math:`\begin{array}{|c|c|c|} \hline    \alpha & \beta & (\alpha\lor\beta) \\ \hline \hline    \vF & \vF & \vF \\ \hline    \vF & \vT & \vT \\ \hline    \vT & \vF & \vT \\ \hline    \vT & \vT & \vT \\ \hline    \end{array}`
  :math:`~~`
  :math:`\begin{array}{|c|c|c|} \hline    \alpha & \beta & (\alpha\limpl\beta) \\ \hline \hline    \vF & \vF & \vT \\ \hline    \vF & \vT & \vT \\ \hline    \vT & \vF & \vF \\ \hline    \vT & \vT & \vT \\ \hline    \end{array}`
  :math:`~~`
  :math:`\begin{array}{|c|c|c|} \hline    \alpha & \beta & (\alpha\lequiv\beta) \\ \hline \hline    \vF & \vF & \vT \\ \hline    \vF & \vT & \vF \\ \hline    \vT & \vF & \vF \\ \hline    \vT & \vT & \vT \\ \hline    \end{array}`
  :math:`~~`
  :math:`\begin{array}{|c|c|c|} \hline    \alpha & \beta & (\alpha\xor\beta) \\ \hline \hline    \vF & \vF & \vF \\ \hline    \vF & \vT & \vT \\ \hline    \vT & \vF & \vT \\ \hline    \vT & \vT & \vF \\ \hline    \end{array}`

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
