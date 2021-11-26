let btn = document.getElementById('btn1')
let f1 = document.getElementById('field1')
let f2 = document.getElementById('field2')
let tf = document.getElementById('tf')
btn1.addEventListener("click",() => {
  tf.innerText += `${f1.value} and ${f2.value}`
})
