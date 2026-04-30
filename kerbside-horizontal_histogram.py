import matplotlib.pyplot as plt
import numpy as np

# 1. Generate sample data
# Three datasets to stack, e.g., representing different categories within bins
# data1 = np.random.randn(1000) * 40
# data2 = np.random.randn(1000) * 40
# data = [data1, data2]
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
unprofitable_threshold = 8

# 2. Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# 3. Add 5 different shaded areas in the background using axhspan
# Define the y-limits for the shaded regions (based on your bins)
# We use axhspan to fill horizontal spans across the entire axis
ax.axhspan(commerciality_threshold, 45, facecolor='lightgreen', alpha=0.2, label='Commercial profits')
ax.axhspan(unprofitable_threshold, commerciality_threshold, facecolor='yellow', alpha=0.2, label='Profitable, but at non-commercial rates')
# ax.axhspan(unprofitable_threshold, 10, facecolor='yellow', alpha=0.2, label='Non-commercial returns if 100% capex subsidised')
ax.axhspan(0, unprofitable_threshold, facecolor='red', alpha=0.2, label='Unprofitable')


# region_x = 16
# ax.text(region_x, 25, 'Commercially profitable', fontsize=12, 
# ha='left')#, fontweight='bold', backgroundcolor='white')
# ax.text(region_x, 13, 'Commercially profitable with 80% subsidy', fontsize=12, 
# ha='left')#
# ax.text(region_x, 8, 'Non-commercially profitable with 80% subsidy', fontsize=12, 
# ha='left')#
# ax.text(region_x, 1, 'Unprofitable', fontsize=12, 
# ha='left')#


# 4. Plot the horizontal stacked histogram
ax.hist(data, bins=bins, orientation='horizontal', stacked=True, 
        color=colors, label=labels, edgecolor='black')

# 5. Add 4 horizontal lines
# Define the y-positions for the lines (e.g., at specific bin edges or values)
# line_positions = [40, 45, 55, 60]
# for y_pos in line_positions:
#     ax.axhline(y_pos, color='black', linestyle='--', linewidth=1.5)

combined_data = np.append(AC, DC)
combined_data_w_o_profit = [c for c in combined_data if c < commerciality_threshold]
print(len(combined_data))
print(len(combined_data_w_o_profit))
Charge_east_av = combined_data.mean()
Charge_east_av_wo_profit = np.mean(combined_data_w_o_profit)
city = 7
regional = 3
x_max = 25
offset = -.2

ax.text(x_max-offset-10, Charge_east_av+.4, 'Eastern Suburbs network average', 
fontsize=14, ha='left', fontweight='bold')#, backgroundcolor='white')
ax.plot([0,x_max], [Charge_east_av,Charge_east_av], color='black', linewidth=3, zorder=10, linestyle='--')#, label='Financial viability')
# ax.text(x_max-offset, Charge_east_av_wo_profit-1, 'Eastern Suburbs network average \nw/o profitable sites', fontsize=12, 
# ha='left', fontweight='bold')#, backgroundcolor='white')
# ax.plot([0,x_max], [Charge_east_av_wo_profit,Charge_east_av_wo_profit], color='black', linewidth=3, zorder=10, linestyle='--')#, label='Financial viability')


# ax.text(x_max-offset, city-.5, 'Urban AC networks (anecdotal)', fontsize=12, 
# ha='left', fontweight='bold')#, backgroundcolor='white')
# ax.plot([0,x_max], [city,city], color='black', linewidth=3, zorder=10, linestyle='-.')#, label='Financial viability')
# ax.text(x_max-offset, regional-.5, 'Regional AC networks (anecdotal)', fontsize=12, 
# ha='left', fontweight='bold')#, backgroundcolor='white')
# ax.plot([0,x_max], [regional,regional], color='black', linewidth=3, zorder=10, linestyle=':')#, label='Financial viability')     

# 6. Customize the plot
labelfontsize = 15
ax.tick_params(axis='x', labelsize=labelfontsize)
ax.tick_params(axis='y', labelsize=labelfontsize)
ax.set_xlabel('% of Eastern Suburbs charging network', fontsize=labelfontsize)
ax.set_ylabel('Charging site average utilisation (% of time)', fontsize=labelfontsize)
# ax.set_title('Profitability of kerbside charging networks', fontsize=20)

ax.legend(loc='upper right', fontsize=14)#, bbox_to_anchor=(1.25, 1))
# ax.grid(axis='x', linestyle=':', alpha=0.6)

plt.ylim(0, 45)
plt.xlim(0, 27)
# Ensure layout is adjusted to prevent legend overlap
plt.tight_layout() 

# 7. Display the plot
# plt.show()
plt.savefig('horizontal_histogram.png')












# 1. Generate sample data
# Three datasets to stack, e.g., representing different categories within bins
# data1 = np.random.randn(1000) * 40
# data2 = np.random.randn(1000) * 40
# data = [data1, data2]
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

commerciality_threshold = 15
unprofitable_threshold = 8

# 2. Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# 3. Add 5 different shaded areas in the background using axhspan
# Define the y-limits for the shaded regions (based on your bins)
# We use axhspan to fill horizontal spans across the entire axis
ax.axhspan(commerciality_threshold, 45, facecolor='lightgreen', alpha=0.2, label='Commercial profits')
ax.axhspan(unprofitable_threshold, commerciality_threshold, facecolor='yellow', alpha=0.2, label='Profitable, but at non-commercial rates')
# ax.axhspan(10, commerciality_threshold, facecolor='blue', alpha=0.2, label='Commercial returns if 80% capex subsidised')
# ax.axhspan(unprofitable_threshold, 10, facecolor='yellow', alpha=0.2, label='Non-commercial returns if 100% capex subsidised')
ax.axhspan(0, unprofitable_threshold, facecolor='red', alpha=0.2, label='Unprofitable')

# region_x = 16
# ax.text(region_x, 25, 'Commercially profitable', fontsize=12, 
# ha='left')#, fontweight='bold', backgroundcolor='white')
# ax.text(region_x, 13, 'Commercially profitable with 80% subsidy', fontsize=12, 
# ha='left')#
# ax.text(region_x, 8, 'Non-commercially profitable with 80% subsidy', fontsize=12, 
# ha='left')#
# ax.text(region_x, 1, 'Unprofitable', fontsize=12, 
# ha='left')#


# 4. Plot the horizontal stacked histogram
ax.hist(data, bins=bins, orientation='horizontal', stacked=True, 
        color=colors, label=labels, edgecolor='black')

# 5. Add 4 horizontal lines
# Define the y-positions for the lines (e.g., at specific bin edges or values)
# line_positions = [40, 45, 55, 60]
# for y_pos in line_positions:
#     ax.axhline(y_pos, color='black', linestyle='--', linewidth=1.5)

combined_data = np.append(AC, DC)
combined_data_w_o_profit = [c for c in combined_data if c < commerciality_threshold]
print(len(combined_data))
print(len(combined_data_w_o_profit))
Charge_east_av = combined_data.mean()
Charge_east_av_wo_profit = np.mean(combined_data_w_o_profit)
city = 7
regional = 3
x_max = 25
offset = -.2

ax.text(x_max-offset-10, Charge_east_av_wo_profit+1.2, 'Eastern Suburbs network average \nwithout commercial sites', 
fontsize=14, ha='left', fontweight='bold')#, backgroundcolor='white')
ax.plot([0,x_max], [Charge_east_av_wo_profit,Charge_east_av_wo_profit], color='black', linewidth=3, zorder=10, linestyle='--')#, label='Financial viability')
# ax.text(x_max-offset, Charge_east_av_wo_profit-1, 'Eastern Suburbs network average \nw/o profitable sites', 
# fontsize=14, ha='left', fontweight='bold')#, backgroundcolor='white')
# ax.plot([0,x_max], [Charge_east_av_wo_profit,Charge_east_av_wo_profit], color='black', linewidth=3, zorder=10, linestyle='--')#, label='Financial viability')


# ax.text(x_max-offset, city-.5, 'Urban AC networks (anecdotal)', fontsize=12, 
# ha='left', fontweight='bold')#, backgroundcolor='white')
# ax.plot([0,x_max], [city,city], color='black', linewidth=3, zorder=10, linestyle='-.')#, label='Financial viability')
# ax.text(x_max-offset, regional-.5, 'Regional AC networks (anecdotal)', fontsize=12, 
# ha='left', fontweight='bold')#, backgroundcolor='white')
# ax.plot([0,x_max], [regional,regional], color='black', linewidth=3, zorder=10, linestyle=':')#, label='Financial viability')     

# 6. Customize the plot
labelfontsize = 15
ax.tick_params(axis='x', labelsize=labelfontsize)
ax.tick_params(axis='y', labelsize=labelfontsize)
ax.set_xlabel('% of Eastern Suburbs charging network', fontsize=labelfontsize)
ax.set_ylabel('Charging site average utilisation (% of time)', fontsize=labelfontsize)
# ax.set_title('Profitability of kerbside charging networks', fontsize=20)

ax.legend(loc='upper right', fontsize=14)#, bbox_to_anchor=(1.25, 1))
# ax.grid(axis='x', linestyle=':', alpha=0.6)

plt.ylim(0, 45)
plt.xlim(0, 27)
# Ensure layout is adjusted to prevent legend overlap
plt.tight_layout() 

# 7. Display the plot
# plt.show()
plt.savefig('horizontal_histogram-segregated.png')
