import matplotlib.pyplot as plt
import mne
from mne.io import read_raw_edf


def read_data(file_path: str) -> mne.io.BaseRaw:
    """Read EEG data from an EEGLAB .set file.

    Parameters:
    - file_path (str): Path to the .set EEG file.

    Returns:
    - mne.io.BaseRaw: Raw EEG data loaded into an MNE object.
    """
    # Read the EEG data
    read_eeg = read_raw_edf(file_path, preload=True)
    return read_eeg


def visualise_raw_data(raw_eeg):
    """Visualize EEG data with a band-pass filter from 0.5-45 Hz."""
    raw_eeg.plot()
    plt.show()


visualise_raw_data(
    read_data(
        "/Users/noam/Downloads/23.1.25 - Lying on back/muscle_1_23_01_25_retest_RecordingFile_EYEC_Jan_23_2025.edf"
    )
)

def visualize_annotated_epochs(file_path, tmin=-0.2, tmax=0.8, baseline=(None, 0)):
    """
    Load an EDF file, extract annotated epochs, and visualize them.
    
    Parameters:
    - file_path (str): Path to the EDF file.
    - tmin (float): Start time before the event (in seconds).
    - tmax (float): End time after the event (in seconds).
    - baseline (tuple or None): Baseline correction interval (start, end in seconds). Use None for no baseline correction.
    
    Returns:
    - epochs (mne.Epochs): The created epochs object.
    """
    # Load the raw EDF file
    raw = mne.io.read_raw_edf(file_path, preload=True)
    
    # Extract events and event IDs from annotations
    events, event_id = mne.events_from_annotations(raw)
    
    # Create epochs based on events
    epochs = mne.Epochs(raw, events, event_id, tmin=tmin, tmax=tmax, baseline=baseline, preload=True)
    
    # Visualize the epochs
    epochs.plot()
    
    return epochs

# Example usage:
epochs = visualize_annotated_epochs("'/Users/noam/Downloads/23.1.25 - Lying on back/muscle_3_23_01_25_retest_RecordingFile_EYEC_Jan_23_2025.edf'")
