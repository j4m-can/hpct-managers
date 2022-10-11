# hpct-managers

This package provides the `Manager` class and a collection of commonly
used manager implementations.

## Manager Class
The base `Manager` class defines a common set of methods that managers
will provide.

The design goals of the `Manager` class are:
1. To manage one or more underlying service/server/resources.
2. To provide only high-level operations which either succeed or fail.
3. To not provide control over low-level, individual items.

## Managers

Manager implementations are found under `lib/hpctlib/ext`. Managers
are generally intended to be standalone. However, some managers may
be "super" managers and superintend other managers.

