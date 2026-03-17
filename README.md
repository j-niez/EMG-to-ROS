# EMG-to-ROS
EMG signal processing pipeline and data repo for control of a robotic arm via ROS

Each file is named in the form pAmBtC.csv, where A is the number of the muscle being recorded, see Table X  for those pairings, B is the motion sequence being recorded, and C is the trial number for that particular recording. Thus, the file containing the data for the biceps brachii EMG signal during the fourth sequence would be found in the p7m4t1.csv file. Note that position 10, for the brachioradialis, uses X as the muscle number so the files are properly sorted.

|     Position #    |     Muscle/Muscle Group of Interest                                                                        |     Movement                                         |
|-------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
|     1             |     Flexor carpi radialis \   Flexor carpi ulnaris \ Palmaris longus                                       |     Controls wrist flexion                           |
|     2             |     Extensor carpi radialis   longus \ Extensor carpi radialis brevis \ Extensor carpi radialis brevis     |     Controls wrist   extension                       |
|     3             |     Pronator Teres                                                                                         |     Pronates forearm (turn   palm to face ground)    |
|     4             |     Supinator                                                                                              |     Supinates forearm (turn   palm to face up)       |
|     5             |     Extensor digitorum                                                                                     |     Controls finger   extension                      |
|     6             |     Flexor digitorum   superficialis                                                                       |     Controls finger flexion                          |
|     7             |     Biceps brachii                                                                                         |     Controls elbow flexion                           |
|     8             |     Triceps brachii                                                                                        |     Controls elbow   extension                       |
|     9             |     Brachialis                                                                                             |     Controls elbow flexion                           |
|     10            |     Brachioradialis                                                                                        |     Controls elbow flexion                           |
