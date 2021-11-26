let inp = document.getElementById('in')
console.log(inp)
inp.addEventListener("onkeyup",() => {
  console.log('up')
  inp.style.backgroundColor = "red";
})

inp.addEventListener("onkeydown",() => {
  console.log('down')
  inp.style.backgroundColor = "green";
})
