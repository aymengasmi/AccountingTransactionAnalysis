# AccountingTransactionAnalysis
#setup guide
---

## Installation
1. [Install Requirements](#requirements)

    1.1 [Install Java](#requirements-java)

    1.2 [Install Scala](#requirements-scala)

    1.3 [Install py4j](#requirements-py4j)

2. [Set Up Apache Spark](#spark) 

## Instructions

```bash
$ spark-submit bonify-challenge.py
```

---

In order to run Spark, we need Scala, which in turn requires Java. So, let's install these requirements first

<div id='requirements'/></div>
##1 | Install Requirements

<div id='requirements-java'/></div>
###1.1 | Install Java

```bash
$ sudo apt-add-repository ppa:webupd8team/java
$ sudo apt-get update
$ sudo apt-get install oracle-java7-installer
```

<div id='requirements-scala'/></div>
###1.2 | Install Scala

```bash
$ wget http://www.scala-lang.org/files/archive/scala-2.11.7.deb
$ sudo dpkg -i scala-2.11.7.deb
```

<div id='requirements-py4j'/></div>
###1.3 | Install py4j

PySpark requires the `py4j` python package.

```bash
$ pip install py4j
```

<div id='spark'/></div>
##2 | Install Apache Spark

```bash
$ wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz
$ tar xvf spark-2.0.0-bin-hadoop2.7.tgz
$ rm spark-2.0.0-bin-hadoop2.7.tgz
$ sudo mv spark-* /usr/local/spark 
$ export PATH = $PATH:/usr/local/spark/bin
$ exec bash
```
