from slurm_launcher.sbatch_launcher import launch_tasks


def run_exp():
    base_cmd = "python -B dreamerv3/main.py"

    param_dict = {
        "--script": ["train_eval"],
        "--logdir": ["/storage/raysun/dreamerv3/eval_test_{task}_{seed}"],
        "--configs": ["atari100k"],
        "--run.eval_eps": [100],
        "--run.log_every": [1000],
        "--run.report_every": [10000],
        "--run.save_every": [100000],
        "--seed": range(0, 5),
        "--task": ["atari100k_jamesbond", "atari100k_kung_fu_master", "atari100k_up_n_down"],
        "--logger.outputs": ["jsonl wandb"],
    }
    job_name = "dreamerv3_three"

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
