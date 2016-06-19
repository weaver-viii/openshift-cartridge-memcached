# OpenShift Memcached Cartridge

The `memcached` cartridge provides [Memcached](http://www.memcached.org/) on OpenShift, to install  create your app and run:

	rhc cartridge add http://reflector-getupcloud.getup.io/reflect?github=weaver-viii/openshift-cartridge-memcached --app [APP]


## Environment Variables

The `memcached` cartridge provides following environment variables:

    OPENSHIFT_MEMCACHED_HOST         The Memcached IP address
    OPENSHIFT_MEMCACHED_PORT         The Memcached port
    OPENSHIFT_MEMCACHED_USERNAME     Username (if auth enabled)
    OPENSHIFT_MEMCACHED_PASSWORD     Password (if auth enabled)
    
To enable authentication, set user env var ENABLE_SASL=1 and restart your application:

    $ rhc env set ENABLE_SASL=1 --app [APP]"
    $ rhc app stop --app [APP]"
    $ rhc app-start --app [APP]"
