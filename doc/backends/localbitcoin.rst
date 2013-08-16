Localbitcoin List
=========
Localbitcoin uses OAuth v2 for Authentication

- Register a new application at the `Localbitcoin List API`_, and

- fill ``Client Id`` and ``Client Secret`` values in the settings::

      LOCALBITCOIN_CLIENT_ID = ''
      LOCALBITCOIN_CLIENT_SECRET = ''

- extra scopes can be defined by using::

    LOCALBITCOIN_AUTH_EXTRA_ARGUMENTS = {'scope': 'email message'}

*Note:*
Localbitcoin List does not currently support returning 'state' variable.

.. _Localbitcoin List API: https://localbitcoins.com/api-docs/
