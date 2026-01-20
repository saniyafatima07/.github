import os, time
import requests
import json
import math

ORG = "pointblank-club"
PER_PAGE = 100
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("Set TOKEN environment variable!")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

BASE = "https://api.github.com"
fail_count = 0
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "stats.json")

def get_all_repos():
    repos = []
    page = 1
    while True:
        url = f"{BASE}/orgs/{ORG}/repos?per_page={PER_PAGE}&page={page}"
        r = requests.get(url, headers=HEADERS)
        data = r.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def get_count(url):
    global fail_count
    try:
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        fail_count=0
        if "search/issues" in url:
            return r.json().get("total_count", 0)
        if "Link" not in r.headers:
            return len(r.json())
        link = r.headers["Link"]
        last_page = int(link.split("page=")[-1].split(">")[0])
        return last_page
    except requests.exceptions.HTTPError as e:
        if r.status_code in [403, 429]:
            fail_count += 1
            if fail_count >= 2:
                print("Rate limited, sleeping 2s...")
                time.sleep(2)
                fail_count = 0
            return 0
        else:
            print(f"Error fetching {url}: {e}")
            return 0
        
    except Exception as e:
        print(f"Error {url}: {e}")
        return 0

def get_repo_metrics(repo):
    name = repo["name"]
    return {
        "stargazers": repo.get("stargazers_count", 0),
        "forks": repo.get("forks_count", 0),
        "watchers": repo.get("watchers_count", 0),
        "size": repo.get("size", 0),
        "license": repo["license"]["key"] if repo.get("license") else None,
        "releases": get_count(f"{BASE}/repos/{ORG}/{name}/releases?per_page=1"),
        "issues_open": get_count(f"{BASE}/search/issues?q=is:issue+repo:{ORG}/{name}+state:open"),
        "issues_closed": get_count(f"{BASE}/search/issues?q=is:issue+repo:{ORG}/{name}+state:closed"),
        "prs_open": get_count(f"{BASE}/search/issues?q=is:pr+repo:{ORG}/{name}+is:open"),
        "prs_closed": get_count(f"{BASE}/search/issues?q=is:pr+repo:{ORG}/{name}+is:closed"),
        "prs_merged": get_count(f"{BASE}/search/issues?q=is:pr+repo:{ORG}/{name}+is:merged"),
        "prs_draft": get_count(f"{BASE}/search/issues?q=is:pr+repo:{ORG}/{name}+is:draft"),
        "commits": get_count(f"{BASE}/repos/{ORG}/{name}/commits?per_page=1"),
    }

def get_packages_count():
    try:
        url = f"{BASE}/orgs/{ORG}/packages"
        r = requests.get(url, headers=HEADERS)
        r.raise_for_status()
        return len(r.json())
    except requests.exceptions.HTTPError as e:
        print(f"Warning: Could not fetch packages ({e}) - skipping")
        return 0

def main():
    repos = get_all_repos()
    print(f"Fetched {len(repos)} repos, processing metrics...")

    total_stars = total_forks = total_watchers = total_storage = 0
    total_releases = total_issues_open = total_issues_closed = 0
    total_pr_open = total_pr_closed = total_pr_merged = total_pr_draft = 0
    total_commits = 0
    licenses = {}

    for i, repo in enumerate(repos, start=1):
            repo_metrics = get_repo_metrics(repo)
            total_stars += repo_metrics["stargazers"]
            total_forks += repo_metrics["forks"]
            total_watchers += repo_metrics["watchers"]
            total_storage += repo_metrics["size"]/1024
            total_releases += repo_metrics["releases"]
            total_issues_open += repo_metrics["issues_open"]
            total_issues_closed += repo_metrics["issues_closed"]
            total_pr_open += repo_metrics["prs_open"]
            total_pr_closed += repo_metrics["prs_closed"]
            total_pr_merged += repo_metrics["prs_merged"]
            total_pr_draft += repo_metrics["prs_draft"]
            total_commits += repo_metrics["commits"]

            if repo_metrics["license"]:
                licenses[repo_metrics["license"]] = licenses.get(repo_metrics["license"], 0) + 1

            print(f"Processed {i}/{len(repos)}: {repo['name']}")

    preferred_license = max(licenses.items(), key=lambda x: x[1])[0].upper() if licenses else "NONE"

    stats = {
        "organization": ORG,
        "repositories": len(repos),
        "preferred_license": preferred_license,
        "releases": total_releases,
        "packages": get_packages_count(),
        "storage_mb": math.ceil(total_storage),
        "sponsors": 0,
        "stargazers": total_stars,
        "forkers": total_forks,
        "watchers": total_watchers,
        "issues_open": total_issues_open,
        "issues_closed": total_issues_closed,
        "issues_draft": 0,
        "prs_open": total_pr_open,
        "prs_merged": total_pr_merged,
        "prs_draft": total_pr_draft,
        "prs_closed": total_pr_closed,
        "commits_overall": total_commits
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(stats, f, indent=4)

    print("Stats fetched successfully!")

if __name__ == "__main__":
    main()