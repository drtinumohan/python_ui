#%%
# import sparknlp
import numpy as np
import pandas as pd
import streamlit as st

# from sparknlp.annotator import *
# from sparknlp.base import *


#%%


# @st.cache_resource
# def get_model(MODEL_NAME="deepset/xlm-roberta-base-squad2"):
#     spark = sparknlp.start()
#     document_assembler = (
#         MultiDocumentAssembler()
#         .setInputCols(["question", "context"])
#         .setOutputCols(["document_question", "document_context"])
#     )

#     spanClassifier_loaded = (
#         XlmRoBertaForQuestionAnswering.load("./{}_spark_nlp".format(MODEL_NAME))
#         .setInputCols(["document_question", "document_context"])
#         .setOutputCol("answer")
#     )

#     pipeline = Pipeline().setStages([document_assembler, spanClassifier_loaded])
#     return spark, pipeline


question = "What's my name?"
context = "My name is Clara and I live in Berkeley."
# spark, pipeline = get_model("deepset/xlm-roberta-base-squad2")
#

#%%


text_area = st.text_area(
    "context",
    value=context,
    height=300,
    max_chars=1500,
    key=None,
    help=None,
    on_change=None,
    args=None,
    kwargs=None,
    placeholder=None,
    disabled=False,
    label_visibility="visible",
)


text_input = st.text_input(
    "question",
    value=question,
    max_chars=None,
    key=None,
    type="default",
    help=None,
    autocomplete=None,
    on_change=None,
    args=None,
    kwargs=None,
    placeholder=None,
    disabled=False,
    label_visibility="visible",
)


if st.button("execute"):
    # example = spark.createDataFrame([[text_input, text_area]]).toDF(
    #     "question", "context"
    # )
    # result = pipeline.fit(example).transform(example)
    # st.write(result.select("answer.result").toPandas())
    st.write(f"{question}{text_input}")


# %%
