# WorldSeed Lint 快速开始 / Quick Start

本指南将帮助你快速安装并运行 `worldseed-lint`。  
This guide helps you quickly install and run `worldseed-lint`.

## 前提条件 / Prerequisites

- 已安装 [Git](https://git-scm.com/)  
  Git is installed.
- 已安装 Conda（或 Miniconda/Anaconda）  
  Conda (or Miniconda/Anaconda) is installed.

## 安装与运行 / Installation and Execution

在终端中依次执行以下命令：  
Run the following commands in your terminal:

```bash
# 1. 创建 Conda 虚拟环境（Python 3.10）  
#    Create a Conda virtual environment (Python 3.10)
conda create -n ex python=3.10

# 2. 克隆项目仓库（请替换 <REPO_URL> 为实际地址）  
#    Clone the repository (replace <REPO_URL> with the actual URL)
git clone <REPO_URL>
cd <REPO_DIR>

# 3. 激活环境并以可编辑模式安装包  
#    Activate the environment and install the package in editable mode
conda activate ex
pip install -e .
```

> 💡 **提示 / Tip**：将 `<REPO_URL>` 替换为实际的 Git 仓库地址（例如 `https://github.com/example/worldseed-lint.git`），`<REPO_DIR>` 通常与仓库同名。  
> Replace `<REPO_URL>` with the actual repository URL, and `<REPO_DIR>` is usually the same as the repo name.

## 运行 Lint 检查 / Run Lint Checks

使用以下命令检查示例清单文件：  
Check example manifest files with these commands:

```bash
# 检查无效清单  
# Check an invalid manifest
worldseed-lint examples/invalid_world.json

# 检查有效清单  
# Check a valid manifest
worldseed-lint examples/valid_world.json
```