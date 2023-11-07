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

1. Clone the repo
   ```shell
   git clone https://github.com/miragon/robocorp-certifications.git
   cd robocorp-certifications
   ```

2. Install [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html)

   ```shell
   brew install miniconda
   conda init "$(basename "${SHELL}")"
   ```

3. Create a new conda environment

   ```shell
   conda env create -f conda.yaml -n robocorp
   ```

### Setup PyCharm

> Note: PyCharm is missing some of the convenient command from Visual Studio Code.
> Like bootstrapping a new robot project or uploading a robot to *Control Room*.
   
Open one of the projects in PyCharm and add new **Python Interpreter**
1. `PyCharm` > `Settings`
2. `Project: python-level?` > `Python Interpreter`
3. `Add Interpreter` > `Add Local Interpreter...`
4. Select `Conda Environment` > `Existing environment`
5. Select `robocorp` as the existing environment


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/Miragon/robocorp-cetifications.svg?style=for-the-badge

[contributors-url]: https://github.com/Miragon/robocorp-certifications/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Miragon/robocorp-certifications.svg?style=for-the-badge

[forks-url]: https://github.com/Miragon/robocorp-certifications/network/members

[stars-shield]: https://img.shields.io/github/stars/Miragon/robocorp-certifications.svg?style=for-the-badge

[stars-url]: https://github.com/Miragon/robocorp-certifications/stargazers

[issues-shield]: https://img.shields.io/github/issues/Miragon/robocorp-certifications.svg?style=for-the-badge

[issues-url]: https://github.com/Miragon/robocorp-certifications/issues

[license-shield]: https://img.shields.io/github/license/Miragon/robocorp-certifications.svg?style=for-the-badge

[license-url]: https://github.com/Miragon/robocorp-certifications/blob/main/LICENSE
