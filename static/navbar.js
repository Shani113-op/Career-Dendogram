const nav = document.querySelector('.navbar')
fetch('/static/navbar.html')
.then(res=>res.text())
.then(data=>{
    nav.innerHTML=data
})