armstrong.apps.content
======================
Provides a concrete implementation of the ``ContentBase`` model inside the
`armstrong.core.arm_content`_ package.


.. _armstrong.core.arm_content: https://github.com/armstrong/armstrong.core.arm_content

Usage
-----
You can use this as a base-class for a common "content" type.  You can use this
type of structure inside your Django application to allow cross-content-type
queries.

If you don't need that functionality, you can extend directly from
``armstrong.core.arm_content.models.ContentBase`` to get all of the fields that
are on ``Content`` without having the extra table and relationship specified.


Installation & Configuration
----------------------------
You can install the latest release of ``armstrong.apps.content`` using `pip`_:

::

    pip install armstrong.apps.content

Make sure to add ``armstrong.apps.content`` to your ``INSTALLED_APPS``.  You
can add this however you like.  This works as a copy-and-paste solution:

::

	INSTALLED_APPS += ["armstrong.apps.content", ]

Once installed, you have to run either ``syncdb``, or ``migrate`` if you are
using `South`_.

.. _pip: http://www.pip-installer.org/
.. _South: http://south.aeracode.org/


Contributing
------------

* Create something awesome -- make the code better, add some functionality,
  whatever (this is the hardest part).
* `Fork it`_
* Create a topic branch to house your changes
* Get all of your commits in the new topic branch
* Submit a `pull request`_

.. _Fork it: http://help.github.com/forking/
.. _pull request: http://help.github.com/pull-requests/


State of Project
----------------
Armstrong is an open-source news platform that is freely available to any
organization.  It is the result of a collaboration between the `Texas Tribune`_
and `Bay Citizen`_, and a grant from the `John S. and James L. Knight
Foundation`_.

To follow development, be sure to join the `Google Group`_.

``armstrong.apps.content`` is part of the `Armstrong`_ project.  You're
probably looking for that.

.. _Texas Tribune: http://www.texastribune.org/
.. _Bay Citizen: http://www.baycitizen.org/
.. _John S. and James L. Knight Foundation: http://www.knightfoundation.org/
.. _Google Group: http://groups.google.com/group/armstrongcms
.. _Armstrong: http://www.armstrongcms.org/


License
-------
Copyright 2011-2012 Bay Citizen and Texas Tribune

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
