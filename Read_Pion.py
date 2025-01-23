from Read_Kaon import sig_pion_data, bg_pion_data
import matplotlib.pyplot as plt
import os



output_dir = r'C:\Users\xziya\Desktop\BSc Project\Particle-Machine-Learning\Pion_Plots'

os.makedirs(output_dir, exist_ok=True)

plt.hist(bg_pion_data['pion_PX'], bins=50,alpha=0.7, label='background')
plt.hist(sig_pion_data['pion_PX'],bins=50, alpha=0.9, label='signal', color='green')
plt.xlabel('Pion PY (MeV/c)')
plt.ylabel('Counts')
plt.title('Pion PY Distribution')
plt.legend()
plt.savefig(os.path.join(output_dir, 'Pion_PX_Distribution.png'))
plt.close()


plt.hist(bg_pion_data['pion_PY'], bins=50, alpha=0.7, label='background')
plt.hist(sig_pion_data['pion_PY'], bins=50, alpha=0.9, label='signal', color='green')
plt.xlabel('Pion PY (MeV/c)')
plt.ylabel('Counts')
plt.title('Pion PY Distribution')
plt.legend()
plt.savefig(os.path.join(output_dir, 'Pion_PY_Distribution.png'))
plt.close()

plt.hist(bg_pion_data['pion_PZ'], bins=50, alpha=0.7, label='background')
plt.hist(sig_pion_data['pion_PZ'], bins=50, alpha=0.9, label='signal', color='green')
plt.xlabel('Pion PZ (MeV/c)')
plt.ylabel('Counts')
plt.title('Pion PZ Distribution')
plt.legend()
plt.savefig(os.path.join(output_dir, 'Pion_PZ_Distribution.png'))
plt.close()


plt.hist(bg_pion_data['pion_P'], bins=50, alpha=0.7, label='background')
plt.hist(sig_pion_data['pion_P'], bins=50, alpha=0.9, label='signal', color='green')
plt.xlabel('Pion P (MeV/c)')
plt.ylabel('Counts')
plt.title('Pion Total Momentum Distribution')
plt.legend()
plt.savefig(os.path.join(output_dir, 'Pion_Total_Momentum_Distribution.png'))
plt.close()


plt.hist(bg_pion_data['pion_PT'], bins=50, alpha=0.7, label='background')
plt.hist(sig_pion_data['pion_PT'], bins=50, alpha=0.9, label='signal', color='green')
plt.xlabel('Pion Transverse Momentum (MeV/c)')
plt.ylabel('Counts')
plt.title('Pion Transverse Momentum Distribution')
plt.legend()
plt.savefig(os.path.join(output_dir, 'Pion_Transverse_Momentum_Distribution.png'))
plt.close()


plt.hist(bg_pion_data['pion_PE'], bins=50, alpha=0.7, label='background')
plt.hist(sig_pion_data['pion_PE'], bins=50, alpha=0.9, label='signal', color='green')
plt.xlabel('Pion E (MeV)')
plt.ylabel('Counts')
plt.title('Pion Total Energy Distribution')
plt.legend()
plt.savefig(os.path.join(output_dir, 'Pion_Total_Energy_Distribution.png'))
plt.close()


plt.hist(bg_pion_data['pion_M'], bins=50, alpha=0.7, label='background')
plt.hist(sig_pion_data['pion_M'], bins=50, alpha=0.9, label='signal', color='green')
plt.xlabel('Pion M (MeV/c^2)')
plt.ylabel('Counts')
plt.title('Pion Mass Distribution')
plt.legend()
plt.savefig(os.path.join(output_dir, 'Pion_Mass_Distribution.png'))
plt.close()
