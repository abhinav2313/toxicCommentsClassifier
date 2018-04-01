import pandas as pd
from file import Cleaner
from pyspark.sql import SparkSession

from pyspark.sql.types import *

from pyspark.sql.functions import length

from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF, StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vector

from pyspark.ml import Pipeline

from pyspark.ml.classification import NaiveBayes

def nb(object):
    
    data_train = pd.read_csv(object)

    # extract comment data
    comment_text = data_train['comment_text']

    # clean the text data

    clean = []
    for x in comment_text:
        clean.append(Cleaner(x))

    # add the clean data to the data frame 
    comment_col = pd.Series(clean)
    data_train['comment_text_clean'] = comment_col.values

    # print(data_train[:1])

    # drop id and comment_text columns 
    data_train.drop(['id', 'comment_text'], axis=1, inplace=True)

    # randomly select 10% of data
    data_train_10 = data_train.sample(frac=0.05)

    # Start a spark session

    spark = SparkSession.builder.appName('naivebayes').getOrCreate()

    mySchema = StructType([ StructField("toxic", IntegerType(), True)\
                       ,StructField("severe_toxic", IntegerType(), True)\
                       ,StructField("obscene", IntegerType(), True)\
                       ,StructField("threat", IntegerType(), True)\
                       ,StructField("insult", IntegerType(), True)\
                       ,StructField("identity_hate", IntegerType(), True)\
                       ,StructField("comment_text_clean", StringType(), True)])

    spark_df = spark.createDataFrame(data_train_10, schema=mySchema)

    data = spark_df.withColumn('length', length(spark_df['comment_text_clean']))

    # Create all the features to the data set
    # ham_spam_to_num = StringIndexer(inputCol='class',outputCol='label')
    tokenizer = Tokenizer(inputCol="comment_text_clean", outputCol="token_text")
    stopremove = StopWordsRemover(inputCol='token_text',outputCol='stop_tokens')
    hashingTF = HashingTF(inputCol="token_text", outputCol='hash_token')
    idf = IDF(inputCol='hash_token', outputCol='idf_token')

    # Create feature vectors
    clean_up = VectorAssembler(inputCols=['idf_token', 'length'], outputCol='features')

    data_prep_pipeline = Pipeline(stages=[tokenizer, stopremove, hashingTF, idf, clean_up])

    # Fit and transform the pipeline
    cleaner = data_prep_pipeline.fit(data)
    cleaned = cleaner.transform(data)

    # Show label of ham spame and resulting features
    toxic_df = cleaned.select(['toxic', 'features'])

    toxic_df = toxic_df.withColumnRenamed("toxic", "label")

    print((toxic_df.count(), len(toxic_df.columns)))

    # Break data down into a training set and a testing set
    (training, testing) = toxic_df.randomSplit([0.7, 0.3])

    # Create a Naive Bayes model and fit training data
    model_nb = NaiveBayes(smoothing=1.0, modelType='multinomial')

    return model_nb

