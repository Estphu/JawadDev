from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.files.storage import FileSystemStorage
from docx import Document
from pdf2docx import parse

# Create your views here.
class pdftodocx(View):
    def get(self, request):
        context = {
            'convert': {
                'ready': False,
            },
            'download': {
                'isDone': False,
            }
        }
        return render(request, 'pdftodocx/pdftodocx.html', context=context)
    
    def post(self, request):
        selectedFile = request.FILES['selectedFile']
        fs = FileSystemStorage(location="media/pdftodocx/pdf/")
        fs.save(selectedFile.name, selectedFile)
        print(selectedFile)
        docs_path = 'media/pdftodocx/word/SampleDocx.docx'
        pdf_path = f'media/pdftodocx/pdf/{selectedFile.name}'
        parse(pdf_path, docs_path)
        fs.delete(selectedFile.name)
        context = {
            'convert': {
                'name': selectedFile.name,
                'ready': True,
            },
            'download': {
                'isDone': True,
            }
        }
        return render(request, 'pdftodocx/pdftodocx.html', context=context)
    
def download_docx(request, fileName):
    updated_fileName = fileName.split('.pdf')
    document = Document('media/pdftodocx/word/SampleDocx.docx')
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = f'attachment; filename={updated_fileName[0]}.docx'
    document.save(response)
    return response    
