# Collective Mind toolkit

[![Python Version](https://img.shields.io/badge/python-3+-blue.svg)](https://github.com/mlcommons/ck/tree/master/ck2)
[![PyPI version](https://badge.fury.io/py/cmind.svg)](https://badge.fury.io/py/cmind)
[![License](https://img.shields.io/badge/License-Apache%202.0-green)](https://github.com/mlcommons/ck/tree/master/ck2)


The Collective Mind toolkit (CM) transforms Git repositories, Docker containers, Jupyter notebooks, zip/tar files
and any local directory into a collective database of reusable artifacts 
and automation scripts with a unified interface and extensible meta descriptions.

Our goal is to help researchers and engineers exchange their artifacts, knowledge, 
experience and best practices in a more automated, reusable, portable and unified way
across rapidly evolving software and hardware.

CM is motivated by our tedious experience reproducing [150+ ML and Systems papers](https://www.youtube.com/watch?v=7zpeIVwICa4)
when [our colleagues](https://ctuning.org/ae/committee.html) have spent many frustrating months communicating with each other 
and trying to understand numerous technical reports, README files, specifications, dependencies, 
ad-hoc scripts, tools, APIs, models and data sets of all shared projects 
to be able to [validate experimental results](https://cknowledge.io/?q=%22reproduced-papers%22) 
and adapt ad-hoc projects to the real world with very diverse 
and continuously changing software, hardware, user environments, settings and data.

The Collective Mind toolkit is based on the [Collective Knowledge concept (CK)]( https://arxiv.org/abs/2011.01149 )
that was successfully validated in the past few years to provide a simple, common and extensible format 
and API for shared projects and make it easier for researchers and engineers to communicate, collaborate and innovate.
The CK prototype was used to [enable collaborative ML and Systems R&D](https://cKnowledge.org/partners.html),
[connect MLOps and DevOps](https://github.com/mlcommons/ck-mlops) by treating models, datasets and other artifacts as "code" packages,
[automate the MLPerf inference benchmark](https://github.com/mlcommons/ck/tree/master/docs/mlperf-automation),
and [automate the development and deployment of Pareto-efficient ML Systems in the real world](https://www.youtube.com/watch?v=1ldgVZ64hEI).
We are desiging the CM toolkit based on all the feedback we have received from these projects.

See related slides [about our motivation](docs/motivation.md) and a related article 
about ["MLOps Is a Mess But That's to be Expected"](https://www.mihaileric.com/posts/mlops-is-a-mess) (March 2022).



# License

Apache 2.0



# How it works

* Check this [getting started tutorial](docs/getting-started.md) 
  to understand the Collective Mind concepts and try this toolkit.


# Community meetings

* [Public notes](meetings/)
* [Regular conf-calls](meetings/conf-calls.md)


# News

* **2022 April 20:** Join us at the public MLCommons community meeting. Register [here](https://docs.google.com/spreadsheets/d/1bb7qWgWM-6gop1Mwjm4u8LZtC7uqbee8C30DHipkkms/edit#gid=533252977).

* **2022 April 3:** We presented our approach to bridge the growing gap between ML Systems research and production 
  at the HPCA'22 workshop on [benchmarking deep learning systems](https://sites.google.com/g.harvard.edu/mlperf-bench-hpca22/home).

* **2022 March:** We presented our concept to [enable collaborative and reproducible ML Systems R&D](https://meetings.siam.org/sess/dsp_programsess.cfm?SESSIONCODE=73126) 
  at the SIAM'22 workshop on "Research Challenges and Opportunities within Software Productivity, Sustainability, and Reproducibility"

* **2022 March:** we've released the first prototype of [the Collective Mind toolkit (CK2)](https://github.com/mlcommons/ck/tree/master/ck2)
  based on your feedback and our practical experience [reproducing 150+ ML and Systems papers and validating them in the real world](https://www.youtube.com/watch?v=7zpeIVwICa4).



# Documentation

* [User guide and API (under development)](https://cknowledge.org/docs/cm)



# Development

## CM core 

We use [GitHub tickets](https://github.com/mlcommons/ck/issues) 
to improve and enhance the CM core that manages shared projects
as a collective database of reusable artifacts and automations.
Please don't hesitate to share your ideas and report encountered issues!


## Reusable CM components

We are developing reusable CM components to bridge [the gap](https://www.mihaileric.com/posts/mlops-is-a-mess) 
between MLOps and DevOps and make it easier to co-design, benchmarking, optimize and deploy
AI and ML system across continuously changing software and hardware stacks: https://github.com/octoml/cm-mlops . 


## Modular CM-based projects

TBA



# Resources

* [MLOps](docs/KB/MLOps.md)


# Acknowledgments

We thank the [users and partners of the original CK framework](https://cKnowledge.org/partners.html), 
[OctoML](https://octoml.ai), [MLCommons](https://mlcommons.org) 
and all our colleagues for their valuable feedback and support!


# Contacts

* [Grigori Fursin](https://cKnowledge.io/@gfursin) - author and coordinator
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh) - coordinator and maintainer
