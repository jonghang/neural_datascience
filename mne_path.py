import os
import os.path as op
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class PathHandler(object):
    
    ERP_CORE_DIR = "MNE-ERP-CORE-data"
    BRAINSTORM_DIR = "MNE-brainstorm-data"
    EEGBCI_DIR = "MNE-eegbci-data"
    EEGBCI_DIR = "MNE-eegbci-data"
    FNIRS_MOTOR_DIR = "MNE-fNIRS-motor-data"
    KILOWORD_DIR = "MNE-kiloword-data"
    MISC_DIR = "MNE-misc-data"
    MULTIMODEL_DIR = "MNE-multimodal-data"
    OPM_DIR = "MNE-OPM-data"
    PHANTOM_4DBTI_DIR = "MNE-phantom-4DBTi"
    REFMEG_NOISE_DIR = "MNE-refmeg-noise-data"
    SAMPLE_DIR = "MNE-sample-data"
    SOMATO_DIR = "MNE-somato-data"
    SPMFACE_DIR = "MNE-spm-face"
    TESTING_DIR = "MNE-testing-data"
    MRTF_DIR = "mTRF_1.5"
    SSVEP_EXAMPLE_DIR = "ssvep-example-data"
    
    def __init__(self) -> None:
        self.mne_root = op.join(os.environ["HOME"], "mne_data")
    
    def cddir(self, mne_data_dir):
        gotodir = op.join(self.mne_root, mne_data_dir)
        print("Changed to: ", gotodir)
        return gotodir

def main():
    path_handler = PathHandler()
    print(path_handler.cddir(path_handler.SAMPLE_DIR))

if __name__ == "__main__":
    main()