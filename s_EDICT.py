from sEDICT_functions import *
import argparse

parser = argparse.ArgumentParser(description="Stochastic editing with EDICT")
parser.add_argument("--reference_img_path", default="experiment_images/imagenet_dog_7.jpg", type=str, help="original img path")
parser.add_argument("--b_prompt", default="A dog", type=str, help="base prompt")
parser.add_argument("--t_prompt", default="A dog", type=str, help="target prompt")
parser.add_argument("--steps", default=50, type=int, help='number of total inversion steps')
parser.add_argument("--s_i", default=0.7, type=float, help='init image strength for inversion')
parser.add_argument("--s_d", default=0.8, type=float, help='init image strength for denoising')
parser.add_argument("--seed", default=1, type=int, help="init seed")
parser.add_argument("--scale", default=0.2, type=float, help="added noise scale")
parser.add_argument("--n_sample", default=10, type=int, help="number of edited images to generate")
parser.add_argument("--save_dir", default='./results/', type=str, help="save dir")

if __name__ == "__main__":
    args = parser.parse_args()
    print(args)
    os.makedirs(args.save_dir, exist_ok=True)
    
    im_path = args.reference_img_path
    base_prompt = args.b_prompt
    target_prompt = args.t_prompt
    
    gens = sEDICT_editing(im_path,
                          base_prompt,
                          target_prompt, 
                          init_image_strength=args.s_i,
                          steps=args.steps,
                          d_init_image_strength=args.s_d,
                          noise_seed=args.seed,
                          noise_scale=args.scale,
                          n_sample=args.n_sample,
                         save_dir=args.save_dir
                        )