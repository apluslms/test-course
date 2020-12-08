Styles for code blocks
======================


With caption vs Without caption
-------------------------------
.. code-block:: javascript
  :caption: exec.js

  var exec = require('child_process').exec, child;

  child = exec('cat *.js bad_file | wc -l',
      function (error, stdout, stderr) {
          console.log('stdout: ' + stdout);
          console.log('stderr: ' + stderr);
          if (error !== null) {
              console.log('exec error: ' + error);
          }
      });
  child();

.. code-block:: javascript

  var exec = require('child_process').exec, child;

  child = exec('cat *.js bad_file | wc -l',
      function (error, stdout, stderr) {
          console.log('stdout: ' + stdout);
          console.log('stderr: ' + stderr);
          if (error !== null) {
              console.log('exec error: ' + error);
          }
      });
  child();

With caption vs Without caption - With line numbers
---------------------------------------------------
.. code-block:: javascript
  :caption: exec.js
  :linenos:

  var exec = require('child_process').exec, child;

  child = exec('cat *.js bad_file | wc -l',
      function (error, stdout, stderr) {
          console.log('stdout: ' + stdout);
          console.log('stderr: ' + stderr);
          if (error !== null) {
              console.log('exec error: ' + error);
          }
      });
  child();

.. code-block:: javascript
  :linenos:

  var exec = require('child_process').exec, child;

  child = exec('cat *.js bad_file | wc -l',
      function (error, stdout, stderr) {
          console.log('stdout: ' + stdout);
          console.log('stderr: ' + stderr);
          if (error !== null) {
              console.log('exec error: ' + error);
          }
      });
  child();

With caption vs Without caption - With line numbers and without wrapping
------------------------------------------------------------------------

.. code-block:: javascript
  :caption: exec.js
  :linenos:

  var exec = require('child_process').exec, child;

  child = exec('cat *.js bad_file | wc -l',
      function (error, stdout, stderr) {
          console.log('stdout: ' + stdout);
          console.log('stderr: ' + stderr); // The file name is usually relative to the current file’s path. However, if it is absolute (starting with /), it is relative to the top source directory.
          if (error !== null) {
              console.log('exec error: ' + error);
          }
      });
  child();

.. code-block:: javascript
  :linenos:

  var exec = require('child_process').exec, child;

  child = exec('cat *.js bad_file | wc -l',
      function (error, stdout, stderr) {
          console.log('stdout: ' + stdout);
          console.log('stderr: ' + stderr); // The file name is usually relative to the current file’s path. However, if it is absolute (starting with /), it is relative to the top source directory.
          if (error !== null) {
              console.log('exec error: ' + error);
          }
      });
  child();

With caption vs Without caption - Without line numbers and without wrapping
---------------------------------------------------------------------------

.. code-block:: javascript
  :caption: exec.js

  var exec = require('child_process').exec, child;

  child = exec('cat *.js bad_file | wc -l',
      function (error, stdout, stderr) {
          console.log('stdout: ' + stdout);
          console.log('stderr: ' + stderr); // The file name is usually relative to the current file’s path. However, if it is absolute (starting with /), it is relative to the top source directory.
          if (error !== null) {
              console.log('exec error: ' + error);
          }
      });
  child();

.. code-block:: javascript

  var exec = require('child_process').exec, child;

  child = exec('cat *.js bad_file | wc -l',
      function (error, stdout, stderr) {
          console.log('stdout: ' + stdout);
          console.log('stderr: ' + stderr); // The file name is usually relative to the current file’s path. However, if it is absolute (starting with /), it is relative to the top source directory.
          if (error !== null) {
              console.log('exec error: ' + error);
          }
      });
  child();
