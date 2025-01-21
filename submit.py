from slurm_launcher.sbatch_launcher import launch_tasks


def run_exp():
    base_cmd = "python -B dreamerv3/main.py"

    param_dict = {
        "--logdir": ["/storage/raysun/dreamerv3/{task}_{seed}"],
        "--configs": ["atari100k"],
        "--run.log_every": [120],
        "--run.report_every": [300],
        "--run.save_every": [10000],
        "--seed": range(0, 5),
        "--task": ["atari100k_pong"],
        "--logger.outputs": ["jsonl wandb"],
    }
    job_name = "dreamerv3_pong"

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
