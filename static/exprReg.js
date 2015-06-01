function ValidaCampos(rfcc) {
 
var regexrfc = /^[A-Z]{4}\d{6}[a-zA-Z0-9]{3}$/;
 
if(regexrfc.test(rfcc.rfc_emisor.value)==false)
{
alert("El RFC no es valido");
return false;
}
 
alert('Se ingreso RFC correcto');
return true;
}
function ValidarCampos(rfccc) {
 
var regexrfc = /^[A-Z]{4}\d{6}[a-zA-Z0-9]{3}$/;
 
if(regexrfc.test(rfccc.rfc_receptor.value)==false)
{
alert("El RFC no es valido");
return false;
}
 
alert('Se ingreso RFC correcto');
return true;
}