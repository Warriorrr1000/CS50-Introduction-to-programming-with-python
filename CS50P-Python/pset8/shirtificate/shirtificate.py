from fpdf import FPDF

def main():
    name = input("Name: ").strip()
    create_pdf(name)
def create_pdf(name):
    pdf = FPDF(orientation="P",format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()
    pdf.set_font("Helvetica", size=30)
    pdf.cell(w=0,text="CS50 Shirtificate",align="C")
    x = (pdf.w - 100) / 2
    pdf.image("shirtificate.png",x=x,w=100,y=60)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(2,70)
    pdf.set_font("Helvetica", size=20)
    pdf.cell(w=0,h=23,text=f"{name} took CS50",align="C")
    pdf.output("shirtificate.pdf")

if __name__=="__main__":
    main()