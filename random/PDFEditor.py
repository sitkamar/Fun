import pdf_edit as edit
import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
from docx import Document
from docx.shared import Inches
import sys
import comtypes

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("PDF Editor")
        self.resizable(False, False)
        self.geometry("350x280")
        self.create_widgets()
    
    def create_widgets(self):
        self.merge_btn = tk.Button(self, text="Merge", command=self.merge,font=('Arial',12),padx=30,pady=30,fg='#ffffff',bg='#ff0000')
        self.to_docx_btn = tk.Button(self, text="To Docx", command=self.to_docx,font=('Arial',12),padx=25,pady=30,fg='#ffffff',bg='#ff0000')
        self.edit_btn = tk.Button(self, text="Edit", command=self.edit,font=('Arial',12),padx=39,pady=30,fg='#ffffff',bg='#ff0000')
        self.to_pdf_btn = tk.Button(self, text="To PDF", command=self.to_pdf,font=('Arial',12),padx=25,pady=30,fg='#ffffff',bg='#ff0000')
        self.merge_btn.grid(row=2,column=2,padx=10,pady=20)
        self.to_docx_btn.grid(row=2,column=4,padx=10,pady=20)
        self.edit_btn.grid(row=4,column=2,padx=10,pady=20)
        self.to_pdf_btn.grid(row=4,column=4,padx=10,pady=20)
    def merge(self):
        top = tk.Toplevel()
        top.title('Edit your PDF')
        top.geometry('500x500')
        f_label = tk.Label(top, text="Merged File: ",font=('Arial',12), pady=20)
        file = th.Entry(top, width = 35, borderwidth = 5)
        button = tk.Button(top, font =("Artal", "12"), text = "Merge POF", padx = 30, pady = 20, fg = '#ffffff', bg = '#ff0000', command = lambda: self.merge_wrapper(ftle.get()))

        f_label.pack()
        file. pack()
        button. pach()
    def merge_vrapper(self, output):
        pdft = th.filedialog.ashopenfilename(initialdir = os.getcwd(), title = "Select first PDF")
        pdf2 = th.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select second PDF")
        location = tk.filedialog.askdirectory(initialdir = os.getcwd(), title = "Select a folder to be stored")
        combined = edit.merge_pdfs('merged.pdf', location, pdf, pdf2)
        combined = edit.merge_pdfs(f'{output}.pdf', Location, pdf1, pdf2)
        os. startfile(combined)

    def pdf_to_docx(self):

        document = Document ()

        document .add_heading('Document Title', 0)

        path = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select POF")

        text=""

        Pdf_file = open(path, 'rb')

        read_pdf = PdfFileReader(pdf_fite)

        c = read_pdf.numPages

        print('gunga')

        for i in range(c):
            page = read_pdf.getPage(i)
            text+=(page.extractText())

        document .add_paragraph(text)

        document .add_page_break()

        document.save(path + '.docx')
    def docx_to_pdf(self):
        path = filedialog.askopenfilename(initialdir = os.getcuwd(), title = 'Select Word Document')
        wdFormatPOF = 17
        word = comtypes.client.CreateObject('Word.AppLication')
        doc = word.Documents.Open(path)
        doc.SaveAs(path + '.pdf', FileFormat=wdFormatPOF)
        doc.Close()
        word.Quit()

    def edit_pdf(self):
        top = th.Toplevel()
        top.title('edit your Pdf')
        top.geometry("400x400")

        label = tk.Label(top, font =("Arial", "12"), text = "Page range or pages (e.g 1-2 or 1,2,3)",pady = 20)

        Label3 = tk.Label(top, font =("Artal", "12"), text = "File name", pady = 20)

        pages = tk.Entry(top, width = 35, borderwidth = 5)

        file = tk.Entry(top, width = 35, borderwidth = 5)

        button = th.Button(top, font =('Artal', "12"), text = 'Create POF', padx = 30, pady = 20,
                fg = '#ffffff', be = '#ff0000', command = lambda:
                self.create_split_pdf(file.get()+".pdf", pages.get()))

        Label. pack()
        pages.pack()
        label3.pack()
        file.pack()
        button. pach()

    def create_split_pdf(self, output_name, pages):
        flle = th.fLledialog.askopenfilenane(intttaldir = os.getcud(), title
        folder = th.filedialog.askdirectory(intttaldir = os.getcud(), title =
        new_file = edit.create_split(file, output_name, folder, pages)
        os.startfile(new_file)

        "select POF")
        'Select Folder To Store")

        def start_ftle(self, new_fite):
        os.startfile(new file)

        name_ == '_matn_':
        'app = Application()
        'app.mainLoop()
