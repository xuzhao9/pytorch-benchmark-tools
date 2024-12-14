"""
Backfiller for pytorch benchmarking.
"""
import argparse

from tools import TorchRepo, TritonRepo

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", choices=["pytorch", "triton"], required=True, help="Target repository to backfill.")
    parser.add_argument("--begin", required=True, help="Begin hash or date (YYYYMMDD).")
    parser.add_argument("--end", required=True, help="End hash or date (YYYYMMDD).")
    parser.add_argument("--step", choices=["nightly", "weekly", "monthly"], default="nightly", help="Backfill step, by default nightly.")
    parser.add_argument("--benchmark-script", required=True, help="Benchmark script to run")
    return parser


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    repo = TritonRepo() if args.target == "triton" else TorchRepo()
    # Checkout repository
    repo.checkout()
    # List commits to backfill
    commits = repo.init_commits()
    # Run backfill commits
    for commit in commits:
        repo.checkout_commit(commit)
        repo.build()
        repo.run_benchmark(args.benchmark_script)
