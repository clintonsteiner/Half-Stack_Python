Easy reference for find commands I come back to
###############################################

Fix rm to long error
********************

``rm -rf ./*.dat``

.. code-block:: bash

   find . -name "*.rst" -print0 -exec echo {} +
   find . -name "*.rst" -print0 -exec rm -f {} +
