.. image:: https://gunivers.net/wp-content/uploads/2022/11/Banner.png

📚 Bookshelf Documentation
==========================

🔎 What is it?
--------------

Bookshelf (previously Gunivers Libs) is a modular library datapack designed to help mapmakers to implement common or complexe systems.


.. grid:: 2

    .. grid-item::

        .. button-link:: getting_started.html
            :color: primary
            :align: right
            :shadow:

            👋 Get started!

    .. grid-item::

        .. button-link:: https://www.youtube.com/watch?v=E2nKYEvjETk
            :color: primary
            :align: left
            :outline:

            🎬 Watch trailer

⚙️ Features
-----------

.. grid:: 2

    .. grid-item-card:: 🧮 Math
        :link: math
        :link-type: doc
        :margin: 0 3 0 0

        Basic mathematical function : sin, cos, exp, log, sqrt and much more!

    .. grid-item-card:: 🏷️ ID
        :link: id
        :link-type: doc 
        :margin: 0 3 0 0

        Identity the entities with a unique ID, and use it to create complexe systems!

    .. grid-item-card:: 🔀 Block conversion
        :link: block
        :link-type: doc
        :margin: 0 3 0 0

        Block :octicon:`arrow-switch` Score :octicon:`arrow-switch` Item conversion systems!

    .. grid-item-card:: 🧠 AI tools
        :link: move
        :link-type: doc
        :margin: 0 3 0 0

        Pathfinding, vision and other tools to create NPCs!

    .. grid-item-card:: 🪃 Vectors 
        :link: vector
        :link-type: doc
        :margin: 0 0 0 0

        Give customized trajectories to your entities, which can be deflected by the wind, bounce on blocks etc.

    .. grid-item-card:: 📎 Entity Link
        :link: link
        :link-type: doc
        :margin: 0 0 0 0

        Synchronize the movement of your entities, move consistent entity structures or add mirrors effects

And much more!

🏃 Motivation
-------------

As developers, we know the importance of using libraries to avoid losing time by re-inventing the wheel in each project. But in Minecraft, we often see that mapmakers are not familiar with this concept.

That's why we created this library, to propose a lot of re-usable tools and try to convice mapmakers to become real developers by looking for and using the available tools.

Thus, this lib is not made to propose the best optimized functions or the more accurate ones. Instead, it is designed to be easy to install and use, and propose various features. We give a huge importance to the accessibility and we recommend talented creators to fork this project in order to make their own optimized versions of the lib.

.. epigraph::

    "I have seen further than others because I have stood on the shoulders of giants."

    -- Isaac Newton

🤝 Follow and/or contribute
---------------------------

You can come on `our Discord <https://discord.gg/E8qq6tN>`_ server to talk with us and/or take part of the project!

If you want to contribute, please read at least the "Getting started" section in the `"Contributing" page <https://glib-core.readthedocs.io/en/latest/contributing.html>`_ that contain all the development convention used in this project.

📃 Contents
-----------

.. toctree::
    :maxdepth: 3
    :caption: Info

    getting_started
    contributing.md
    faq
    CHANGELOG.md

.. toctree::
    :maxdepth: 2
    :caption: Libs

    biome
    bitwise
    block
    cache
    color
    health
    id
    item
    link
    location
    mapedit
    math
    memory
    move
    orientation
    schedule
    time
    vector
    view
    xp

.. toctree::
    :maxdepth: 2
    :caption: Systems

    biomedisplayer
    lgdir
