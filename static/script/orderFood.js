function decrementQuantity(element){

    let itemId = element.name
    let itemQuantity = document.getElementById(itemId).value
    let subTotal = document.getElementById(itemId+"_subTotal").innerHTML
    let grandTotal = document.getElementById("grandTotal").value
    let itemPrice = document.getElementById(itemId+"_price").innerHTML

    if(itemQuantity>0){

        itemQuantity= itemQuantity-1
        document.getElementById(itemId).value = itemQuantity

        grandTotal = grandTotal - itemPrice
        subTotal = subTotal - itemPrice
        document.getElementById("grandTotal").value = grandTotal
        document.getElementById(itemId+"_subTotal").innerHTML = subTotal

    }

}

function showPassword(){

    let passwordType = document.getElementById("password").type

    if(passwordType==='text'){

        passwordType='password'
        document.getElementById("password").type=passwordType

    }

    else{

        passwordType='text'
        document.getElementById("password").type=passwordType

    }

}

function incrementQuantity(element){

    let itemId = element.name
    let itemQuantity = document.getElementById(itemId).value
    let subTotal = Number(document.getElementById(itemId+"_subTotal").innerHTML)
    let grandTotal = Number(document.getElementById("grandTotal").innerHTML)
    let itemPrice = Number(document.getElementById(itemId+"_price").innerHTML)

    itemQuantity = Number(itemQuantity)+1
    document.getElementById(itemId).value = itemQuantity

    grandTotal = grandTotal + itemPrice
    subTotal = subTotal + itemPrice
    document.getElementById("grandTotal").innerHTML = grandTotal
    document.getElementById(itemId+"_subTotal").innerHTML = subTotal

}