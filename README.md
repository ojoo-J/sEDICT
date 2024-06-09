# sEDICT (stochastic EDICT)
<img width="712" alt="image" src="https://github.com/ojoo-J/sEDICT/assets/124341473/3e809337-d422-4175-8a2c-c306519ff1ec">

The baseline model is EDICT: Exact Diffusion Inversion via Coupled Transformation in this repository: https://github.com/salesforce/EDICT
Please refer to the setup part for EDICT.

# Experimental Results
<img width="960" alt="image" src="https://github.com/ojoo-J/sEDICT/assets/124341473/c8e5a898-861a-4334-b834-808900d5d7e9">
<img width="960" alt="image" src="https://github.com/ojoo-J/sEDICT/assets/124341473/854c0020-5ade-4a6c-a17d-07c11a7d7e37">

# Run Example
```
# reference-based image generation
python -u s_EDICT.py --b_prompt 'A dog' --t_prompt 'A dog' --s_i 0.7 --s_d 0.8 --seed 1 --scale 0.2

# image editing
python -u s_EDICT.py --b_prompt 'A dog' --t_prompt 'A golden retriever' --s_i 0.7 --s_d 0.8 --seed 1 --scale 0.2
```

# Evaluation
```
python qualitative_evaluation.py --reference_img_path REF_PATH --generated_img_path GEN_PATH
```
