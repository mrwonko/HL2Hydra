import shutil, os

files = [
    # stuff I don't know about
    
    # I don't know about these
    #"gamestate.txt",
    #"demoheader.tmp",
    #"detail.vbsp",
    #"ep1_gamestats.dat",
    #"lights.rad",
    #"voice_ban.dt",

    # meta info about 
    "gameinfo.txt",

    # preload information
    "maplist.txt",

    # binaries
    "bin/Client.dll",
    "bin/server.dll",

    # overwritten camera animation fix (A-Bug)
    "maps/d1_trainstation_04_l_0.lmp",
    "maps/d2_prison_08_l_0.lmp",
    "maps/d3_breen_01_l_0.lmp", # also: mapchange override
    "maps/d1_canals_01a_l_0.lmp",
    "maps/d1_canals_05_l_0.lmp",
    "maps/d3_c17_02_l_0.lmp",
    "maps/ep1_citadel_00_l_0.lmp",
    "models/blackou2.mdl",
    "models/blackou3.mdl",

    # mapchange override
    "maps/ep1_c17_06_l_0.lmp",

    # Regenerated scene cache so scripted sequences play out correctly (A-Bug)
    "scenes/scenes.image",
    
    # chapter preview images
    "materials/vgui/chapters/chapter1.vmt",
    "materials/vgui/chapters/chapter1.vtf",
    "materials/vgui/chapters/chapter2.vmt",
    "materials/vgui/chapters/chapter2.vtf",
    "materials/vgui/chapters/chapter3.vmt",
    "materials/vgui/chapters/chapter3.vtf",
    "materials/vgui/chapters/chapter4.vmt",
    "materials/vgui/chapters/chapter4.vtf",
    "materials/vgui/chapters/chapter5.vmt",
    "materials/vgui/chapters/chapter5.vtf",
    "materials/vgui/chapters/chapter6.vmt",
    "materials/vgui/chapters/chapter6.vtf",
    "materials/vgui/chapters/chapter7.vmt",
    "materials/vgui/chapters/chapter7.vtf",
    "materials/vgui/chapters/chapter8.vmt",
    "materials/vgui/chapters/chapter8.vtf",
    "materials/vgui/chapters/chapter9.vmt",
    "materials/vgui/chapters/chapter9.vtf",
    "materials/vgui/chapters/chapter9a.vmt",
    "materials/vgui/chapters/chapter9a.vtf",
    "materials/vgui/chapters/chapter10.vmt",
    "materials/vgui/chapters/chapter10.vtf",
    "materials/vgui/chapters/chapter11.vmt",
    "materials/vgui/chapters/chapter11.vtf",
    "materials/vgui/chapters/chapter12.vmt",
    "materials/vgui/chapters/chapter12.vtf",
    "materials/vgui/chapters/chapter13.vmt",
    "materials/vgui/chapters/chapter13.vtf",
    "materials/vgui/chapters/chapter14.vmt",
    "materials/vgui/chapters/chapter14.vtf",
    "materials/vgui/chapters/chapter15.vmt",
    "materials/vgui/chapters/chapter15.vtf",
    "materials/vgui/chapters/chapter16.vmt",
    "materials/vgui/chapters/chapter16.vtf",
    "materials/vgui/chapters/chapter17.vmt",
    "materials/vgui/chapters/chapter17.vtf",
    "materials/vgui/chapters/chapter18.vmt",
    "materials/vgui/chapters/chapter18.vtf",
    "materials/vgui/chapters/chapter19.vmt",
    "materials/vgui/chapters/chapter19.vtf",
    "materials/vgui/chapters/chapter20.vmt",
    "materials/vgui/chapters/chapter20.vtf",
    "materials/vgui/chapters/chapter21.vmt",
    "materials/vgui/chapters/chapter21.vtf",
    "materials/vgui/chapters/chapter22.vmt",
    "materials/vgui/chapters/chapter22.vtf",
    "materials/vgui/chapters/chapter23.vmt",
    "materials/vgui/chapters/chapter23.vtf",
    "materials/vgui/chapters/chapter24.vmt",
    "materials/vgui/chapters/chapter24.vtf",
    "materials/vgui/chapters/chapter25.vmt",
    "materials/vgui/chapters/chapter25.vtf",
    "materials/vgui/chapters/chapter26.vmt",
    "materials/vgui/chapters/chapter26.vtf",
    "materials/vgui/chapters/chapter27.vmt",
    "materials/vgui/chapters/chapter27.vtf",
    
    # chapter config
    "cfg/chapter1.cfg",
    "cfg/chapter2.cfg",
    "cfg/chapter3.cfg",
    "cfg/chapter4.cfg",
    "cfg/chapter5.cfg",
    "cfg/chapter6.cfg",
    "cfg/chapter7.cfg",
    "cfg/chapter8.cfg",
    "cfg/chapter9.cfg",
    "cfg/chapter9a.cfg",
    "cfg/chapter10.cfg",
    "cfg/chapter11.cfg",
    "cfg/chapter12.cfg",
    "cfg/chapter13.cfg",
    "cfg/chapter14.cfg",
    "cfg/chapter15.cfg",
    "cfg/chapter16.cfg",
    "cfg/chapter17.cfg",
    "cfg/chapter18.cfg",
    "cfg/chapter19.cfg",
    "cfg/chapter20.cfg",
    "cfg/chapter21.cfg",
    "cfg/chapter22.cfg",
    "cfg/chapter23.cfg",
    "cfg/chapter24.cfg",
    "cfg/chapter25.cfg",
    "cfg/chapter26.cfg",

    # chapter backgrounds
    "scripts/ChapterBackgrounds.txt",

    # credits (essential or it will crash!)
    "scripts/credits.txt",

    # strings
    "resource/hl2hydra_english.txt"
    
]
out_dir = "release/hl2hydra/"

for file in files:
    # try creating folders
    # will throw exception if folder already exists
    src = os.path.normpath(file)
    dst = os.path.normpath(out_dir + file)

    pos = dst.find(os.path.sep)
    while pos != -1:
        try:
            os.mkdir(dst[:pos])
        except:
            pass
        pos = dst.find(os.path.sep, pos+1)
        
    shutil.copy2(src, dst)
