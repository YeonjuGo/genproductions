import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
                         comEnergy = cms.double(2760.0),
                         filterEfficiency = cms.untracked.double(1.0000),
                         maxEventsToPrint = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         pythiaPylistVerbosity = cms.untracked.int32(0),

                         filterType     = cms.untracked.string('EcalGenEvtSelectorFrag'),
                         particlePt     = cms.vdouble(35),
                         particleStatus = cms.vint32(1),
                         particles      = cms.vint32(22),
                         etaMax         = cms.double(3),   # Photon eta cut
                         partonStatus = cms.vint32(2, 2, 2, 2, 2, 2, 2, 1),
                         partonPt = cms.vdouble(0,0,0,0,0,0,0,0),
                         partons = cms.vint32(1, 2, 3, 4, 5, 6, 21, 22), # parton cut is not functioning
                         maxTries = cms.untracked.int32(5000),

                         PythiaParameters = cms.PSet(
                             pythiaUESettingsBlock,
                             customProcesses = cms.vstring('MSEL=0   ! User processes'),
                             allQCDPhotonChannel = cms.vstring(    'MSUB(11)=1', # q+q->q+q
                                                                   'MSUB(12)=1', # q+qbar->q+qbar
                                                                   'MSUB(13)=1', # q+qbar->g+g
                                                                   'MSUB(28)=1', # q+g->q+g
                                                                   'MSUB(53)=1', # g+g->q+qbar
                                                                   'MSUB(68)=1', # g+g->g+g
                                                                   # Leading order photons
                                                                   'MSUB(14)=1', # q+qbar->g+gamma
                                                                   'MSUB(18)=1', # q+qbar->gamma+gamma
                                                                   'MSUB(29)=1', # q+g->q+gamma
                                                                   'MSUB(114)=1', # g+g->gamma+gamma
                                                                   'MSUB(115)=1' # g+g->g+gamma
                                                               ),

                             parameterSets = cms.vstring('pythiaUESettings',
                                                         'customProcesses',
                                                         'allQCDPhotonChannel',
                                                         'kinematics'),
                             kinematics = cms.vstring('CKIN(3)=80',
                                                      'CKIN(4)=9999'
                                                  )
                         )
)

ProductionFilterSequence = cms.Sequence(generator)