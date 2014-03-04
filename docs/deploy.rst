Deployment guide
================

Continuous deployment
---------------------

Whenever a change is pushed to ``master`` branch on GitHub, Travis CI runs all
tests for that commit and if successful pushes that latest code to Heroku.
Heroku then deploys it on http://testpyramidtemplate.herokuapp.com.

In other words, to deploy some code to production do::

    $ git checkout master
    $ git merge <your_feature_branch>
    $ git push origin master

Travis will then build this code and (if successful) deploy to Heroku.

However, merging your own work is discouraged. Rather open up a Pull Request
on GitHub so someone else can go through your changes and confirm they are OK.

If you need to manually push code to Heroku (to skip the Travis step) do this::

    $ heroku login
    $ heroku keys:add
    $ git push heroku master


Staging
-------

If you are preparing a bigger change it is wise to first deploy your code to
staging. Do this by pushing your code to the ``staging`` branch on GitHub::

    $ git checkout staging
    $ git merge <your_feature_branch>
    $ git push origin staging


Troubleshoot Heroku environment
-------------------------------

To build your environment in the same manner as it's built on Heroku do this::

    # Build and start the Heroku environment locally
    $ source bin/activate
    $ pip install -r requirements.txt
    $ foreman start

Heroku uses ``requirements.txt`` to install all dependencies for testpyramidtemplate, make
sure all version pins in ``versions.cfg`` are also present in
``requirements.txt``.


Deploy to your own account
--------------------------

If you want, you can deploy the entire app to your own Heroku account::

    $ heroku login
    $ heroku keys:add
    $ heroku create --stack cedar
    $ heroku apps:rename my-own-testpyramidtemplate-app
    $ git push heroku master  # upload code
    $ heroku addons:add heroku-postgresql:dev
    $ heroku pg:promote <HEROKU_POSTGRESQL_URL>
    $ heroku run 'python -m testpyramidtemplate.scripts.populate'  # populate db
    $ heroku restart  # restart the app so DB changes take effect
    $ heroku logs -t  # see what's going on
    $ heroku open  # open deployed app in your browser

To redeploy, manually push latest changes to Heroku (not GitHub)::

    $ git push heroku master


IRC deploy notifications
------------------------

On every deploy we get an IRC notification in irc.freenode.org#digipub. It's configured with::

    $ heroku addons:add deployhooks:irc \
        --server=irc.freenode.org
        --room=digipub
        --message="{{user}} deployed {{app}} to {{url}}"
