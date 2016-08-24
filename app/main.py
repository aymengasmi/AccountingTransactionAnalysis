from datetime import datetime
from pyspark.sql import SQLContext, Row
from pyspark import SparkConf, SparkContext
from pyspark.ml.classification import LogisticRegression


APP_NAME = " AccountingTransactionAnalysis "


def get_datetime(dt):
    return datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')


def main(sc):
    sqlContext = SQLContext(sc)
    transactions_df = sqlContext.read.json("data_input.json")
    transactions_df.registerTempTable("transactions")

    transactions_df.printSchema()   # Print the schema in a tree format
    transactions_df.show()  # Show the content of the DataFrame

    # count booking types
    transactions_df.groupBy('bookingType').count().show()

    # amount by booking types
    transactions_df.groupBy('bookingType').sum('amount').show()

    # amount by booking date
    transactions_df.groupBy('bookingDate').sum('amount').show()

    sqlContext.sql("SELECT bookingDate, bookingType, amount FROM transactions ORDER BY (bookingDate, bookingType)").show()

    bookingDateDF = transactions_df.toPandas()
    bookingDateDF['bookingFullDate'] = [date for date in bookingDateDF['bookingDate']]
    bookingDateDF['bookingDay'] = [get_datetime(date).day for date in bookingDateDF['bookingDate']]
    bookingDateDF['bookingMonth'] = [get_datetime(date).month for date in bookingDateDF['bookingDate']]
    bookingDateDF['bookingDate'] = [date[:11] for date in bookingDateDF['bookingDate']]
    bookingDateDF.index = bookingDateDF['bookingDate']
    amount_plot = bookingDateDF['amount'].plot()
    fig = amount_plot.get_figure()
    fig.savefig("output.png")

    new_tr_df = sqlContext.createDataFrame(bookingDateDF)
    new_tr_df.show()


if __name__ == "__main__":
    # Configure Spark
    conf = SparkConf().setAppName(APP_NAME)
    conf = conf.setMaster("local[*]")
    sc = SparkContext(conf=conf)

    main(sc)
