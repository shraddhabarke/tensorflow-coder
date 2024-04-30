import json
import matplotlib.pyplot as plt
import numpy as np

with open('tfcoder_results.json', 'r') as file:
    tfcoder_data = json.load(file)

with open('unguided_res.json', 'r') as file:
    unguided = json.load(file)

with open('res_pcfg.json', 'r') as file:
    res1 = json.load(file)

# Extract the times and sort them
tfcoder_times = [result['time'] for result in tfcoder_data['results'] if result['solved']]
unguided_times = [result['time'] for result in unguided['results'] if result['solved']]
res_times = [result['time'] for result in res1['results'] if result['solved']]

# Sorting times to ensure the graph is plotted correctly
sorted_tf_times = sorted(tfcoder_times)
unguided_tf_times = sorted(unguided_times)
fres_times = sorted(res_times)

sorted_tf_times.append(600)
unguided_tf_times.append(600)
fres_times.append(600)

print(sorted_tf_times)
print(unguided_tf_times)
# Generating cumulative counts of problems solved over time
tf_cumulative_counts = np.cumsum([1 for _ in tfcoder_times])
ug_cumulative_counts = np.cumsum([1 for _ in unguided_times])
res_cumulative_counts = np.cumsum([1 for _ in res_times])

tf_cumulative_counts = np.append(tf_cumulative_counts, tf_cumulative_counts[-1])
ug_cumulative_counts = np.append(ug_cumulative_counts, ug_cumulative_counts[-1])
res_cumulative_counts = np.append(res_cumulative_counts, res_cumulative_counts[-1])

plt.figure(figsize=(10, 6))
plt.plot(sorted_tf_times, tf_cumulative_counts, 'b--', linewidth=2, label='TFCoder', markersize=4)
plt.legend(loc='best')

plt.plot(unguided_tf_times, ug_cumulative_counts, 'k--', linewidth=2, label='Unguided', markersize=4)
plt.legend(loc='best')

plt.plot(fres_times, res_cumulative_counts, 'r--', linewidth=2, label='Constants-PCFG', markersize=4)
plt.legend(loc='best')
plt.xlabel('Time (s)')
plt.ylabel('Cumulative Number of Problems Solved')
plt.title('Number of Problems Solved Against Time')
plt.savefig('plot.pdf')