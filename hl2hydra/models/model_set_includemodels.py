# changes the given model, setting its includemodels to the list of given includemodels.
def SetIncludeModels(inname, filename, includeModels):
    print("Copying file...")
    import shutil
    shutil.copy2(inname, filename)
    with open(filename, mode="r+b") as file:
        print("Successfully opened \"{}\"".format(filename))
        headerStart = file.read(4+4+4+64+4)
        if len(headerStart) < 80:
            print("Could not read header start")
            return False
        import struct
        fileId, version, length = struct.unpack("4si4x64xi", headerStart)
        if fileId != b'IDST':
            print("file ID is not IDST")
            return False
        if version not in [44, 45]: # I'm not sure this works for 44
        #if version != 45:
            print("Version is not 45 (is {})".format(version))
            return False
        print("Is valid file.")
        print("Changing include models")
        file.seek(0x150) # position of includemodel_count, which is followed by includemodel_index
        # we're going to append this at the end of the file, so write that into the header...
        numIncludeModels = len(includeModels)
        print("numIncludeModels: {}".format(numIncludeModels))
        file.write(struct.pack("2i", numIncludeModels, length))
        # ... and write the actual info at the file's end (I leave the old information where it was so I don't have to recalculate any offsets
        charsSoFar = 0
        file.seek(length)
        for index, model in enumerate(includeModels):
            file.write(struct.pack("2i", 0, (numIncludeModels - index) * 8 + charsSoFar))
            charsSoFar += len(model) + 1; # will be written as nullterminated string
        assert(file.tell() == length + numIncludeModels * 8)
        for model in includeModels:
            assert(len(model.encode() + b"\x00") == len(model) + 1)
            file.write(model.encode() + b"\x00")
        #write new file length
        newLength = file.tell()
        file.seek(4+4+4+64)
        file.write(struct.pack("i", newLength))
        print("Done")
        return True
    return False

# fix alyx
# """
alyxModels = [
    "models/alyx_animations.mdl",
    "models/alyx_postures.mdl",
    "models/alyx_gestures.mdl",
    "models/humans/female_shared.mdl",
    "models/humans/female_ss.mdl",
    # new: ep1 animations
    "models/alyx_animat_ep1.mdl",
    "models/alyx_gest_ep1.mdl",
    "models/alyx_post_ep1.mdl",
    # new: hl2 animations
    "models/alyx_animat_hl2.mdl",
    "models/alyx_gest_hl2.mdl",
    "models/alyx_post_hl2.mdl",
    ]
#SetIncludeModels("alyx_untouched.mdl", "alyx.mdl", alyxModels)
SetIncludeModels("alyx_interior_untouched.mdl", "alyx_interior.mdl", alyxModels)
# """
