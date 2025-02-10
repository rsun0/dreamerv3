from slurm_launcher.sbatch_launcher import launch_tasks


def run_exp():
    base_cmd = "python -B dreamerv3/main.py"

    param_dict = {
        "--script": ["train_eval"],
        "--run.eval_eps": [100],
        "--logdir": ["/storage/raysun/dreamerv3/old_atari_{task}_{seed}"],
        "--configs": ["atari100k"],
        "--run.log_every": [10000],
        "--run.report_every": [400000],
        "--run.save_every": [0],
        "--task": [
            "atari100k_alien",
            "atari100k_amidar",
            "atari100k_assault",
            "atari100k_asterix",
            "atari100k_bank_heist",
            "atari100k_battle_zone",
            "atari100k_boxing",
            "atari100k_breakout",
            "atari100k_chopper_command",
            "atari100k_crazy_climber",
            "atari100k_demon_attack",
            "atari100k_freeway",
            "atari100k_frostbite",
            "atari100k_gopher",
            "atari100k_hero",
            "atari100k_jamesbond",
            "atari100k_kangaroo",
            "atari100k_krull",
            "atari100k_kung_fu_master",
            "atari100k_ms_pacman",
            "atari100k_private_eye",
            "atari100k_qbert",
            "atari100k_road_runner",
            "atari100k_seaquest",
            "atari100k_up_n_down",
        ],
        "--seed": range(0, 5),
        "--logger.outputs": ["jsonl wandb"],
    }
    job_name = "old_atari"

    launch_tasks(
        param_option=1,
        base_cmd=base_cmd,
        param_dict=param_dict,
        partition="rtx3090",
        timeout="7-00:00:00",
        job_name=job_name,
        max_job_num=24,
    )


if __name__ == "__main__":
    run_exp()
