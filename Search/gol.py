# -*- coding: utf-8 -*-
import lucene
vm_env = lucene.initVM(vmargs=['-Djava.awt.headless=true'])
def getenv():
    return vm_env