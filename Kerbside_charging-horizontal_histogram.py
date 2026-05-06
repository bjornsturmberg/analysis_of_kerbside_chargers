import matplotlib.pyplot as plt
import numpy as np

# Data from zenodo.org/records/19233669
AC = np.array([22.19836401, 18.64199735, 16.37609649, 15.44304654, 15.04038137,14.98888889,
      14.37911959,13.2125947,13.16029457,12.13045635, 11.9346174,11.83142245,
      11.4837963,11.41226398,10.65022275,10.2611715,10.26056505,9.912992571,
      9.51778297,9.50547138,9.226549919,8.981829574,8.947285354,8.536616162,
      8.329903978,7.783564815,7.65491453,7.432336182,7.27590812,7.10515873,
      6.602704678, 6.350308642, 4.254070881])
DC = np.array([41.32038798, 27.07802064, 17.78412698, 17.37847222, 16.24553849, 15.96197632, 
      15.41514042, 12.12465084, 6.464806968])
data = [AC, DC]
colors = ["#D55E00","#0072B2"]
labels = ['AC', 'DC']
bins = np.linspace(0, 45, 10) # Define the bins

commerciality_threshold = 15
unprofitable_threshold = 11

fig, ax = plt.subplots(figsize=(10, 6))
ax.axhspan(commerciality_threshold, 45, facecolor='lightgreen', alpha=0.2, label='Commercial profits')
ax.axhspan(unprofitable_threshold, commerciality_threshold, facecolor='yellow', alpha=0.2, label='Profitable, but at non-commercial rates')
ax.axhspan(0, unprofitable_threshold, facecolor='red', alpha=0.2, label='Unprofitable')

ax.hist(data, bins=bins, orientation='horizontal', stacked=True, 
        color=colors, label=labels, edgecolor='black')

combined_data = np.append(AC, DC)
combined_data_w_o_profit = [c for c in combined_data if c < commerciality_threshold]
Charge_east_av = combined_data.mean()
Charge_east_av_wo_profit = np.mean(combined_data_w_o_profit)
city = 7
regional = 3
x_max = 25
offset = -.2

ax.text(x_max-offset-10, Charge_east_av+.4, 'Eastern Suburbs network average', 
fontsize=14, ha='left', fontweight='bold')
ax.plot([0,x_max], [Charge_east_av,Charge_east_av], color='black', linewidth=3, zorder=10, linestyle='--')#, label='Financial viability')

labelfontsize = 15
ax.tick_params(axis='x', labelsize=labelfontsize)
ax.tick_params(axis='y', labelsize=labelfontsize)
ax.set_xlabel('% of Eastern Suburbs charging network', fontsize=labelfontsize)
ax.set_ylabel('Charging site average utilisation (% of time)', fontsize=labelfontsize)
ax.legend(loc='upper right', fontsize=14)

plt.ylim(0, 45)
plt.xlim(0, 27)
# Ensure layout is adjusted to prevent legend overlap
plt.tight_layout() 

plt.savefig('horizontal_histogram.png')
plt.savefig('horizontal_histogram.pdf')



# Remove chargers with such high utilisation rates that they generate commercial returns
AC = np.array([14.98888889,
      14.37911959,13.2125947,13.16029457,12.13045635, 11.9346174,11.83142245,
      11.4837963,11.41226398,10.65022275,10.2611715,10.26056505,9.912992571,
      9.51778297,9.50547138,9.226549919,8.981829574,8.947285354,8.536616162,
      8.329903978,7.783564815,7.65491453,7.432336182,7.27590812,7.10515873,
      6.602704678, 6.350308642, 4.254070881])
DC = np.array([12.12465084, 6.464806968])
data = [AC, DC]
colors = ["#D55E00","#0072B2"]
labels = ['AC', 'DC']
bins = np.linspace(0, 45, 10) # Define the bins

fig, ax = plt.subplots(figsize=(10, 6))
ax.axhspan(commerciality_threshold, 45, facecolor='lightgreen', alpha=0.2, label='Commercial profits')
ax.axhspan(unprofitable_threshold, commerciality_threshold, facecolor='yellow', alpha=0.2, label='Profitable, but at non-commercial rates')
ax.axhspan(0, unprofitable_threshold, facecolor='red', alpha=0.2, label='Unprofitable')

ax.hist(data, bins=bins, orientation='horizontal', stacked=True, 
        color=colors, label=labels, edgecolor='black')

combined_data = np.append(AC, DC)
combined_data_w_o_profit = [c for c in combined_data if c < commerciality_threshold]
Charge_east_av = combined_data.mean()
Charge_east_av_wo_profit = np.mean(combined_data_w_o_profit)
city = 7
regional = 3
x_max = 25
offset = -.2

ax.text(x_max-offset-10, Charge_east_av_wo_profit+1.2, 'Eastern Suburbs network average \nwithout commercial sites', 
fontsize=14, ha='left', fontweight='bold')
ax.plot([0,x_max], [Charge_east_av_wo_profit,Charge_east_av_wo_profit], color='black', linewidth=3, zorder=10, linestyle='--')#, label='Financial viability')

labelfontsize = 15
ax.tick_params(axis='x', labelsize=labelfontsize)
ax.tick_params(axis='y', labelsize=labelfontsize)
ax.set_xlabel('% of Eastern Suburbs charging network', fontsize=labelfontsize)
ax.set_ylabel('Charging site average utilisation (% of time)', fontsize=labelfontsize)

ax.legend(loc='upper right', fontsize=14)

plt.ylim(0, 45)
plt.xlim(0, 27)
# Ensure layout is adjusted to prevent legend overlap
plt.tight_layout() 

plt.savefig('horizontal_histogram-segregated.png')
plt.savefig('horizontal_histogram-segregated.pdf')
