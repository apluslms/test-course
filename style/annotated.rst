Annotated code blocks
=====================

Test the annotated directive.

.. annotated::

  .. code-block:: python

    1«def func(param):»
        2«return None»

    3«x = "hello"»
    4«print(x + " world")»
    print("Last line without any annotation")

  Annotations may be written inline within text using square brackets (``[ ]``)
  or as blocks with the ``.. annotation::`` directive.
  Inline annotations look like this: [[[define a **function** named ``func`` that takes one parameter *param*]]].
  You can add a ``data-replacement`` attribute to the HTML code of the inline
  annotation too like this:
  [[[**return statement** ends the function execution and returns a value to the caller¶content for the replacement attribute]]]

  It is up to your custom JavaScript code to do something with the data-replacement
  attribute, but the intended use-case is that the content of the annotated code
  would change when the user hovers over the annotation with the mouse.

  The inline annotations are always numbered before the block annotations.
  This affects the numbers in the annotated code block
  (the sections like ``1«def func(param):»``).

  .. annotation:: optional content for the data-replacement HTML attribute

    Assign a string to the variable x.

  .. annotation::

    The parameters to the function call are evaluated first.


Basic example without any inline annotations
--------------------------------------------

.. annotated::

  .. code-block:: python

    1«def print_numbers(2«until»):»
        3«for i in range(until):»
            print(i)

    4«if __name__ == '__main__':»
        5«import sys»
        if len(sys.argv) < 2:
            sys.exit(1)
        try:
            print_numbers(6«int(sys.argv[1])»)
        7«except ValueError:»
            print("The parameter must be an integer!")

  .. annotation::

    Define the function ``print_numbers`` that takes one parameter.

  .. annotation::

    The parameters are variables that can be used in the function body.
    The function caller supplies the value to the parameter.

  .. annotation::

    Loop from zero to the parameter value minus one.

  .. annotation::

    This if condition is true only if this module is executed as the start of the process:
    ``python modulename.py``.
    Not when this module is imported to another module.

  .. annotation::

    The ``sys`` module needs to be imported so that the command-line parameters can be used.

  .. annotation::

    The command-line parameters are strings, hence the parameter is cast to integer.

  .. annotation::

    If the command-line parameter is not a number, the ``ValueError`` exception is raised.

