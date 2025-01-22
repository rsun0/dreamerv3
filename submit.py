from slurm_launcher.sbatch_launcher import launch_tasks


def run_exp():
    base_cmd = "python -B dreamerv3/train.py"

    param_dict = {
        "--script": ["train_eval"],
        "--logdir": ["/storage/raysun/dreamerv3/old_dreamer_{task}_{seed}"],
        "--configs": ["atari100k"],
        "--seed": range(0, 5),
        "--run.log_every": [1000],
        "--run.save_every": [100000],
    }
    job_name = "old_dreamer"

    launch_tasks(
        param_option=1,
        base_cmd=base_cmd,
        param_dict=param_dict,
        partition="rtx3090",
        timeout="7-00:00:00",
        job_name=job_name,
    )


if __name__ == "__main__":
    run_exp()