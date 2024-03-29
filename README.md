<div id="top"></div>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- END OF PROJECT SHIELDS -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
    <a href="#">
        <img src="https://avatars.githubusercontent.com/u/54288445?s=200&v=4?raw=true" alt="Logo" height="180">
    </a>
    <h3 ><a href="https://robocorp.com/docs/courses">Robocorp Certifications</a></h3>
</div>

## About The Project

This is the repository that contains the robots for the different levels of certification.

## Getting started

In the tutorials it is recommended to use [Visual Studio Code](https://code.visualstudio.com/) as the IDE.
But it is possible to use any other IDE (e.g. *PyCharm*).
These IDEs lacks some of the practical commands of Visual Studio Code,
but you can use the [rcc](https://robocorp.com/docs/rcc/overview) command line tool to do this.

1. [RCC](#rcc)
2. [Conda](#conda)
3. [PyCharm](#pycharm)

## RCC

In the following sections you will find some useful tips on how to set up and use `rcc`.

### Installation

```shell
# MacOS
brew install robocorp/tools/rcc
```

### Autocompletion in ZSH

1. If the environment variable `FPATH` does not hold any value add one
   1. Create a new folder in your home directory

      ```shell
      mkdir ~/.zfunc
      ```

   2. Open `~/.zshrc` in your favorite editor and add the following line

      ```text
      fpath=(~/.zfunc $fpath)
      ```

2. Create the autocompletion script

   ```shell
   rcc completion > ~/.zfunc/_rcc
   ```

3. Make the script executable

   ```shell
   chmod +x ~/.zfunc/_rcc
   ```

4. Reload your shell

   ```shell
   exec zsh
   ```

### Create a new robot project

Enter the following command in the terminal and follow the instructions.

```shell
rcc create
```

### Upload a robot to Control Room

1. Ensure you have access to the workspace
   1. Open the `Control Center`
   2. Select your `Workspace` (top left corner)
   3. Go to `User Settings` (top right corner)
   4. Go to `Access Credentials` and add your credentials

2. Add your credentials to the rcc config

   ```shell
   # Get the Workspace ID
   rcc cloud workspace
   ```

   ```shell
   # This will add the credentials to your default account
   rcc configure credentials <YOUR_CREDENTIALS>
   ```

   ```shell
   # This will add the credentials to a specific account or will create a new one
   rcc configure -a <YOUR_ACCOUNT> credentials <YOUR_CREDENTIALS>
   ```

   > Note: You can find the file with the configuration at `$ROBOCORP_HOME/rcc.yml` (default: ~/.robocorp/rcc.yml)

3. Create a new robot in your workspace

   ```shell
   rcc cloud new -r <YOUR_DESIRED_TASK_NAME> -w <WORKSPACE_ID>
   ```

4. Push your local robot to Control Room

   ```shell
   # Get the Task ID
   rcc cloud workspace -w <WORKSPACE_ID>
   ```

   ```shell
   rcc cloud push -r <TASK_ID> -w <WORKSPACE_ID>
   ```

## Conda

### Installation

```shell
# MacOS
brew install miniconda
conda init "$(basename "${SHELL}")"
```

### Create a new environment

If you used `rcc` to create a new robot project, you can use the `conda.yaml` file to create a new environment.

```shell
conda env create -f conda.yaml -n <your-conda-env>
```

## PyCharm

### Setup `conda` as the **Python Interpreter**

Open your robot project in PyCharm and add new **Python Interpreter**

1. `PyCharm` > `Settings`
2. `Project: <your-project-name>` > `Python Interpreter`
3. `Add Interpreter` > `Add Local Interpreter...`
4. Select `Conda Environment` > `Existing environment`
5. Select `<your-conda-env>` as the existing environment

### Setup Run Configurations

1. Install `EnvFile` plugin for using JSON files instead of .env files
   > ℹ️ Dependent on the template you used while creating the project with `rcc` there might already be some
   > environment variables under `/devdata`.
   > These environment variables are stored in a JSON file.

2. Add a Run Configuration

   > ⚠️ You can find the necessary information for the *Run Configurations* in the `robot.yaml` file created by `rcc`.

   > ℹ️ You can find my *Run Configurations* in `.run` in the respective project folders.

   <p>
      <img src="images/run-config.png" alt="Example of a Run Configuration" width="800"><br>
      <em>Example of a Run Configuration</em>
   </p>



<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/Miragon/robocorp-cetification.svg?style=for-the-badge

[contributors-url]: https://github.com/Miragon/robocorp-certification/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Miragon/robocorp-certification.svg?style=for-the-badge

[forks-url]: https://github.com/Miragon/robocorp-certification/network/members

[stars-shield]: https://img.shields.io/github/stars/Miragon/robocorp-certification.svg?style=for-the-badge

[stars-url]: https://github.com/Miragon/robocorp-certification/stargazers

[issues-shield]: https://img.shields.io/github/issues/Miragon/robocorp-certification.svg?style=for-the-badge

[issues-url]: https://github.com/Miragon/robocorp-certification/issues

[license-shield]: https://img.shields.io/github/license/Miragon/robocorp-certification.svg?style=for-the-badge

[license-url]: https://github.com/Miragon/robocorp-certification/blob/main/LICENSE
