import nidaqmx
import numpy as np
from scipy import integrate

task = nidaqmx.Task()
task.ai_channels.add_ai_voltage_chan("Dev1/ai0", "Dev2/ai0", "Dev3/ai0")

task.start()

value = task.read()


# Create array with enough spots to be filled by voltages. We know there are 40 rows, but unsure how many columns.
array = np.empty((15, 3), dtype=float, like=None)
nidaqmx.stream_readers.AnalogMultiChannelReader.read_many_sample(
    data=array,
    number_of_samples_per_channel=15,
    timeout=nidaqmx.constants.WAIT_INFINITELY)

# Create a list of all the channel names, and an empty list of the max voltages and integrated values. 
channels = nidaqmx._task_modules.channel_collection.ChannelCollection.channel_names()
max_volts = list()
int_volts = list()

print("The channels are ", channels)

# Print array to to understand the format of the produced array. 
print("The array is", array)

# Go through each row of array (each diode), and get the max from each column to be added to the list max_volts, and the integrated value of the rows. 
for i in range (0, 40):
    max_volts.append(max(array[i, :]))
    int_volts.append(integrate.simps(array[i, :]))

# Create dictionaries for the associated values for each diode
max_voltdict = dict(zip(channels, max_volts))
int_voltdict = dict(zip(channels, int_volts))

print(max_volts)

task.stop()
task.close()





# ------------ General Questions: --------------
# Do we have to make 40 tasks, one for each bnc port / diode?
#   - The stream_readers method might let us get all the data without doing that. 
# Where do you specify which channels are being used in the multi channel reader function? 
# Unclear to me what the array will look like after the stream readers function goes to work on it. 
