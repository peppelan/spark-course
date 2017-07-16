To prepare the dev environment (Docker-based Spark installation), after installing Docker, run, from the top folder:
```bash
docker run --rm -it --name sparkdev -v `pwd`:/SparkCourse -p 4040:4040 gettyimages/spark:2.1.1-hadoop-2.7
```

For checking the correct installation (as suggested in the course), you can open a PySpark shell by running:
`docker exec -it sparkdev /usr/spark-2.1.1/bin/pyspark`, where the following lines: 

```python
dd = sc.textFile("README.md")
rdd.count()
```

will print the line count of that file (104 in this case)


Datasets:
- ml-100k from grouplens.org

