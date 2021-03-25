const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function(){
  $('#message.alert').fadeOut('slow');
}, 3000);