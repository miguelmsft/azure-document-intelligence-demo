# Azure Document Intelligence Demo - Create Searchable PDF files
This repository shows a demo of how to convert image files into searchable pdf files. 

## Step 1. Convert from image file to pdf (non-searchable) file. 
If you have image files, use the code in `convert_pdf.py` to convert them to (non-searchable) pdf files. Currently, Azure Document Intelligence can produce searchable pdf files from (non-searchable) pdf files as input. Support for creating searchable pdf files from other input types such as images will be available later in 2024. In this example, `receipt-image.jpg` is converted to `receipt-nonsearchable.pdf`.

## Step 2. Create Azure Document Intelligence resource.
If you haven't done so already, create an Azure Document Intelligence resource. Here is the [documentation page](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/create-document-intelligence-resource?view=doc-intel-4.0.0)

## Step 3. Perform POST request.
Use the template in `request_template_post.bash` to perform a POST request to your Azure Document Intelligence resource. To this request template, simply add your Azure Document Intelligence endpoint URL, resource key, and the source input PDF file. The response will show the `apim-request-id`. In this example, `receipt-nonsearchable.pdf` is the input file for the POST request. 

## Step 4. Perform GET request. 
Use the template in `request_template_get.bash` to perform a GET request to obtain the searchable pdf file. To this request template, simply add your Azure Document Intelligence endpoint URL, resource key, the `apim-request-id` string from the POST request, and the name you want for the output file. The response will send you the searchable pdf. In this example, `receipt-searchable.pdf` is the searchable pdf that gets created. 

Here is the documentation for [creating searchable pdf files in Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept-read?view=doc-intel-4.0.0&tabs=sample-code#searchable-pdf)
