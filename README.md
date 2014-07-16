E64-SHA512 Password Generator
=============================

This is a set of implementations (for now only python) for a specific password generator invented to follow as closely as possible a specific set of rules.

Rules to follow:
----------------

* Passwords should be generated uniquely from an identifier and a master password
* Password generation should be deterministic in order to retrieve a password later
* Passwords should be secure (wide alphabet and sufficient number of characters)
* Passwords shouldn't be stored, can't be stolen or lost

Specifics of the implementation:
--------------------------------

* The password is generated from the SHA512 hash of a seed
* The seed starts off from the concatenation of the identifier and the master password
* The hash is cropped to a certain number of characters (default is 12)
* The cropped hash is translated in the specified password valid characters
* Valid characters are #$%*0123456789:@ABCDEFGHJKLMNPRSTUVWXYZabcdefghijkmnopqrstuvwxyz (64 in total)
* The translated cropped hash is checked if it is secure
* A string is secure if it has chars from 0-9, a-z, A-Z and other characters
* If the generated password isn't secure, the char '*' is added to the seed
* The process is repeated till a secure password is found

Advise on using this password generator:
----------------------------------------

* Usually the identifier would be the name of the service you need a password for
* If you have more than one account use the service name + account name as an identifier
* If you need to change your password add a '*' to your usual identifier (remember that)
* If you change your password frequently add a date you'll remember to your usual identifier
