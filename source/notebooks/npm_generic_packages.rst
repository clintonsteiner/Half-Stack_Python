Example Bundling of Package
###########################

Install Verdaccio
#################

.. code-block:: bash
   :linenos:

    npm install verdaccio
    verdaccio

Create example package
######################

.. code:: bash
   :linenos:

    head -c 100M </dev/urandom > myfile

    mkdir -p myPackage/files/
    tar -czf ./myPackage/files/myPackage-1.0.0.tgz myfile

Create package.json file inside myPackage
*****************************************

.. code-block:: JSON

    {
    "name": "myPackage",
    "version": "1.0.0",
    "description": "A generic package tarball",
    "main": "index.js",
    "files": [
      "files/myPackage-1.0.0.tgz"
    ]
    }

Package and upload to local npm server
**************************************

.. code:: bash
   :linenos:

    npm pack myPackage
    npm publish myPackage --registry http://localhost:4873

Install and view package
************************

.. code:: bash
   :linenos:

   npm install myPackage --registry http://localhost:4873
   ls -grtha ./*myPackage*
