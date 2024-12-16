import boto3
import json

# AWS Textract client integration
textract = boto3.client(
    'textract',
    aws_access_key_id='A--------------L',
    aws_secret_access_key='41----------------------------lGZ',
    region_name='ap-south-1' # mumbai region has been used for india
)

def extract_text_from_image(image_path):
    """Extract text from an image using Amazon Textract.
    Input Parameters = param image_path : Path to the image file
    Output = return Extracted text (as a string)    """
    
  with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    response = textract.detect_document_text(Document={'Bytes': image_bytes})

    extracted_text = ""
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            extracted_text += block['Text'] + '\n'

    return extracted_text


image_path = "C:/Users/-----.jpg"  # path to photograph 
text = extract_text_from_image(image_path)
print("Extracted Text:\n", text)
