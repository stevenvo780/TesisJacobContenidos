#!/bin/bash
cd /datos/repos/Personal/TesisJacobContenidos
PYTHONUNBUFFERED=1 python3 repos/scripts/auditoria_cientifica_profunda.py > /tmp/audit_full.log 2>&1
echo "DONE exit=$?" >> /tmp/audit_full.log
