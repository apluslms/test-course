Points of interest 1
====================

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet neque dui. Cras maximus, purus vel sollicitudin sodales, magna enim porta tortor, quis lobortis eros nunc a urna.

.. point-of-interest:: The beginning
  :id: poi1
  :next: poi2

  Some content in the point of interest.

  Some text here and a list:

  * item 1
  * item 2

  ===== =====
  Col A Col B
  ===== =====
  daa   foo
  baz   bar
  ===== =====

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. point-of-interest:: Column-row example
  :id: poi2
  :previous: poi1
  :next: poi3
  :hidden:

  .. row::

    .. column::
      :width: 8
      :column-class: bg-warning

      col-8

      .. row::

        .. column::
          :width: 6
          :column-class: bg-light

          col-6

        .. column::
          :width: 6
          :column-class: bg-secondary

          col-6

    .. column::
      :width: 4
      :column-class: bg-success

      col-4

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. point-of-interest:: Mathematics
  :id: poi3
  :previous: poi2
  :next: poi4

  **Bolded text**

  Inline mathematics like :math:`a + b * 6` and a display equation next:

  .. math::

    x = y^2 - z_2

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. point-of-interest:: Code block
  :id: poi4
  :previous: poi3
  :next: poi5

  Python code block next:

  .. code-block:: python

    a = 6
    c = 2 * a + 7
    print(c + 2)

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. point-of-interest:: Example image
  :id: poi5
  :previous: poi4
  :next: poi6

  This POI contains an image.

  .. figure:: /images/apluslogo.png
    :alt: Aplus logo

    A+ logo

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

.. point-of-interest:: Background image
  :id: poi6
  :previous: poi5
  :next: poi7
  :bgimg: water-background.jpeg

  This POI has a background image.

Lorem ipsum dolor sit amet, consectetur adipiscing elit.
