import pickle as pkl
import numpy as np



with open('center_neuron_info_radius10.pkl', 'rb') as file:
    data = pkl.load(file)

# data is a dict with keys:
# 'bo_info': meta information, such as neuron id, bav etc.
# 'res_info': response information, units' responses to different square orientations.
# 'stim_info': stimulus information, such as stimulus, orientation etc.
# 'unique_orientation': unique orientation, ignore this
print(data.keys())

# bo_info is a dict with keys:
# 'E0': E0 module's bo_info
# 'E1': E1 module's bo_info
# 'E2': E2 module's bo_info
# 'E3': E3 module's bo_info
print(data['bo_info'].keys())

# data['bo_info']['E0'] is a dict with keys:
# 'neuron_id': a 3D tuple, continas neuron id
# 'BOI': BOI value at each orientation
# 'boi_abs_max': maximum BOI value
# 'boi_pref_dire': preferred BOI direction of the neuron
# 'boi_abs_rank': 
# 'bav': bav value
# 'bav_angle': the angle of circular averaged boi
# 'bav_p_value': p value of bav. If smaller than 0.05, the neuron is a BOS unit.
# 'is_bo': whether the neuron is a BOS unit, by bav_p_value < 0.05
# 'bo_only_rank': the rank of the neuron among all BOS units
# 'heatmap': heatmap of the neuron's response to different sparse noise stimuli (can be used to estimate cRF size)
# 'rf': cRF
print(data['bo_info']['E2'].keys())

for mode in ['E0', 'E1', 'E2', 'E3']:
    print(mode)
    #print("number of BOS units: ", np.sum(data['bo_info'][mode]['is_bo']))
    print("number of canidate:", np.size(data['bo_info'][mode]))

print("E_0 id?", data['bo_info']['E0']['neuron_id'][50])