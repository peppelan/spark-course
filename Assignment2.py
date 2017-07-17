from pyspark import SparkConf, SparkContext

def normalizeData(text):
    fields = text.split(',')
    return (int(fields[0]), float(fields[2]))

conf = SparkConf().setMaster("local").setAppName("TimeSpentByCustomerOrdered")
sc = SparkContext(conf = conf)

text = sc.textFile("file:///SparkCourse/customer-orders.csv")
results = text.map(normalizeData).reduceByKey(lambda x,y: x + y).map(lambda x: (x[1], x[0])).sortByKey().collect()

for result in results:
    customer = str(result[1])
    moneySpent = "%.2f" % result[0]
    print("Customer " + customer + " spent " + moneySpent)
