from flask import Flask, render_template,request
from pdfs import create_pdf
from xhtml2pdf import pisa
#from flask_weasyprint import HTML, render_pdf
#from flask_mail import Mail, Message

app = Flask(__name__)
#mail_ext = Mail(app)

sourceHtml = '/static/facturas.html'
outputFilename = "test3.pdf"


def convertHtmlToPdf(sourceHtml, outputFilename):
    # open output file for writing (truncated binary)
	resultFile = open(outputFilename, "w+b")

    # convert HTML to PDF
	pisaStatus = pisa.CreatePDF(
            sourceHtml,                # the HTML to convert
            dest=resultFile)           # file handle to recieve result

    # close output file
	resultFile.close()                 # close output file

    # return True on success and False on errors
	return pisaStatus.err


@app.route('/')
def Login():
    return render_template('login.html')
	
@app.route('/factura/', methods = ['GET', 'POST'])
def factura():

	
	#subject = "Mail with PDF"
	#receiver = "carlosklr48@gmail.com"
	#mail_to_be_sent = Message(subject=subject, recipients=[receiver])
	#mail_to_be_sent.body = "This email contains PDF."
	#pdf = create_pdf(render_template('facturas.html'))
	#mail_to_be_sent.attach("file.pdf", "Facturacion/pdf", pdf.getvalue())
	#mail_ext.send(mail_to_be_sent)
	#return redirect(url_for('other_view'))
		
	print 'El metodo hello ha sido llamado'
	
	if request.method == 'POST':
		#convertHtmlToPdf(sourceHtml, outputFilename)
		rfc_emisor = request.form['rfc']
		nombre_emisor = request.form['nombre']
		calle_emisor = request.form['calle']
		numeroext_emisor = request.form['numext']
		numeroint_emisor = request.form['numint']
		colonia_emisor = request.form['colonia']
		municipio_emisor = request.form['mun']
		estado_emisor = request.form['estado']
		pais_emisor = request.form['pais']
		cp_emisor = request.form['cp']
		print rfc_emisor
		
		rfc_receptor = request.form['rfc']
		nombre_receptor = request.form['nombre']
		calle_receptor = request.form['calle']
		numeroext_receptor = request.form['numext']
		numeroint_receptor = request.form['numint']
		colonia_receptor = request.form['colonia']
		municipio_receptor = request.form['mun']
		estado_receptor = request.form['estado']
		pais_receptor = request.form['pais']
		cp_receptor = request.form['cp']
		
		fecha_exp = request.form['fexp']
		serie = request.form['serie']
		folio = request.form['folio']
		forma_pago = request.form['forma']
		metodo_pago = request.form['metodo']
		condicion_pago = request.form['condpago']
		
		cantidad = request.form['cant']
		descripcion = request.form['desc']
		precio = request.form['precio']
		

		#TODO: Obtener los demas campos
		
		return render_template('facturas.html') #TODO: qe hacer despues de guardar los datos 
	else:
		return render_template('facturas.html')	    


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug = True)
	pisa.showLogging()
	convertHtmlToPdf(sourceHtml, outputFilename)
	
