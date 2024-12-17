# InkCredible
### College Minor Project 
### It uses Amazon Texteract API to extract Text from Image.
### It then processes the sentences and using NLP libraries, corrects the sentences and summarizes too if needed. 
### The grammar correction is done using language_tool_python library. 
### The summarization can be done using two models available and tested :-
### 1. Pegasus     2. FineTunedBartSummarizer
### At last, it stores the text in a doc file in same folder to later perform word processing and save as pdf. 
### To Run the Summarization Code, make sure to install transformers and the required NLP libraries such as pytorch, huggingface/transformers, sentencepiece, pegasus & suriya/finetuneBartmodel.
### For Grammar Correction & Saving the Document Code, download and import python-docx and language-tool-python.
### For Text Extraction & Using Amazon Texteract, Create a User Account with desired plan ( avoid using root user id passcode for this ), assign a user the needed permissions and setup an aws environment, obtain a passkey and credentials mentioned from the accounts page, and continue while downloading and imporing boto3 and json in the file before starting. 
### Here is the code to import necessary libraries: 
```!pip install git+https://github.com/PyTorchLightning/pytorch-lightning
!pip install git+https://github.com/huggingface/transformers
!pip install sentencepiece
!pip install git+https://github.com/stas00/transformers
!pip install pegasus

!pip install python-docx
!pip install language-tool-python

!pip install boto3

