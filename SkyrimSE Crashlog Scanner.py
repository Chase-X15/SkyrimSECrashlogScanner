# Created By: Chase
# Date Created: 9/9/2022
# Checks directory for Skyrim SE Crash Logs and scans them for potential culprits
# Version: 1.3
# Last Edited: 9/15/2022

import os
import sys
import time
import fnmatch

# Happy little window
print("Crashlog Scanner - Ver 1.3 - Made By Chase")
print("------------------------------")
print("CRASHLOGS MUST BE NAMED crash-[date].log AND IN THE SAME FOLDER AS THIS SCRIPT")
print("------------------------------")
print("BEGINNING SCAN...")

longStartTime = time.time()
originalPrompt = sys.stdout

# Finding the Files
for file in os.listdir("."):
    if fnmatch.fnmatch(file, "crash-*.log"):
        strLogName = str(file)[:len(str(file))-4]
        sys.stdout = open(strLogName + "-SCANNED.md", "w", errors="ignore")
        strLogFile = str(strLogName + str(".log"))

        print(strLogName + ".log")
        print("------------------------------")

        # Open the file
        strCrashLog = open(strLogFile, "r", errors="ignore")

        strAllLines = strCrashLog.readlines()
        strMainError = str(strAllLines[3].strip())
        
        print("MAIN ERROR: ", strMainError)
        print("------------------------------")

        # Start at the beginning of the file and read everything
        strCrashLog.seek(0)
        strLogContents = strCrashLog.read()

        # Possibly relevant callout
        if ".dll" in strMainError and "tbbmalloc" not in strMainError:
            print("------------------------------")
            print("MAIN ERROR REPORTS A DLL WAS INVLOVED IN THIS CRASH!")
            print("------------------------------")
        if "KERNELBASE.dll+004474C" in strMainError:
            print("------------------------------")
            print("MAIN ERROR REPORTS POSSIBLE DECIMAL SEPARATOR CRASH!")
            print("------------------------------")
        if "tbbmalloc.dll+00196EB" in strMainError:
            print("------------------------------")
            print("MAIN ERROR REPORTS POSSIBLE FACE OVERLAY CRASH!")
            print("------------------------------")
        if "SkyrimSE.exe+0A" in strMainError:
            print("------------------------------")
            print("MAIN ERROR REPORTS POSSIBLE ANIMATION CRASH!")
            print("------------------------------")
        if "D6DDDA" in strMainError:
            print("------------------------------")
            print("MAIN ERROR REPORTS POSSIBLE MEMORY CRASH!")
            print("------------------------------")
        if "12F5590" in strMainError:
            print("------------------------------")
            print("MAIN ERROR REPORTS POSSIBLE FACEGEN CRASH!")
            print("------------------------------")
        if "132BEF" in strMainError:
            print("------------------------------")
            print("MAIN ERROR REPORTS POSSIBLE HEAD MESH CRASH!")
            print("------------------------------")
        if "8BDA97" in strMainError:
            print("------------------------------")
            print("MAIN ERROR REPORTS POSSIBLE ENGINE FIXES/DISPLAY TWEAKS OVERLAP CRASH!")
            print("------------------------------")
        if "5E1F22" in strMainError:
            print("------------------------------")
            print("MAIN ERROR REPORTS POSSIBLE MISSING MASTER CRASH!")
            print("------------------------------")


        print("------------------------------")

        # Count Everything
        # Overflow
        intOverflow = strLogContents.count("EXCEPTION_STACK_OVERFLOW")
        if int(intOverflow) >= int(1):
            print("Found Overflow Callout!")
            print("Priority Level: HIGH")
            print("------------------------------")
        # Active Effect
        intActiveEffect = strLogContents.count("0x000100000000")
        if int(intActiveEffect) >= int(1):
            print("Found Active Effect Callout!")
            print("Priority Level: HIGH")
            print("------------------------------")
        # Bad Math
        intBadMath = strLogContents.count("EXCEPTION_INT_DIVIDE_BY_ZERO")
        if int(intBadMath) >= int(1):
            print("Found Bad Math Callout!")
            print("Priority Level: HIGH")
            print("------------------------------")
        # Null
        intNULL = strLogContents.count("0x000000000000")
        if int(intNULL) >= int(1):
            print("Found NULL Callout!")
            print("Priority Level: HIGH")
            print("------------------------------")
        # CBP
        intCBP = strLogContents.count("cbp.dll")
        intSketelon = strLogContents.count("skeleton.nif")
        intXPMSEWeaponStyleScaleEffect = strLogContents.count("XPMSEWeaponStyleScaleEffect")
        if int(intCBP) >= int(3) or int(intSketelon) >= int(1) or int(intXPMSEWeaponStyleScaleEffect) >= int(1) or str("cbp") in strMainError:
            print("Found Body Physics Callout!")
            print("Priority Level: HIGH")
            print("Count of cbp.dll : ",intCBP) 
            print("Count of skeleton.nif : ",intSketelon) 
            print("Count of XPMSEWeaponStyleScaleEffect : ",intXPMSEWeaponStyleScaleEffect)
            print("------------------------------")
        # LOD
        intBGSLocation = strLogContents.count("BGSLocation")
        intBGSQueued = strLogContents.count("BGSQueuedTerrainInitialLoad")
        if (int(intBGSLocation) and int(intBGSQueued)) >= int(1):
            print("Found LOD Callout!")
            print("Priority Level: HIGH")
            print("Count of BGSLocation : ",intBGSLocation)
            print("Count of BGSQueuedTerrainInitialLoad : ",intBGSQueued)
            print("------------------------------")
        # Script
        intPapyrus = strLogContents.count("Papyrus")
        intVirtualMachine = strLogContents.count("VirtualMachine")
        if (int(intPapyrus) or int(intVirtualMachine)) >= int(2):
            print("Found Script Callout!")
            print("Priority Level: MEDIUM")
            print("Count of Papyrus : ",intPapyrus)
            print("Count of VirtualMachine : ",intVirtualMachine)
            print("------------------------------")
        # Generic
        intGeneric = strLogContents.count("tbbmalloc.dll")
        if int(intGeneric) >= int(3) or str("tbbmalloc") in strMainError:
            print("Found Generic Callout!")
            print("Priority Level: LOW")
            print("Detected number of tbbmalloc.dll : ",intGeneric)
            print("------------------------------")
        # Rendering
        intRender = strLogContents.count("d3d11.dll")
        if int(intRender) >= int(3):
            print("Found Rendering Callout!")
            print("Priority Level: HIGH")
            print("Detected number of d3d11.dll : ",intRender)
            print("------------------------------")
        # Mesh (NIF)
        intLooseFileStream = strLogContents.count("LooseFileStream")
        intBSMulti = strLogContents.count("BSMultiBoundNode")
        intBSFade = strLogContents.count("BSFadeNode")
        intBSFaceGenNiNode = strLogContents.count("BSFaceGenNiNode")
        if (int(intLooseFileStream) or int(intBSFade) or int(intBSMulti) or int(intBSFaceGenNiNode)) >= int(1) and int(intLooseFileAsync) == int(0):
            print("Found Mesh (NIF) Callout!")
            print("Priority Level: HIGH")
            print("Count of LooseFileStream : ",intLooseFileStream)
            print("Count of BSFadeNode : ",intBSFade)
            print("Count of BSMultiBoundNode : ",intBSMulti)
            print("Count of BSFaceGenNiNode : ",intBSFaceGenNiNode)
            print("------------------------------")
        # Texture (DDS)
        intCreature2DTexture = strLogContents.count("Create2DTexture")
        intDefaultTexture = strLogContents.count("DefaultTexture")
        if (int(intCreature2DTexture) or int(intDefaultTexture)) >= int(1):
            print("Found Texture (DDS) Callout!")
            print("Priority Level: MEDIUM")
            print("Count of Create2DTexture : ",intCreature2DTexture)
            print("Count of DefaultTexture : ",intDefaultTexture)
            print("------------------------------")
        # Material (BGSM)
        intTextureBlack = strLogContents.count("DefaultTexture_Black")
        intNiAlphaProperty = strLogContents.count("NiAlphaProperty")
        if int(intTextureBlack) or int(intNiAlphaProperty) >= int(1):
            print("Found Material (BGSM) Callout!")
            print("Priority Level: MEDIUM")
            print("Count of DefaultTexture_Black : ",intTextureBlack)
            print("Count of NiAlphaProperty : ",intNiAlphaProperty)
            print("------------------------------")
        # Light / Camera
        intShadowSceneNode = strLogContents.count("ShadowSceneNode")
        intNiCamera = strLogContents.count("NiCamera")
        if int(intShadowSceneNode) or int(intNiCamera) >= int(1):
            print("Found Light/Camera Callout!")
            print("Priority Level: MEDIUM")
            print("Count of ShadowSceneNode : ",intShadowSceneNode)
            print("Count of NiCamera : ",intNiCamera)
            print("------------------------------")
        # BitDefender
        intBitDefender = strLogContents.count("bdhkm64.dll")
        intDeleteFileW = strLogContents.count("usvfs::hook_DeleteFileW")
        if (int(intBitDefender) or int(intDeleteFileW)) >= int(2):
            print("Found BitDefender Callout!")
            print("Priority Level: HIGH")
            print("Count of bdhkm64.dll : ",intBitDefender)
            print("Count of usvfs::hook_DeleteFileW : ",intDeleteFileW)
            print("------------------------------")
        # Audio Driver
        intX3DAudio = strLogContents.count("X3DAudio1_7.dll")
        intXAudio = strLogContents.count("XAudio2_7.dll")
        if int(intX3DAudio) >= int(3) or int(intXAudio) >= int(2) or str("X3DAudio1_7") in strMainError or str("XAudio2_7") in strMainError:
            print("Found Audio Driver Callout!")
            print("Priority Level: HIGH")
            print("Count of X3DAudio1_7.dll : ",intX3DAudio)
            print("Count of XAudio2_7.dll : ",intXAudio)
            print("------------------------------")
        # Plugin Limit
        intObjectBindPolicy = strLogContents.count("ObjectBindPolicy")
        intBSMemStorage = strLogContents.count("BSMemStorage")
        intReaderWriter = strLogContents.count("DataFileHandleReaderWriter")
        if int(intObjectBindPolicy) or int(intBSMemStorage) or int(intReaderWriter) >= int(1):
            print("Found Plugin Limit Callout!")
            print("Priority Level: HIGH")
            print("Count of ObjectBindPolicy : ",intObjectBindPolicy)
            print("Count of BSMemStorage : ",intBSMemStorage)
            print("Count of DataFileHandleReaderWriter : ",intReaderWriter)
            print("------------------------------")
        # Plugin Order
        intGamebryo = strLogContents.count("GamebryoSequenceGenerator")
        if int(intGamebryo) >= int(1):
            print("Found Plugin Order Callout!")
            print("Priority Level: HIGH")
            print("Count of GamebryoSequenceGenerator : ",intGamebryo)
            print("------------------------------")
        # Nvidia Debris
        intNvidiaFlexRelease = strLogContents.count("flexRelease_x64.dll")
        if int(intNvidiaFlexRelease) >= int(2) or str("flexRelease_x64") in strMainError:
            print("Found NVidia Debris Callout!")
            print("Priority Level: HIGH")
            print("Count of flexRelease_x64.dll : ",intNvidiaFlexRelease)
            print("------------------------------")
        # Nvidia Driver
        intNvidiaDriver = strLogContents.count("nvwgf2umx.dll")
        if int(intNvidiaDriver) >= int(10) or str("nvwgf2umx") in strMainError:
            print("Found NVidia Driver Callout!")
            print("Priority Level: HIGH")
            print("Count of nvwgf2umx.dll : ",intNvidiaDriver)
            print("------------------------------")
        # Vulkan Memory
        intKERNALBASE = strLogContents.count("KERNELBASE.dll")
        intMSVCP140 = strLogContents.count("MSVCP140.dll")
        intSubmissionQueue = strLogContents.count("DxvkSubmissionQueue")
        if (int(intKERNALBASE) or int(intMSVCP140)) >= int(3) and int(intSubmissionQueue) >= int(1):
            print("Found Vulkan Memory Callout!")
            print("Priority Level: HIGH")
            print("Count of KERNELBASE.dll : ",intKERNALBASE)
            print("Count of MSVCP140.dll : ",intMSVCP140)
            print("Count of DxvkSubmissionQueue : ",intSubmissionQueue)
            print("------------------------------")
        # Vulkan Settings
        intDxgiAdapter  = strLogContents.count("dxvk::DxgiAdapter")
        intDxgiFactory  = strLogContents.count("dxvk::DxgiFactory")
        if (int(intDxgiAdapter) or int(intDxgiFactory)) >= int(1):
            print("Found Vulkan Settings Callout!")
            print("Priority Level: HIGH")
            print("Count of dxvk::DxgiAdapter : ",intDxgiAdapter)
            print("Count of dxvk::DxgiFactory : ",intDxgiFactory)
            print("------------------------------")
        # Corrupted Audio
        intBSXAudio2DataSrc =  strLogContents.count("BSXAudio2DataSrc")
        intBSXAudio2GameSound =  strLogContents.count("BSXAudio2GameSound")
        if (int(intBSXAudio2DataSrc) or int(intBSXAudio2GameSound)) >= int(1):
            print("Found Corrupted Audio Callout!")
            print("Priority Level: HIGH")
            print("Count of BSXAudio2DataSrc : ",intBSXAudio2DataSrc)
            print("Count of BSXAudio2GameSound : ",intBSXAudio2GameSound)
            print("------------------------------")
        # Animation / Physics
        intHKBVariableBinding = strLogContents.count("hkbVariableBindingSet")
        intHKBHandIkControls = strLogContents.count("hkbHandIkControlsModifier")
        intHKBBehaviorGraph = strLogContents.count("hkbBehaviorGraph")
        intHKBModifierList = strLogContents.count("hkbModifierList")
        intHKBClipGenerator = strLogContents.count("hkbClipGenerator")
        intHKADefaultAnimationControl = strLogContents.count("hkaDefaultAnimationControl")
        intBSHKBAnimationGraph = strLogContents.count("BShkbAnimationGraph")
        intBSAnimationGraphManager = strLogContents.count("BSAnimationGraphManager")
        intAnimationGraphManagerHolder = strLogContents.count("AnimationGraphManagerHolder")
        if int(intHKBVariableBinding) or int(intHKBHandIkControls) or int(intHKBBehaviorGraph) or int(intHKBModifierList) or int(intHKBClipGenerator) or int(intHKADefaultAnimationControl) or int(intBSHKBAnimationGraph) or int(intBSAnimationGraphManager) or int(intAnimationGraphManagerHolder) >= int(1):
            print("Found Animation/Physics Callout!")
            print("Priority Level: HIGH")
            print("Count of hkbVariableBindingSet : ",intHKBVariableBinding)
            print("Count of hkbHandIkControlsModifier : ",intHKBHandIkControls)
            print("Count of hkbBehaviorGraph : ",intHKBBehaviorGraph)
            print("Count of hkbModifierList : ",intHKBModifierList)
            print("Count of hkbClipGenerator : ",intHKBClipGenerator)
            print("Count of hkaDefaultAnimationControl : ",intHKADefaultAnimationControl)
            print("Count of bshkbAnimationGraph : ",intBSHKBAnimationGraph)
            print("Count of bsAnimationGraphManager : ",intBSAnimationGraphManager)
            print("Count of AnimationGraphManagerHolder : ",intAnimationGraphManagerHolder)
            print("------------------------------")
        # Particle
        intParticleSystem = strLogContents.count("ParticleSystem")
        intNiParticleSystem = strLogContents.count("NiParticleSystem")
        if int(intParticleSystem) or int(intNiParticleSystem) >= int(1):
            print("Found Particle System Callout!")
            print("Priority Level: HIGH")
            print("Count of ParticleSystem : ",intParticleSystem)
            print("Count of NiParticleSystem : ",intNiParticleSystem)
            print("------------------------------")
        # BA2 Limit
        intLooseFileAsync = strLogContents.count("LooseFileAsyncStream")
        if int(intLooseFileAsync) >= int(1):
            print("Found BA2 Callout!")
            print("Priority Level: HIGH")
            print("Count of LooseFileAsyncStream : ",intLooseFileAsync)
            print("------------------------------")
        # MCM
        intFaderData = strLogContents.count("FaderData")
        intFaderMenu = strLogContents.count("FaderMenu")
        intUIMessage = strLogContents.count("UIMessage")
        if (int(intFaderData) or int(intFaderMenu) or int(intUIMessage)) >= int(1):
            print("Found MCM Callout!")
            print("Priority Level: MEDIUM")
            print("Count of FaderData : ",intFaderData)
            print("Count of FaderMenu : ",intFaderMenu)
            print("Count of UIMessage : ",intUIMessage)
            print("------------------------------")
        # Decal
        intBGSDecal = strLogContents.count("BGSDecalManager")
        intBSTempEffect = strLogContents.count("BSTempEffectGeometryDecal")
        if (int(intBGSDecal) or int(intBSTempEffect)) >= int(1):
            print("Found Decal Callout!")
            print("Priority Level: HIGH")
            print("Count of BGSDecalManager : ",intBGSDecal)
            print("Count of BSTempEffectGeometryDecal : ",intBSTempEffect)
            print("------------------------------")
        # Console
        intCompileAndRun = strLogContents.count("SysWindowCompileAndRun")
        intNiBinaryStream = strLogContents.count("BSResourceNiBinaryStream")
        intConsoleLogPrinter = strLogContents.count("ConsoleLogPrinter")
        if int(intCompileAndRun) or int(intNiBinaryStream) or int(intConsoleLogPrinter) >= int(1):
            print("Found Console Command Callout!")
            print("Priority Level: LOW")
            print("Count of SysWindowCompileAndRun : ",intCompileAndRun)
            print("Count of BSResourceNiBinaryStream : ",intNiBinaryStream)
            print("Count of ConsoleLogPrinter : ",intConsoleLogPrinter)
            print("------------------------------")
        # Pathing
        intPathingCell = strLogContents.count("PathingCell")
        intBSPathBuilder = strLogContents.count("BSPathBuilder")
        intPathManager = strLogContents.count("PathManagerServer") 
        intBGSProcedureFollowExecState = strLogContents.count("BGSProcedureFollowExecState") # not sure if this is pathing
        if int(intPathingCell) or int(intBSPathBuilder) or int(intPathManager) or int(intBGSProcedureFollowExecState) >= int(1):
            print("Found NPC Pathing Callout!")
            print("Priority Level: MEDIUM")
            print("Count of PathingCell : ",intPathingCell)
            print("Count of BSPathBuilder : ",intBSPathBuilder)
            print("Count of PathManagerServer : ",intPathManager)
            print("Count of BGSProcedureFollowExecState : ",intBGSProcedureFollowExecState)
            print("------------------------------")
        # NPC
        intTESNPC = strLogContents.count("TESNPC")
        if int(intTESNPC) >= int(1):
            print("Found NPC Callout!")
            print("Priority Level: MEDIUM")
            print("Count of TESNPC : ",intTESNPC)
            print("------------------------------")
        # Grid Scrap
        intGridAdjacency = strLogContents.count("GridAdjacencyMapNode")
        intPowerUtils = strLogContents.count("PowerUtils")
        if int(intGridAdjacency) or int(intPowerUtils) >= int(1):
            print("Found GridScrap Callout!")
            print("Priority Level: HIGH")
            print("Count of GridAdjacencyMapNode : ",intGridAdjacency)
            print("Count of PowerUtils : ",intPowerUtils)
            print("------------------------------")
        # Leveled List
        intLevelList = strLogContents.count ("TESLevItem")
        if int(intLevelList) >= int(1):
            print("Found Leveled List Callout!")
            print("Priority Level: MEDIUM")
            print("Count of TESLevItem : ",intLevelList)
            print("------------------------------")
        # Save
        intBGSSaveForm = strLogContents.count("BGSSaveFormBuffer")
        if int(intBGSSaveForm) >= int(2):
            print("Found SAVE CRASH Callout!")
            print("Priority Level: UNKNOWN")
            print("Count of BGSSaveFormBuffer : ",intBGSSaveForm)
            print("------------------------------")
        # Player Character
        intPlayerCharacter = strLogContents.count("PlayerCharacter")
        int0x7 = strLogContents.count("0x00000007")
        int0x8 = strLogContents.count("0x00000008")
        int0x14 = strLogContents.count("0x00000014")
        if (int(intPlayerCharacter) and int(int0x7)) >= int(2) and (int(int0x14) or int(int0x8)) >= int(2):
            print("Found PLAYER CHARACTER Callout!")
            print("Priority Level: UNKNOWN")
            print("Count of PlayerCharacter : ",intPlayerCharacter)
            print("Count of 0x00000007 : ",int0x7)
            print("Count of 0x00000008 : ",int0x8)
            print("Count of 0x000000014 : ",int0x14)
            print("------------------------------")
        
        # Create arrays
        arrPlugins = []
        arrFormIDs = []
        arrFiles = []
        arrAllPlugins = []

        intSKSE = strLogContents.count("skse64_1_6_353.dll")
        intSteamAPI = strLogContents.count("steam_api64.dll")

        if int(intSKSE) == int(0) and int(intSteamAPI) >= int(1):
            print("Could not find SKSE DLL!")
            print("------------------------------")
            
        for line in strAllLines:
            if len(line) >= 6 and "]" in line[4]:
                arrAllPlugins.append(line.strip())
            if len(line) >= 7 and "]" in line[5]:
                arrAllPlugins.append(line.strip())
            if len(line) >= 10 and "]" in line[8]:
                arrAllPlugins.append(line.strip())
            if len(line) >= 11 and "]" in line[9]:
                arrAllPlugins.append(line.strip())

        # Specific callouts
        print("POSSIBLE PLUGIN CULPRITS:")
        for line in strAllLines:
          if "File:" in line:
            line = line.replace("File: ", "") 
            line = line.replace('"', '') 
            arrPlugins.append(line.strip())

        arrPlugins = list(dict.fromkeys(arrPlugins))
        arrRemove = ["Skyrim.esm", "Update.esm", "Dawnguard.esm", "HearthFires.esm", "Dragonborn.esm", "", '']
        for elem in arrRemove:
            if elem in arrPlugins:
                arrPlugins.remove(elem)
                
        arrPluginStrings = arrAllPlugins
        arrPluginSubstrings = arrPlugins
        arrPluginResults = []

        for string in arrPluginStrings:
            arrPluginMatches = []
            for substring in arrPluginSubstrings:
                if substring in string:
                    arrPluginMatches.append(string)
            if arrPluginMatches:
                arrPluginResults.append(arrPluginMatches)
                print("- " + ' '.join(arrPluginMatches))

        if not arrPlugins:
            print("No culprits found")

        print("------------------------------")
        print("POSSIBLE FORM ID CULPRITS:")
        for line in strAllLines:
          if "Form ID:" in line:
            line = line.replace("0x", "")
            arrFormIDs.append(line.strip())
            line = line.replace("Form ID: ", "")
            line = line[:5].strip()

        arrFormIDs = list(dict.fromkeys(arrFormIDs))
        for elem in arrFormIDs:
            print(elem)
        
        if not arrFormIDs:
            print("No culprits found")

        print("------------------------------")
        print("POSSIBLE FILE CULPRITS:")
        for line in strAllLines:
            if ".NIF" in line or ".nif" in line or ".BGSM" in line or ".bgsm" in line or ".DDS" in line or ".dds" in line or ".SWF" in line or ".swf" in line or ".cpp" in line or ".tri" in line:
                line = line.replace("File Name: ", "") 
                line = line.replace("Name: ", "") 
                line = line.replace('"', '')
                arrFiles.append(line.strip())

        arrFiles = list(dict.fromkeys(arrFiles))
        for elem in arrFiles:
            print(elem)
        
        if not arrFiles:
            print("No culprits found")

        print("------------------------------")
        print("------------------------------")
        print("ORIGINAL LOG BELOW")
        print("------------------------------")
        print("------------------------------")

        for line in strAllLines:
            print(line.strip())

        # Close everything
        strCrashLog.close()
        sys.stdout.close()

sys.stdout = originalPrompt

print("SCAN COMPLETE...")
print("Time taken: ", (str(time.time() - longStartTime)[:7]), " seconds")
print("------------------------------")

# Check if a scan failed
arrFailedScans = []
for file in os.listdir("."): 
    if fnmatch.fnmatch(file, "*-SCANNED.md"):
        intLineCount = 0
        strScanName = str(file)
        strScanFile = open(file, errors="ignore")
        for line in strScanFile:
            if line != "\n":
                intLineCount += 1
        if int(intLineCount) <= int(10):
            arrFailedScans.append(strScanName.removesuffix("-SCANNED.md") + "-FAILED.log")

if len(arrFailedScans) >= 1:
    print("UNABLE TO SCAN FOLLOWING LOGS: ")
    for elem in arrFailedScans:
        print(elem)

sys.stdout.close()