[ [Back to index](README.md) ]

# MLCommons Task force on Automation and Reproducibility

***Announcement: we are peparing new tasks for Q2-Q3 2024 with MLCommons and looking for volunteers and an extra co-chair.
   Please get in touch via [email](mailto:gfursin@cknowledge.org) or [Discord](https://discord.gg/JjWNWXKxwT) for more details!***

## Mission

* Develop [reusable automation recipes and workflows](https://access.cknowledge.org/playground/?action=scripts) 
  with [a common and human-friendly interface (Collective Mind aka CM)](https://github.com/mlcommons/ck) 
  to support MLCommons projects and help everyone assemble, run, reproduce, customize and optimize ML(Perf) benchmarks
  in a unified and automated way across diverse models, data sets, software and hardware from different vendors.
* Gradually extend a unified MLCommons CM interface to automate [all MLPerf inference submissions](https://github.com/mlcommons/ck/issues/1052) starting from v3.1.
* Continuously encode MLPerf rules and best practices in the [CM automation recipes and workflows for MLPerf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script)
  to reduce the burden for submitters to go through numerous README files 
  and track all the latest changes and updates.
* [Automatically compose high-performance and cost-efficient AI applications and systems using MLPerf and CM](https://doi.org/10.5281/zenodo.10786893).

## Chairs and Tech Leads

* [Grigori Fursin](https://cKnowledge.org/gfursin)
* [Arjun Suresh](https://www.linkedin.com/in/arjunsuresh)

## Discussions

Since we already participate in many weekly conf-calls to support various MLCommons initiatives, 
we decided not to have yet another separate conf-call for our TF in 2024.
Instead, we discuss our progress on MLPerf automation and reproducibility at existing MLCommons conf-calls
where CM is used:
* [MLPerf inference WG](https://mlcommons.org/working-groups/benchmarks/inference): weekly conf-calls on Tuesday at 8:30am PST
* [MLPerf automotive WG](https://mlcommons.org/working-groups/benchmarks/automotive)
  * Automotive TF weekly conf-calls on Wednesday at 8am PST
  * Automotive implementation bi-weekly conf-calls on Friday at 9:30am PST
* [Croissant TF](https://github.com/mlcommons/croissant): weekly at 8am PST

You can participate in our discussions via [public Discord server](https://discord.gg/JjWNWXKxwT).

## Deliverables (2024)

* Collaborate with chip vendors and MLPerf inference submitters to add
  their implementations to CM and automate their submissions.

* Develop a more universal Python and C++ wrapper for the MLPerf loadgen
  with the CM automation to support different models, data sets, software
  and hardware: [Python prototype](https://github.com/mlcommons/ck/blob/master/docs/tutorials/scc23-mlperf-inference-bert.md); 
  [C++ prototype](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-mlcommons-cpp).

* Introduce [CM automation badge](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/app-mlperf-inference-mlcommons-cpp) 
  to MLPerf inference v4.1 submission
  similar to ACM/IEEE/NeurIPS reproducibility badges to make it easier for
  all submitters to re-run and reproduce each others’ results before the
  publication date.

* Collaborate with system vendors and cloud providers to quickly benchmark
  their platforms using the best available MLPerf inference implementation.

* Collaborate with other MLPerf working groups to modularize their
  benchmarks using [CM automation recipes](https://access.cknowledge.org/playground/?action=scripts).

* Use MLCommons CM to modularize and automate the upcoming [automotive benchmark](https://mlcommons.org/working-groups/benchmarks/automotive/).

* Use [MLCommons Croissant](https://mlcommons.org/working-groups/data/croissant/) 
  to unify [MLPerf datasets](https://access.cknowledge.org/playground/?action=scripts).



## Completed deliverables

* Developed [reusable and technology-agnostic automation recipes and workflows](https://access.cknowledge.org/playground/?action=scripts) 
  with a common and human-friendly interface (MLCommons Collective Mind aka CM) to modularize
  MLPerf inference benchmarks and run them in a unified and automated way
  across diverse models, data sets, software and hardware from different
  vendors.

* Added [GitHub actions](https://github.com/mlcommons/inference/tree/master/.github/workflows) 
  to test MLPerf inference benchmarks using CM.

* Encoded MLPerf inference rules and best practices in the [CM automation
  recipes and workflows for MLPerf](https://github.com/mlcommons/ck/tree/master/cm-mlops/script) 
  and reduced the burden for submitters to go through numerous README files 
  and track all the latest changes and reproduce results.

* Automated [MLPerf inference submissions](https://access.cknowledge.org/playground/?action=howtorun) 
  and made it easier to re-run and reproduce results 
  (see [submitters orientation](https://doi.org/10.5281/zenodo.10605079) 
  and [CM-MLPerf documentation](https://github.com/mlcommons/ck/tree/master/docs/mlperf)).

* Started developing an open-source platform to automatically compose
  high-performance and cost-effective AI applications and systems using
  MLPerf and CM (see our [presentation at MLPerf-Bench at HPCA’24](https://doi.org/10.5281/zenodo.10786893)).

* Supported AI, ML and Systems conferences to automate artifact evaluation
  and reproducibility initiatives (see CM at [ACM/IEEE MICRO’23](https://ctuning.org/ae/micro2023.html) 
  and [SCC’23/SuperComputing’23](https://github.com/mlcommons/ck/blob/master/docs/tutorials/scc23-mlperf-inference-bert.md)).



## Resources

* [GitHub project](https://github.com/mlcommons/ck)
* [Getting Started Guide](https://github.com/mlcommons/ck/blob/master/docs/getting-started.md)
* [CM-MLPerf commands](https://github.com/mlcommons/ck/tree/master/docs/mlperf)
* [CM-MLPerf GUI](https://access.cknowledge.org/playground/?action=howtorun)
* [Invited talk at MLPerf-Bench @ HPCA'24 about Automatically Composing High-Performance and Cost-effective AI Systems with MLCommons' CM and MLPerf](https://doi.org/10.5281/zenodo.10786893)
* [Invited keynote about CM framework at ACM REP'23](https://doi.org/10.5281/zenodo.8105339)
* [ACM artifact review and badging methodology](https://www.acm.org/publications/policies/artifact-review-and-badging-current) 
* [Artifact Evaluation at ML and systems conferences](https://cTuning.org/ae)
* [Terminology (ACM/NISO): Repeatability, Reproducibility and Replicability](artifact-evaluation/faq.md#what-is-the-difference-between-repeatability-reproducibility-and-replicability)
* [ACM TechTalk about reproducing 150+ research papers and validating them in the real world](https://www.youtube.com/watch?v=7zpeIVwICa4)
