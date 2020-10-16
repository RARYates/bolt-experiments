# Bolt Samples

This repository contains the simplest implementation of Bolt concepts we can pull together. This is VERY MUCH
work in progress

## Main Notes

* Need a method to grab data in one task, set it as a variable in the plan, and use the data in a follow-on
task run by the plan
* All code in this repo should be considered a short-term best attempt, at this phase.

## Boltdir

This Boltdir is designed to ensure python_task_helper is available. In the future, it should also bring in
ruby_task_helper. Python is a more common language seen in DevOps practitioners, so we'll start there. Can
consider shell again in the future as well.

## site-modules

### stuff

Stuff is my second attempt at building a task that generates data in the first task, and writes it out to a file in the second.
This site-module should absolutely be renamed to something sensical when we have a data in/data out sample in Python.

#### Contents:

* Plan: rw.pp - Runs stuff::read and stuff:write. Creates Data for both, attempts to use the data.
  * Note: https://github.com/matthewrstone/gpno/blob/master/plans/create_manifest.pp <-- Good Sample
* Task: stuff::read - Cracks open /etc/hosts and /etc/resolv.conf and returns the contents as a string
  * Note: Not JSON blob - See sample::structure.py
  * Note: Although this is powershell, notice we're dumping the data into JSON for the plan (https://github.com/matthewrstone/gpno/blob/master/tasks/export.ps1#L56)
* Task: stuff::write - Takes in data, and writes to a file called test.txt - Meant to prove data has been moved from task to task
  * Note: This task, on this file line, contains a sample of finding our data from within the ResultSet: (https://github.com/matthewrstone/gpno/blob/master/tasks/create_resources_nix.py#L14)

### sample

Sample is my first attempt at building a task that generates data in the first task (generate.py) and places it
into a file in my second task (read.py). This set of code remains as a building block, but should be removed
as "stuff" comes to fruitition. This module has been set aside so that components aren't lost that may be of value.

Tl;dr: This project outgrew my simple use case, but I didn't want to lose progress. Looking to do something more targeted in "stuff"

#### Contents:

* Plan: example.pp - The plan that ties it all together
* generate.py - Scans /etc/conf and etc/resolv.conf
  * generate.json - Controls input, brings in task helper during runtime
* read.py - Opens a file and dumps contents (I know, the name is awful. Scratch work)
  * read.json - Controls input, brings in task helper during runtime
* structure.py - lazily stolen, but does a simple job of snatching up some OS info and dropping it as JSON output (Quality Working Block for Costco use-case)
* 
