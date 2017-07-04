docker run -d --name spark -e 'PYSPARK_PYTHON=python3' singularities/spark start-spark master

echo "Started Spark container."
echo " - To open a shell in the container, type \"docker exec -it spark bash\""
