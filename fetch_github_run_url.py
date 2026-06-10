import json
import urllib.request


def main():
    api_url = "https://api.github.com/repos/vidhyajose98-dotcom/V_Care_/actions/runs?per_page=1"
    req = urllib.request.Request(api_url, headers={"User-Agent": "Automation"})
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode())
    runs = data.get('workflow_runs', [])
    if runs:
        print(runs[0].get('html_url'))
    else:
        print("NO_RUN")


if __name__ == '__main__':
    main()
