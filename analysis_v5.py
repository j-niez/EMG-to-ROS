import neurokit2 as nk
import pandas as pd

# Muscle number to motion code dictionary
musc_dict = {
    1: 3,
    2: 3.1,
    3: 2,
    4: 2.1,
    4.2: 2.2,
    5: 4.1,
    6: 4,
    7: 1,
    8: 1.1
}

# Load data
df = pd.read_csv('Thesis\\moves\\combined_m1.csv')

all_onsets = []
sampling_rate = 2000

for i in range(1, 9):
    # print(i)

    emg = df.iloc[0:len(df), i]
    signals, info = nk.emg_process(emg, sampling_rate=sampling_rate)
    amplitude = signals["EMG_Amplitude"]
    onsets = info["EMG_Onsets"]

    min_interval = 2 * sampling_rate

    filtered_onsets = []
    last_onset = -min_interval

    for onset in onsets:
        if onset - last_onset >= min_interval:
            filtered_onsets.append(onset)
            last_onset = onset

    # print(filtered_onsets)
    
    for o in filtered_onsets:
        if i == 2:
            avg_amp = sum(amplitude[o:1000+o])/100
            if avg_amp > 0.05:
                all_onsets.append([int(o), 4.2])
            else:
                all_onsets.append([int(o), i])
        else:
            all_onsets.append([int(o), i])

# print(all_onsets)

all_onsets.sort(key=lambda x: x[0])
# print(all_onsets)

muscles = [row[1] for row in all_onsets]
#print(muscles)

mov_list = []
for m in muscles:
    mov_list.append(musc_dict[m])

print(mov_list)
