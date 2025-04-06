import matplotlib.pyplot as plt
import mido
import os
import numpy as np

# Path to the ESAC dataset (replace with the actual path to MIDI files)
midi_directory = r"C:\Users\LENOVO\OneDrive\Desktop\Internship-Project\DataProcessing\dataset"

# Function to extract the number of notes in each MIDI file
'''def get_midi_song_length(midi_file):
    midi = mido.MidiFile(midi_file)
    note_count = 0
    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on':  # Counting "note_on" messages as notes
                note_count += 1
    return note_count

# Extract note counts for all MIDI files
note_counts = []
for file in os.listdir(midi_directory):
    if file.endswith('.mid'):
        note_counts.append(get_midi_song_length(os.path.join(midi_directory, file)))

# Plot the distribution of song lengths
plt.figure(figsize=(10, 6))
plt.hist(note_counts, bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of Song Lengths (in Notes) in ESAC Dataset')
plt.xlabel('Number of Notes')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()'''

# Function to extract note pitches from a MIDI file
'''def get_midi_note_pitches(midi_file):
    midi = mido.MidiFile(midi_file)
    note_pitches = []
    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on':  # "note_on" messages indicate note events
                note_pitches.append(msg.note)  # MIDI note value (0-127)
    return note_pitches

# Collect pitches for all songs
all_pitches = []
for file in os.listdir(midi_directory):
    if file.endswith('.mid'):
        all_pitches.extend(get_midi_note_pitches(os.path.join(midi_directory, file)))

# Plot the pitch distribution
plt.figure(figsize=(10, 6))
plt.hist(all_pitches, bins=np.arange(0, 128, 1), color='salmon', edgecolor='black')
plt.title('Pitch Distribution (MIDI Note Numbers) in ESAC Dataset')
plt.xlabel('MIDI Note Number')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()'''

'''import mido

# Function to extract note durations from a MIDI file
def get_midi_note_durations(midi_file):
    midi = mido.MidiFile(midi_file)
    note_durations = []
    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on':  # On note events
                start_time = msg.time  # When the note starts
                for next_msg in track:
                    if next_msg.type == 'note_off' and next_msg.note == msg.note:
                        note_durations.append(next_msg.time - start_time)  # Duration
                        break
    return note_durations

# Collect note durations for all songs
durations = []
for file in os.listdir(midi_directory):
    if file.endswith('.mid'):
        durations.extend(get_midi_note_durations(os.path.join(midi_directory, file)))

# Plot the distribution of note durations
plt.figure(figsize=(10, 6))
plt.hist(durations, bins=50, color='lightgreen', edgecolor='black')
plt.title('Distribution of Note Durations in ESAC Dataset')
plt.xlabel('Duration (Ticks)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()'''


'''import matplotlib.pyplot as plt

# Example genres (this should be read from your dataset if available)
genres = ['European', 'Asian', 'African', 'Latin', 'Other']  # Example genres
genre_counts = [120, 90, 60, 50, 80]  # Example counts (replace with actual data)

# Plot genre distribution
plt.figure(figsize=(10, 6))
plt.bar(genres, genre_counts, color='purple')
plt.title('Genre Distribution in ESAC Dataset')
plt.xlabel('Genre')
plt.ylabel('Number of Songs')
plt.show()'''

'''import matplotlib.pyplot as plt
import seaborn as sns

# Collect pitch and duration pairs
pitch_duration_pairs = []
for file in os.listdir(midi_directory):
    if file.endswith('.mid'):
        midi = mido.MidiFile(os.path.join(midi_directory, file))
        for track in midi.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    start_time = msg.time
                    for next_msg in track:
                        if next_msg.type == 'note_off' and next_msg.note == msg.note:
                            duration = next_msg.time - start_time
                            pitch_duration_pairs.append((msg.note, duration))
                            break

# Convert to DataFrame for easier plotting
import pandas as pd
df = pd.DataFrame(pitch_duration_pairs, columns=['Pitch', 'Duration'])

# Plot Pitch vs Duration
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Pitch', y='Duration', alpha=0.6)
plt.title('Pitch vs. Duration (MIDI) in ESAC Dataset')
plt.xlabel('Pitch (MIDI Note Number)')
plt.ylabel('Duration (Ticks)')
plt.show()'''

'''import matplotlib.pyplot as plt
import numpy as np
import os
import mido

# Function to get the number of notes in a MIDI file
def get_midi_song_length(midi_file):
    midi = mido.MidiFile(midi_file)
    note_count = 0
    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on':  # Counting "note_on" messages as notes
                note_count += 1
    return note_count

# Directory containing MIDI files
#midi_directory = '/path/to/your/midi/files'

# Extract note counts for all MIDI files
note_counts = []
for file in os.listdir(midi_directory):
    if file.endswith('.mid'):
        note_counts.append(get_midi_song_length(os.path.join(midi_directory, file)))

# Plot with a colormap for the bars
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(note_counts, bins=50, edgecolor='black')

# Apply colormap to each patch (bar)
for i in range(len(patches)):
    color = plt.cm.viridis(i / len(patches))  # Get a color from the 'viridis' colormap
    patches[i].set_facecolor(color)

plt.title('Distribution of Song Lengths (in Notes) in ESAC Dataset', fontsize=14)
plt.xlabel('Number of Notes', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()'''


import matplotlib.pyplot as plt
import mido
import numpy as np

# Function to extract note pitches from a MIDI file
def get_midi_note_pitches(midi_file):
    midi = mido.MidiFile(midi_file)
    note_pitches = []
    for track in midi.tracks:
        for msg in track:
            if msg.type == 'note_on':  # "note_on" messages indicate note events
                note_pitches.append(msg.note)  # MIDI note value (0-127)
    return note_pitches

# Collect pitches for all songs
all_pitches = []
for file in os.listdir(midi_directory):
    if file.endswith('.mid'):
        all_pitches.extend(get_midi_note_pitches(os.path.join(midi_directory, file)))

# Create the colorful bar plot
plt.figure(figsize=(12, 6))
plt.hist(all_pitches, bins=np.arange(0, 128, 1), color=plt.cm.plasma(np.linspace(0, 1, 128)), edgecolor='black')
plt.title('Pitch Distribution (MIDI Note Numbers) in ESAC Dataset', fontsize=14)
plt.xlabel('MIDI Note Number', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()




