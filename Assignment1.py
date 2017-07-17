from pyspark import SparkConf, SparkContext

def normalizeData(text):
    fields = text.split(',')
    return (int(fields[0]), float(fields[2]))

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

text = sc.textFile("file:///SparkCourse/customer-orders.csv")
results = text.map(normalizeData).reduceByKey(lambda x,y: x + y).collect()

for result in results:
    customer = str(result[0])
    moneySpent = str(result[1])
    print(customer + ":\t\t" + moneySpent)
