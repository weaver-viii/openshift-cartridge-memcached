# OpenShift Memcached Cartridge

The `memcached` cartridge provides [Memcached](http://www.memcached.org/) on OpenShift, to install  create your app and run:

	rhc add-cartridge http://reflector-getupcloud.getup.io/reflect?github=getupcloud/openshift-origin-cartridge-memcached --app [APP]

## Environment Variables

The `memcached` cartridge provides several environment variables to reference for ease
of use:

    OPENSHIFT_MEMCACHED_HOST      The Memcached IP address
    OPENSHIFT_MEMCACHED_PORT      The Memcached port

For more information about environment variables, consult the
[OpenShift Application Author Guide](https://github.com/openshift/origin-server/blob/master/node/README.writing_applications.md).
