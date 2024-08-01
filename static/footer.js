const footer = document.querySelector('.foot')
fetch('/static/footer.html')
.then(res=>res.text())
.then(data=>{
    footer.innerHTML=data
})