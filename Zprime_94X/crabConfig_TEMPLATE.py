from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = Configuration()

config.section_('General')
config.General.workArea = 'resultsAna_JOBTAG/'
config.General.requestName = 'OUTFILENAME'
config.General.transferOutputs = True
config.General.transferLogs=True
config.General.failureLimit=1

import os
config.section_('JobType')
config.JobType.scriptExe = 'submitFileCrab.sh'
config.JobType.inputFiles = [
        #os.environ.get('CMSSW_BASE')+'/src/ZZMatrixElement/MEKD',
        os.environ.get('CMSSW_BASE')+'/src/KinZfitter/KinZfitter/ParamZ1',
        os.environ.get('CMSSW_BASE')+'/src/KinZfitter/HelperFunction/hists',
        ]
config.JobType.psetName = 'CFGFILE'
config.JobType.pluginName = 'Analysis'
config.JobType.disableAutomaticOutputCollection = True
config.JobType.outputFiles = ['OUTFILENAME.root']
config.JobType.maxMemoryMB = 2500

config.section_('Data')
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/global/DBSReader/'
config.Data.inputDataset = 'DATASETNAME'
if ('Run2016' in 'DATASETNAME'):
  config.Data.lumiMask = 'Run2016_ReRecoJSON.txt'
  config.Data.splitting = 'EventAwareLumiBased'
  config.Data.unitsPerJob = 100000
else:
  config.Data.splitting = 'FileBased'
  if   (('GluGlu' in 'DATASETNAME') and ('MCFM701' in 'DATASETNAME') and (not 'tau' in 'DATASETNAME')): config.Data.unitsPerJob = 1
  elif (('GluGlu' in 'DATASETNAME') and ('MCFM701' in 'DATASETNAME') and ('tau' in 'DATASETNAME')): config.Data.unitsPerJob = 1
  elif (('GluGlu' in 'DATASETNAME') and (not 'MCFM701' in 'DATASETNAME')): config.Data.unitsPerJob = 1
  elif ('HToZZ' in 'DATASETNAME'): config.Data.unitsPerJob = 1
  elif ('ZZ' in 'DATASETNAME'): config.Data.unitsPerJob = 4
  elif ('TT' in 'DATASETNAME'): config.Data.unitsPerJob = 5
  else: config.Data.unitsPerJob = 1

config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/klo/HZZdNTuple/JOBTAG/'
config.Data.ignoreLocality = True
config.Data.allowNonValidInputDataset = True

config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T2_US_Florida'
config.Site.whitelist = ['T2_US_*']
