let cart_label=document.getElementById('cart-label')
let cart_update_btn=document.getElementsByClassName('cart-up-button')
let num=1
function update(){
    cart_label.textContent=num;
    num++

}
for (let i=0;i<cart_update_btn.length;i++){
    cart_update_btn[i].addEventListener('click',update)
}
