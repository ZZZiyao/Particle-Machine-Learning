import pickle
import pandas as pd
import matplotlib.pyplot as plt
import os

file_path1 = r"C:\Users\xziya\Desktop\BSc Project\2018signal.pkl"
file_path2=r"C:\Users\xziya\Desktop\BSc Project\2018background.pkl"


with open(file_path1, 'rb') as file:
    signal = pickle.load(file)

with open(file_path2, 'rb') as file:
    background = pickle.load(file)

#print(signal.head())

particle_types = ['kaon_', 'pion_', 'mu_plus_', 'mu_minus_', 'B0_', 'jpsi_', 'kstar_']
particle_counts = {}

for ptype in particle_types:
    particle_counts[ptype] = len([col for col in signal.columns if col.startswith(ptype)])

kaon_columns = [col for col in signal.columns if col.startswith('kaon_')]


sig_kaon_data = signal[signal['kaon_TRUEID'] == 321]
bg_kaon_data = background[background['kaon_TRUEID'] == 321]
sig_pion_data = signal[signal['pion_TRUEID'] == 211]
bg_pion_data = background[background['pion_TRUEID'] == 211]


if __name__=='__main__':


    print(signal['kaon_TRUEID'].unique())
    print(signal['pion_TRUEID'].unique())


    output_dir = r'C:\Users\xziya\Desktop\BSc Project\Particle-Machine-Learning\Kaon_Plots'

    os.makedirs(output_dir, exist_ok=True)

    plt.hist(bg_kaon_data['kaon_PX'], bins=50, alpha=0.7, label='background')
    plt.hist(sig_kaon_data['kaon_PX'], bins=50, alpha=0.9, label='signal', color='green')
    plt.xlabel('Kaon PX (MeV/c)')
    plt.ylabel('Counts')
    plt.title('Kaon PX Distribution')
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'Kaon_PX_Distribution.png'))
    plt.close()

    plt.hist(bg_kaon_data['kaon_PY'], bins=50, alpha=0.7, label='background')
    plt.hist(sig_kaon_data['kaon_PY'], bins=50, alpha=0.9, label='signal', color='green')
    plt.xlabel('Kaon PY (MeV/c)')
    plt.ylabel('Counts')
    plt.title('Kaon PY Distribution')
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'Kaon_PY_Distribution.png'))
    plt.close()

    plt.hist(bg_kaon_data['kaon_PZ'], bins=50, alpha=0.7, label='background')
    plt.hist(sig_kaon_data['kaon_PZ'], bins=50, alpha=0.9, label='signal', color='green')
    plt.xlabel('Kaon PZ (MeV/c)')
    plt.ylabel('Counts')
    plt.title('Kaon PZ Distribution')
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'Kaon_PZ_Distribution.png'))
    plt.close()

    plt.hist(bg_kaon_data['kaon_P'], bins=50, alpha=0.7, label='background')
    plt.hist(sig_kaon_data['kaon_P'], bins=50, alpha=0.9, label='signal', color='green')
    plt.xlabel('Kaon P (MeV/c)')
    plt.ylabel('Counts')
    plt.title('Kaon Total Momentum Distribution')
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'Kaon_Total_Momentum_Distribution.png'))
    plt.close()

    plt.hist(bg_kaon_data['kaon_PT'], bins=50, alpha=0.7, label='background')
    plt.hist(sig_kaon_data['kaon_PT'], bins=50, alpha=0.9, label='signal', color='green')
    plt.xlabel('Kaon Transverse Momentum (MeV/c)')
    plt.ylabel('Counts')
    plt.title('Kaon Transverse Momentum Distribution')
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'Kaon_Transverse_Momentum_Distribution.png'))
    plt.close()

    plt.hist(bg_kaon_data['kaon_PE'], bins=50, alpha=0.7, label='background')
    plt.hist(sig_kaon_data['kaon_PE'], bins=50, alpha=0.9, label='signal', color='green')
    plt.xlabel('Kaon E (MeV)')
    plt.ylabel('Counts')
    plt.title('Kaon Total Energy Distribution')
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'Kaon_Total_Energy_Distribution.png'))
    plt.close()

    plt.hist(bg_kaon_data['kaon_M'], bins=50, alpha=0.7, label='background')
    plt.hist(sig_kaon_data['kaon_M'], bins=50, alpha=0.9, label='signal', color='green')
    plt.xlabel('Kaon M (MeV/c^2)')
    plt.ylabel('Counts')
    plt.title('Kaon Mass Distribution')
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'Kaon_Mass_Distribution.png'))
    plt.close()











    








