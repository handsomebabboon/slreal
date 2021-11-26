let btn1 = document.getElementById('btn1')
let p1 = document.getElementById('counter')
let p2 = document.getElementById('display')
let count = 0
btn1.addEventListener("click",() => {
  count += 1
  p1.innerText = count
})

btn1.addEventListener("click",() => {
  p2.innerText += `button clicked ${count} times\n`
})

let f = document.getElementsByClassName('food')

for(let i=0;i<f.length;i+=1){
  f[i].addEventListener("click",(e) => {
    alert(`${e.target.innerText}`)
  })
}
