# sEDICT (stochastic EDICT)
The baseline model is EDICT: Exact Diffusion Inversion via Coupled Transformation in this repository: https://github.com/salesforce/EDICT
Please refer to the setup part for EDICT.
<img width="465" alt="image" src="https://github.com/ojoo-J/sEDICT/assets/124341473/cfa23250-15d0-40a1-9356-56a62bc09b8d">

# Experimental Results
<img width="960" alt="image" src="https://github.com/ojoo-J/sEDICT/assets/124341473/c8e5a898-861a-4334-b834-808900d5d7e9">
<img width="997" alt="image" src="https://github.com/ojoo-J/sEDICT/assets/124341473/fd44941f-0727-49f2-8393-8f5e87ce5a9f">

# Run Example
```
# reference-based image generation
python -u s_EDICT.py --b_prompt 'A dog' --t_prompt 'A dog' --s_i 0.7 --s_d 0.8 --seed 1 --scale 0.2

# image editing
python -u s_EDICT.py --b_prompt 'A dog' --t_prompt 'A golden retriever' --s_i 0.7 --s_d 0.8 --seed 1 --scale 0.2
```
