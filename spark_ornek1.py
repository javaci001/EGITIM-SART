# coding=utf-8

"""
docker container cp spark_ornek1.py spark-master:/spark/bin
./spark-submit spark_ornek1.py spark://spark-master:7077 hdfs://namenode:9820/deneme/istiklalmarsi.txt
"""

from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark import SparkConf
import sys


if __name__ == "__main__":
    if(len(sys.argv)) != 3:
        print("lütfen argumanları giriniz. namenode ve spark olanı")
        print("su sekilde :   ./spark-submit spark_ornek1.py spark://spark-master:7077 hdfs://namenode:9820/deneme/istiklalmarsi.txt ")
        sys.exit(1)

    sparkmaster = sys.argv[1]
    namenodemaster = sys.argv[2]
    print("====================================================================")
    print("Sparkmaster Bilgisi : ", sparkmaster)
    print("Namenode Bilgisi : " ,namenodemaster )
    print("====================================================================")
    conf = SparkConf().setAppName("ilk olacak inşallah").setMaster(sparkmaster)
    sc = SparkContext(conf=conf)

    data1 = sc.textFile(namenodemaster)
    print(data1.count())

    print("merhaba dünyammm")
