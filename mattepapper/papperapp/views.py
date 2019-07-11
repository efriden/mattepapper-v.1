from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

import pylatex

from django_tex.shortcuts import render_to_pdf

def test(request):
    template_name = 'tex/test.tex'
    context = {'foo': 'Bar'}
    return render_to_pdf(request, template_name, context, filename='test.pdf')

def fractions(request):
	template_name = 'tex/fractions.tex'
	context = {'foo': 'Bar'}
	return render_to_pdf(request, template_name, context, filename='test.pdf')