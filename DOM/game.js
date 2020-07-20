var one = document.querySelector('table')
var two = document.querySelector('#butt')

one.addEventListener('click',function()){
  one.textContent = "X"
  one.style.color = "black"
}

one.addEventListener("dblclick",function()){
  one.textContent = "O"
  one.style.color = "black"
}

two.addEventListener('click',function()){
  one.textContent = " "
}
