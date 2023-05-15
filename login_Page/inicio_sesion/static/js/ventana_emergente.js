function toggleDiv() {
  var div = document.getElementById('popup');
  var iframe = document.getElementById('Ventana');
  if (div.style.display === 'none') {
    iframe.style.display = 'none';
    div.style.display = 'block';
  } else {
    iframe.style.display = 'block';
    div.style.display = 'none';
  }
}

function cerrarVentana() {
  var div = document.getElementById('popup');
  div.style.display = 'none';
}
