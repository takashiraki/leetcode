# Docker Python — LeetCode Practice Environment

A Python LeetCode practice environment using Docker + Dev Container.

## Environment

| Item | Details |
|------|---------|
| Base Image | `python:3` |
| Extra Tools | `git`, `lazygit`, `tmux`, `vim` |
| VSCode Extensions | Python Extension Pack, LeetCode |
| Port | 8080 |

## Setup

### Prerequisites

- [Docker](https://www.docker.com/) installed
- [VS Code](https://code.visualstudio.com/) + [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed

### Getting Started

1. Clone this repository

```bash
git clone <repo-url>
cd docker_python
```

2. Open the folder in VS Code and run the following from the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)

```
Dev Containers: Reopen in Container
```

The container will be built and started automatically.

## LeetCode Usage

After starting the Dev Container, log in via the LeetCode extension in the VS Code sidebar and start solving problems.  
Solutions are saved in the `.leetcode/` directory.

## Solved Problems

| # | Title | Difficulty | Approach |
|---|-------|------------|----------|
| 1 | [Two Sum](.leetcode/1.two-sum.py) | Easy | Hash Map |
| 2 | [Add Two Numbers](.leetcode/2.add-two-numbers.py) | Medium | Linked List |
| 3 | [Longest Substring Without Repeating Characters](.leetcode/3.longest-substring-without-repeating-characters.py) | Medium | Sliding Window |
| 4 | [Median of Two Sorted Arrays](.leetcode/4.median-of-two-sorted-arrays.py) | Hard | Merge & Sort |

## Directory Structure

```
.
├── .devcontainer/
│   └── devcontainer.json   # Dev Container config
├── .leetcode/              # LeetCode solutions
├── Dockerfile              # Container definition
└── requirements.txt        # Python dependencies
```
