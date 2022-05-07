'''Generating PDF and Tex files from selected questions'''
from pylatex import Document, Command
from pylatex.utils import NoEscape

STUDENTS_NAME = """
\\vspace{5mm}
\\makebox[0.75\\textwidth]{Student's name:\\enspace\\hrulefill}
\\vspace{5mm}
"""

def fill_document(doc, questions):
    '''Adding selected questions to the document'''
    for question in questions:
        if question.type == "Multiple Choice":
            answers = "\n".join([f"\\choice {x['body']}" for x in question.answers])
            question_latex = f"""
\\vspace{{5mm}}
\\question {question.body}

\\begin{{oneparchoices}}
{answers}
\\end{{oneparchoices}}
            """
            doc.append(NoEscape(question_latex))

        elif question.type == "Short Answer":
            keypoints = "\n".join([f"\\part {x}" for x in question.key_points])
            question_latex = f"""
\\vspace{{5mm}}
\\question Answer the following question in a short essay with no more than {question.max_word_count} words, while addressing the following key points:
\\begin{{parts}}
{keypoints}
\\end{{parts}}
\\vspace{{\\stretch{{{round(int(question.max_word_count) / 50)}}}}}
            """
            doc.append(NoEscape(question_latex))

def generate_pdf(questions):
    '''Generating PDF'''

    doc = Document(documentclass='exam')
    doc.preamble.append(Command('title', 'Awesome Title'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NoEscape(STUDENTS_NAME))
    fill_document(doc, questions)
    doc.generate_pdf('temp/example', clean_tex=False)
    doc.generate_tex('temp/example')
