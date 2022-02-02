#!/bin/sh

cd /usr/src/CalypsoBTS
sudo osmo-bts-trx -c osmo-bts-trx-calypso.cfg --debug DRSL:DOML:DLAPDM
read e 
