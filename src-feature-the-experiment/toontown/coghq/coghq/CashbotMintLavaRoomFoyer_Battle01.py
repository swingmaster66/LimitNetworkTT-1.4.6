from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE18a',
        'wantDoors': 1},
 1001: {'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 10004: {'type': 'locator',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 0,
         'searchPath': '**/EXIT1'},
 10013: {'type': 'mintProduct',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10012,
         'pos': Point3(-3.94549632072, 18.2319583893, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12500},
 10014: {'type': 'mintProduct',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10012,
         'pos': Point3(3.85402703285, 18.2319583893, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12500},
 10015: {'type': 'mintProduct',
         'name': 'copy of <unnamed>',
         'comment': '',
         'parentEntId': 10012,
         'pos': Point3(-18.5567684174, 14.1500225067, 6.5729341507),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'mintId': 12500},
 10001: {'type': 'model',
         'name': 'vaultDoor',
         'comment': '',
         'parentEntId': 10004,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/VaultDoorCover.bam'},
 10003: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10002,
         'pos': Point3(13.2311220169, 20.3564720154, 0.305192321539),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.21849691868, 1.21849691868, 1.21849691868),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_A.bam'},
 10007: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10002,
         'pos': Point3(-17.5481491089, 20.8210849762, 0.00756931304932),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.30483365059, 1.30483365059, 1.30483365059),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_F1.bam'},
 10008: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10007,
         'pos': Point3(-1.55398654938, -4.84950685501, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(0.913593888283, 0.913593888283, 0.913593888283),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'},
 10009: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10002,
         'pos': Point3(-19.0412902832, -18.4314842224, 0.00867449026555),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/crates_G1.bam'},
 10010: {'type': 'model',
         'name': '<unnamed>',
         'comment': '',
         'parentEntId': 10002,
         'pos': Point3(18.6662273407, -13.083732605, 0.00570194004104),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': Vec3(1.0, 1.0, 1.0),
         'collisionsOnly': 0,
         'flattenType': 'light',
         'loadType': 'loadModelCopy',
         'modelPath': 'phase_10/models/cashbotHQ/CBMetalCrate.bam'},
 10000: {'type': 'nodepath',
         'name': 'cogs',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Point3(0.0, 0.0, 0.0),
         'scale': 1},
 10002: {'type': 'nodepath',
         'name': 'crates',
         'comment': '',
         'parentEntId': 10011,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1},
 10005: {'type': 'nodepath',
         'name': 'battle',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Point3(-90.0, 0.0, 0.0),
         'scale': 1},
 10011: {'type': 'nodepath',
         'name': 'props',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Point3(-90.0, 0.0, 0.0),
         'scale': 1},
 10012: {'type': 'nodepath',
         'name': 'product',
         'comment': '',
         'parentEntId': 10011,
         'pos': Point3(0.0, 0.0, 0.0),
         'hpr': Vec3(0.0, 0.0, 0.0),
         'scale': 1}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
