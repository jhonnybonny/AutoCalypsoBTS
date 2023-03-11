#!/bin/sh

echo "DB UP"
cd /usr/src/CalypsoBTS
sudo osmo-nitb --yes-i-really-want-to-run-prehistoric-software -c openbsc.cfg -l hlr.sqlite3 -P -C --debug=DRLL:DCC:DMM:DRR:DRSL:DNM
read e 
