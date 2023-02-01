/* ----- Puxar Tags HTML existentes ----- */

var header = document.querySelector('header')
var head = document.querySelector('head')

/* ----- Criar novas Tags ----- */

var link_favicon = document.createElement('link')

var h1_header = document.createElement('h1')
var a_header = document.createElement('a')

var br = document.createElement('br')

/* ----- Configurar Tags ----- */

link_favicon.rel="shortcut icon" 
link_favicon.href="../../2.imagens/phi-48-15-60.jpg"
link_favicon.type="image/x-icon"

/*
<link 
        rel="shortcut icon" 
        href="2.imagens/phi - 48-15-60.jpg" 
        type="image/x-icon">
*/

h1_header.innerHTML = 'Paixões Filosóficas'
a_header.href = "https://developerlucassouza.github.io/paixoes.filosoficas/"

/* ----- Colocando em Prática ----- */

head.appendChild(link_favicon)

a_header.appendChild(h1_header)
header.appendChild(a_header)