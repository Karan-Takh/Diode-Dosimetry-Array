import nidaqmx
import numpy as np

task = nidaqmx.Task()
task.ai_channels.add_ai_voltage_chan()

task.start()

value = task.read()
print(value)

# Create array with enough spots to be filled by voltages. We know there are 40 rows, but unsure how many columns.
array = np.empty((10000000, 40), dtype=float, like=None)
nidaqmx.stream_readers.AnalogMultiChannelReader.read_many_sample(
    data=array,
    number_of_samples_per_channel=nidaqmx.constants.READ_ALL_AVAILABLE,
    timeout=nidaqmx.constants.WAIT_INFINITELY)






task.stop()
task.close()





# ------------ General Questions: --------------
# Do we have to make 40 tasks, one for each bnc port / diode?
#   - The stream_readers method might let us get all the data without doing that. 
# Where do you specify which channels are being used in the multi channel reader function? 
