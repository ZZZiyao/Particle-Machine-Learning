import pickle
import pandas as pd
import matplotlib.pyplot as plt
import os

bg1=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\bd2ddkst_munu_MD_2016_1014_reducedbranches.pkl')
bg2=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\bd2ddkst_munu_MD_2017_1016_reducedbranches.pkl')
bg3=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\bd2ddkst_munu_MD_2018_1018_reducedbranches.pkl')
bg4=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\bd2ddkst_munu_MU_2016_1013_reducedbranches.pkl')
bg5=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\bd2ddkst_munu_MU_2017_1015_reducedbranches.pkl')
bg6=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\bd2ddkst_munu_MU_2018_1017_reducedbranches.pkl')
sig1=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\output_kpitautau_2016_md_reducedbranches.pkl')
sig2=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\output_kpitautau_2016_mu_reducedbranches.pkl')
sig3=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\output_kpitautau_2017_md_reducedbranches.pkl')
sig4=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\output_kpitautau_2017_mu_reducedbranches.pkl')
sig5=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\output_kpitautau_2018_md_reducedbranches.pkl')
sig6=pd.read_pickle(r'D:\Year3\BSc Project\Particle-Machine-Learning\dataset\output_kpitautau_2018_mu_reducedbranches.pkl')


print(sig1['kaon_TRUEID'].unique())
# print(sig1['pion_TRUEID'].unique())
# print(sig1['kstar_TRUEID'].unique())
# print(sig1['mu_plus_TRUEID'].unique())
# print(sig1['mu_minus_TRUEID'].unique())


kstar_ids = [
    # Ground states
    313, -313, 323, -323,
    # K*_0 scalar states
    9000311, -9000311, 9000321, -9000321, 10311, -10311, 10321, -10321, 9020311, -9020311, 9020321, -9020321,
    # K*_2 tensor states
    315, -315, 325, -325, 90103315,  -90103315, 9010325, -9010325,
    # K*_3 higher tensor states
    317, -317, 327, -327,
    # K*_4 fourth tensor states
    319, -319, 329, -329,
    # Higher excited states
    30313, 30323, 100313, 100323, -30313, -30323, -100313, -100323
]

mu_plus_ids = [-13]
mu_minus_ids = [13]
kaon_ids = [321, -321]
pion_ids = [211, -211]

filtered_sig1 = sig1[
    (sig1['kstar_TRUEID'].isin(kstar_ids)) &
    (sig1['mu_plus_TRUEID'].isin(mu_plus_ids)) &
    (sig1['mu_minus_TRUEID'].isin(mu_minus_ids)) &
    (sig1['kaon_TRUEID'].isin(kaon_ids)) &
    (sig1['pion_TRUEID'].isin(pion_ids))
]

filtered_bg1 = bg1[
    (bg1['kstar_TRUEID'].isin(kstar_ids)) &
    (bg1['mu_plus_TRUEID'].isin(mu_plus_ids)) &
    (bg1['mu_minus_TRUEID'].isin(mu_minus_ids)) &
    (bg1['kaon_TRUEID'].isin(kaon_ids)) &
    (bg1['pion_TRUEID'].isin(pion_ids))
]

print(filtered_sig1['kstar_TRUEID'].unique())  


filtered_bg1.to_csv("filtered_bg1.csv", index=False)

filtered_sig1.to_csv("filtered_sig1.csv", index=False)



