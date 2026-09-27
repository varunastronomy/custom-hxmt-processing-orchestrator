import os
import glob
import subprocess

def find_file(directory, pattern):
    matches = glob.glob(os.path.join(directory, pattern))
    return matches[0] if matches else None

def process_folder(folder):
    base_dir = os.getcwd()
    os.chdir(folder)  # Change into observation folder

    results = {
        'HE_Results': 'HE_Results',
        'ME_Results': 'ME_Results',
        'LE_Results': 'LE_Results'
    }

    # ============ HE Processing ============
    try:
        he_results = results['HE_Results']
        os.chdir(he_results)

        file_patterns = {
            "evt_file": "*HE-Evt_FFFFFF_V1_L1P.FITS",
            "hv_file": "*HE-HV_FFFFFF_V1_L1P.FITS",
            "temp_file": "*HE-TH_FFFFFF_V1_L1P.FITS",
            "ehk_file": "*EHK_FFFFFF_V1_L1P.FITS",
            "dead_file": "*HE-DTime_FFFFFF_V1_L1P.FITS",
            "att_file": "*Att_FFFFFF_V1_L1P.FITS"
        }

        files = {key: find_file(".", pattern) for key, pattern in file_patterns.items()}
        if None in files.values():
            print(f"❌ Missing HE files in {folder}/HE_Results, skipping.")
            os.chdir(base_dir)
            return

        print(f"🚀 Running HE pipeline for {folder}...")
        # subprocess.run(["hepical", f"evtfile={files['evt_file']}", "outfile=he_pi.fits", "evtnum=5", "timedel=0.00008"])
        # subprocess.run(["hegtigen", f"hvfile={files['hv_file']}", f"tempfile={files['temp_file']}", f"ehkfile={files['ehk_file']}", "outfile=he_gti.fits", "defaultexpr=NONE", 'expr=ELV>10&&COR>8&&SAA_FLAG==0&&ANG_DIST<0.04&&T_SAA>300&&TN_SAA>300'])
        # subprocess.run(["hescreen", "evtfile=he_pi.fits", "gtifile=he_gti.fits", "outfile=he_screen.fits", 'userdetid=0-17'])
        # subprocess.run(["helcgen", "evtfile=he_screen.fits", f"deadfile={files['dead_file']}", "outfile=he_lc", 'userdetid=0-15,17', "binsize=1", "minPI=9", "maxPI=59"])
        # subprocess.run(["hespecgen", "evtfile=he_screen.fits", f"deadfile={files['dead_file']}", "outfile=he_spec", 'userdetid=0-15,17'])

        # with open("lcfile.txt", "w") as f:
        #     f.write("he_lc_g0.lc\n")
        # with open("specfile.txt", "w") as f:
        #     f.write("he_spec_g0.pha\n")

        # subprocess.run(["hebkgmap", "lc", "he_screen.fits", files["ehk_file"], "he_gti.fits", files["dead_file"], "lcfile.txt", "9", "59", "he_lc_bkg"])
        subprocess.run(["hebkgmap", "spec", "he_screen.fits", files["ehk_file"], "he_gti.fits", files["dead_file"], "specfile.txt", "0", "255", "he_spec_bkg"])
        # subprocess.run(["herspgen", f"phafile=he_spec_g0.pha", f"attfile={files['att_file']}", "outfile=he_rsp.fits", "ra=-1", "dec=-91"])
        print(f"✅ Completed HE processing for {folder}")
        os.chdir("..")
    except Exception as e:
        print(f"❌ HE processing error in {folder}: {e}")
        os.chdir(base_dir)

    # ============ ME Processing ============
    try:
        os.chdir(results['ME_Results'])

        me_patterns = {
            "me_evt_file": "*ME-Evt_FFFFFF_V1_L1P.FITS",
            "me_temp_file": "*ME-TH_FFFFFF_V1_L1P.FITS",
            "me_ehk_file": "*EHK_FFFFFF_V1_L1P.FITS",
            "me_att_file": "*Att_FFFFFF_V1_L1P.FITS"
        }

        me_files = {key: find_file(".", pattern) for key, pattern in me_patterns.items()}
        if None in me_files.values():
            print(f"❌ Missing ME files in {folder}/ME_Results, skipping.")
            os.chdir(base_dir)
            return

    #     print(f"🚀 Running ME pipeline for {folder}...")
    #     subprocess.run(["mepical", f"evtfile={me_files['me_evt_file']}", f"tempfile={me_files['me_temp_file']}", "outfile=me_pi.fits"])
    #     subprocess.run(["megrade", "evtfile=me_pi.fits", "outfile=me_grade.fits", "deadfile=dead.fits"])
    #     subprocess.run(["megtigen", f"tempfile={me_files['me_temp_file']}", f"ehkfile={me_files['me_ehk_file']}", "outfile=me_gti.fits", 'defaultexpr=NONE', 'expr=ELV>10&&COR>8&&T_SAA>=300&&TN_SAA>=300&&ANG_DIST<=0.04', "clobber=yes"])
    #     subprocess.run(["mescreen", "evtfile=me_grade.fits", "gtifile=me_gti.fits", "outfile=me_screen.fits", 'userdetid=0-53', "clobber=yes"])
    #     subprocess.run(["mespecgen", "evtfile=me_screen.fits", "deadfile=dead.fits", "userdetid=0 1 2 3 4 5 6 7 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 47 48 49 50 51 52 53;10 28 46", "outfile=me_spec"])
    #     subprocess.run(["melcgen", "evtfile=me_screen.fits", "deadfile=dead.fits", "userdetid=0 1 2 3 4 5 6 7 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 47 48 49 50 51 52 53", "outfile=me_lc", "binsize=1"])

    #     with open("lcfile.txt", "w") as f:
    #         f.write("me_lc_g0.lc\n")
    #     with open("specfile.txt", "w") as f:
    #         f.write("me_spec_g0.pha\n")

        subprocess.run(["mebkgmap", "spec", "me_screen.fits", me_files["me_ehk_file"], "me_gti.fits", "dead.fits", me_files["me_temp_file"], "specfile.txt", "0", "1023", "me_spec_bkg"])
    #     subprocess.run(["mebkgmap", "lc", "me_screen.fits", me_files["me_ehk_file"], "me_gti.fits", "dead.fits", me_files["me_temp_file"], "lcfile.txt", "119", "290", "me_lc_bkg"])
    #     subprocess.run(["merspgen", f"phafile=me_spec_g0.pha", f"attfile={me_files['me_att_file']}", "outfile=me_rsp.fits", "ra=-1", "dec=-91"])
        print(f"✅ Completed ME processing for {folder}")
        os.chdir("..")
    except Exception as e:
        print(f"❌ ME processing error in {folder}: {e}")
        os.chdir(base_dir)

    # ============ LE Processing ============
    try:
        os.chdir(results['LE_Results'])

        le_patterns = {
            "le_evt_file": "*LE-Evt_FFFFFF_V1_L1P.FITS",
            "le_temp_file": "*LE-TH_FFFFFF_V1_L1P.FITS",
            "le_ehk_file": "*EHK_FFFFFF_V1_L1P.FITS",
            "le_att_file": "*Att_FFFFFF_V1_L1P.FITS",
            "le_instat_file": "*LE-InsStat_FFFFFF_V1_L1P.FITS"
        }

        le_files = {key: find_file(".", pattern) for key, pattern in le_patterns.items()}
        if None in le_files.values():
            print(f"❌ Missing LE files in {folder}/LE_Results, skipping.")
            os.chdir(base_dir)
            return

    #     print(f"🚀 Running LE pipeline for {folder}...")
    #     subprocess.run(["lepical", f"evtfile={le_files['le_evt_file']}", f"tempfile={le_files['le_temp_file']}", "outfile=le_pi.fits"], check=True)
    #     subprocess.run(["lerecon", "evtfile=le_pi.fits", f"instatusfile={le_files['le_instat_file']}", "outfile=le_recon.fits"], check=True)
    #     subprocess.run(["legtigen", "defaultexpr=NONE", 'expr=ELV>10&&DYE_ELV>30&&COR>8&&ANG_DIST<0.04&&SAA_FLAG==0&&T_SAA>300&&TN_SAA>300', "evtfile=NONE", f"instatusfile={le_files['le_instat_file']}", f"tempfile={le_files['le_temp_file']}", f"ehkfile={le_files['le_ehk_file']}", "outfile=le_gti.fits"], check=True)
    #     subprocess.run(["lescreen", "evtfile=le_recon.fits", "gtifile=le_gti.fits", 'userdetid=0-95', "eventtype=1", "outfile=le_screen.fits"], check=True)
    #     subprocess.run(["lespecgen", "evtfile=le_screen.fits", 'userdetid=0 2-4 6-10 12 14 20 22-26 28-30 32 34-36 38-42 44 46 52 54-58 60-62 64 66-68 70-74 76 78 84 86-90 92-94', "outfile=le_spec", "eventtype=1"], check=True)
    #     subprocess.run(["lelcgen", "evtfile=le_screen.fits", "outfile=le_lc", "binsize=1", 'userdetid=0 2-4 6-10 12 14 20 22-26 28-30 32 34-36 38-42 44 46 52 54-58 60-62 64 66-68 70-74 76 78 84 86-90 92-94', "eventtype=1", "clobber=yes"], check=True)

    #     with open("lcfile.txt", "w") as f:
    #         f.write("le_lc_g0.lc\n")
    #     with open("specfile.txt", "w") as f:
    #         f.write("le_spec_g0.pha\n")

        subprocess.run(["lebkgmap", "spec", "le_screen.fits", "le_gti.fits", "specfile.txt", "0", "1535", "le_spec_bkg"], check=True)
    #     subprocess.run(["lebkgmap", "lc", "le_screen.fits", "le_gti.fits", "lcfile.txt", "106", "1069", "le_lc_bkg"], check=True)
    #     subprocess.run(["lerspgen", f"phafile=le_spec_g0.pha", f"temp={le_files['le_temp_file']}", f"attfile={le_files['le_att_file']}", "outfile=le_rsp.fits", "ra=-1", "dec=-91"], check=True)
        print(f"✅ Completed LE processing for {folder}")
        os.chdir("..")
    except subprocess.CalledProcessError as e:
        print(f"❌ LE processing error in {folder}: {e}")
        os.chdir(base_dir)

    os.chdir(base_dir)

def main():
    cwd = os.getcwd()
    for folder in os.listdir(cwd):
        if os.path.isdir(folder) and folder.startswith("P"):
            process_folder(folder)

if __name__ == "__main__":
    main()
